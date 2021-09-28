'''
interface_grafica.py

Programa para automatizar rodar simulações Monte Carlo usando o 
PENELOPE v.2014 com a extensão penEasy v.2015.

para rodar este programa é necessaria as subrotinas seguintes
estejam na mesma pasta:

    create_geo.py
    get_out.py
    graph.py
    run_simulation.py
    set_in.py

                Autor: Hitalo Rodrigues Mendes 
                        (hitalo.rm@gmail.com)
                
                Data: 2021/09/21
'''


import PySimpleGUI as sg
from matplotlib.pyplot import figure, cla, clf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import graph
_VARS = {'window':False,
         'fig_agg': False,
         'pltFig': False}

font = ("Arial, 13")
font1 = ("Arial, 14")
font2 = ("Arial, 5")
font3 = ("Arial, 10")
    
    
def draw_figure(canvas, figura):
        figure_canvas_agg = FigureCanvasTkAgg(figura, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    
def drawChart(canvas, figura,fig_agg,first):
    if first:
        figura = figure(figsize = (12,4.25))
        first = False
    
    else:
        fig_agg.get_tk_widget().pack_forget()
        clf()
        cla()
    graph.graph_track()
        
    fig_agg = draw_figure(canvas, figura)
        
    return fig_agg, figura, first
    
def win_track():
    #Layout
    AppFont = 'Any 16'

    layout = [
        [sg.Text('Tipo de partícula', font=font),
                 sg.Radio('Elétron','kpar',key='electron', font=font),
                 sg.Radio('Fóton','kpar',key='photon',default='photon', font=font),
                 sg.Radio('Pósitron','kpar',key='positron', font=font)],

        [sg.Text('',font = font2)],
        [sg.Text('Energia',size=(10,0), font=font),
                     sg.Slider(range=(10,2000),
                               default_value=0,orientation='h',
                               size =(25,20),key = 'sliderEnergy', font=font),
            sg.Text('keV',size=(8,1), font=font),

            sg.Text('   ',font = font2),
        sg.Text('Número de Histórias',size=(10,0), font=font),
             sg.Slider(range=(10,200.0),
                       orientation='h',
                       default_value=1,
                       size =(20,20),
                       key = 'sliderHist',
                       font = font)],
         
         
        [sg.Text('',font = font2)],
        [sg.Text('Material', font=font1)],
         
        [sg.Radio('Hidrogêneio',"mat",key='H', font=font),
                 sg.Radio('Carbono',"mat",key='C', font=font),
                 sg.Radio('Nitrogênio',"mat",key='N', font=font),
                 sg.Radio('Oxigênio',"mat",key='O', font=font),
                 sg.Radio('Alumínio',"mat",key='Al', font=font),
                 sg.Radio('Prata',"mat",key='Ag', font=font),
                 sg.Radio('Cobre',"mat",key='Cu',default='agua', font=font),
                 sg.Radio('Molibdênio',"mat",key='Mo', font=font),
                 sg.Radio('Chumbo', 'mat', key='Pb',font=font),
                 sg.Radio('Tungstênio','mat',key='W',font=font)],
        [sg.Text('',font = font2)],
        [sg.Text('Espessura do cilindro',
                 size=(20,0), 
                 font=font),
        sg.Slider(range=(100,1000),
                  default_value=0,
                  orientation='h',
                  size =(15,20),
                  key = 'sliderThick',
                  font=font),
        sg.Text('mm',size=(8,1), font=font)],

        [sg.Button('Simular', font=font1)],
        #[sg.Output(size=(40,15), font=font),
        [sg.Canvas(key='figCanvas')],
        [sg.Text('by: Hitalo R. Mendes',justification='left')]
    ]


    #Janela
    return sg.Window('TRACKING DE PARTÍCULAS',
                        layout,
                        finalize=True,
                        resizable=True,
                        font=font1,
                        location=(100, 100),
                        element_justification="left")
        
    
