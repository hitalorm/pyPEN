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
from matplotlib.pyplot import figure
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
        figura = figure(figsize = (6,4))
        first = False
    else:
        fig_agg.get_tk_widget().pack_forget()
    
    graph.graph_SDD()
    fig_agg = draw_figure(canvas, figura)
        
    return fig_agg, figura, first
    
def win_dose():
    #Layout
    AppFont = 'Any 16'

    layout = [
        [sg.Text('Tipo de partícula', font=font)],
        [sg.Radio('Elétron','kpar',key='electron', font=font),
                 sg.Radio('Fóton','kpar',key='photon',default='photon', font=font),
                 sg.Radio('Pósitron','kpar',key='positron', font=font)],

        [sg.Text('',font = font2)],
        [sg.Text('Energia',size=(7,0), font=font),
             sg.Slider(range=(10,20000),default_value=0,orientation='h',size =(60,20),key = 'sliderEnergy', font=font),
             sg.Text('keV',size=(8,1), font=font)],

        [sg.Text('',font = font2)],
        [sg.Text('Número de Histórias',size=(20,0), font=font),
             sg.Slider(range=(1,200.0),
                       orientation='h',
                       default_value=1,
                       size =(30,20),
                       key = 'sliderHist',
                       font = font),
             sg.Text('x1e5',size=(8,0), font=font)],
        [sg.Text('',font = font2)],
        [sg.Text('Material', font=font1)],

        [sg.Radio('Acrílico',"mat",key='PMMA', font=font),
                 sg.Radio('Adiposo',"mat",key='adipose', font=font),
                 sg.Radio('Água',"mat",key='agua',default='agua', font=font),
                 sg.Radio('Músculo',"mat",key='muscle', font=font),
                 sg.Radio('Osso', 'mat', key='bone',font=font),
                 sg.Radio('Pulmão','mat',key='lung',font=font),
                 sg.Radio('Tecido Mole',"mat",key='soft', font=font)],
        [sg.Text('',font = font2)],
        [sg.Text('Espessura da caixa',
                 size=(20,0), 
                 font=font),
        sg.Slider(range=(1,5),
                  default_value=0,
                  orientation='h',
                  size =(15,20),
                  key = 'sliderThick',
                  font=font),
        sg.Text('cm',size=(8,1), font=font)],

        [sg.Button('Simular', font=font1),sg.Button('Salvar Imagem', font=font1),sg.Button('Exportar gráfico como csv', font=font1)],
        [sg.Canvas(key='figCanvas'),sg.Output(size=(40,15), font=font)],
        [sg.Text('by: Hitalo R. Mendes',justification='left')]
    ]

    #Janela
    return sg.Window('ANÁLISE DEPOSIÇÃO DE DOSE',
                        layout,
                        finalize=True,
                        resizable=True,
                        font=font1,
                        location=(100, 100),
                        element_justification="left")
        
    
