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


import numpy as np
import pandas as pd
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import set_in
from create_geo import create_geometry_file
import run_simulation as run
import graph
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
from get_out import get_out

_VARS = {'window':False,
         'fig_agg': False,
         'pltFig': False}

font = ("Arial, 13")
font1 = ("Arial, 14")
initial_dir = os.getcwd()
    
    
def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    
def drawChart():
        _VARS['pltFig'] = plt.figure(figsize = (6,5))
        #graph.graph_SDD()
        graph.blanck()
        _VARS['fig_agg'] = draw_figure(
        _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])

def updateChart():
    _VARS['fig_agg'].get_tk_widget().pack_forget()
    #dataXY = makeSynthData()
    plt.cla()
    plt.clf()
    #plt.plot(dataXY[0], dataXY[1], '.k')
    graph.graph_SDD()
    _VARS['fig_agg'] = draw_figure(
        _VARS['window']['figCanvas'].TKCanvas, _VARS['pltFig'])

    
class TelaPython:
    
    def __init__(self):
        #Layout
        AppFont = 'Any 16'
        
        layout = [
            [sg.Text('Tipo de partícula', font=font)],
            [sg.Radio('Elétron','kpar',key='electron', font=font),
                     sg.Radio('Fóton','kpar',key='photon',default='photon', font=font),
                     sg.Radio('Pósitron','kpar',key='positron', font=font)],
            
            [sg.Text('')],
            [sg.Text('Energia',size=(7,0), font=font),
                 sg.Slider(range=(10,1000),default_value=0,orientation='h',size =(30,20),key = 'sliderEnergy', font=font),
                 sg.Text('keV',size=(8,1), font=font)],
            
            [sg.Text('')],
            [sg.Text('Número de Histórias',size=(20,0), font=font),
                 sg.Slider(range=(100,10000.0),
                           orientation='h',
                           default_value=1,
                           size =(30,20),
                           key = 'sliderHist',
                           font = font),
                 sg.Text('milhares',size=(8,0), font=font)],
            [sg.Text('')],
            [sg.Text('Material', font=font1)],
                     
            [sg.Radio('Acrílico',"mat",key='PMMA', font=font),
                     sg.Radio('Adiposo',"mat",key='adipose', font=font),
                     sg.Radio('Água',"mat",key='agua',default='agua', font=font),
                     sg.Radio('Músculo',"mat",key='muscle', font=font),
                     sg.Radio('Osso', 'mat', key='bone',font=font),
                     sg.Radio('Pulmão','mat',key='lung',font=font),
                     sg.Radio('Tecido Mole',"mat",key='soft', font=font)],
            [sg.Text('')],
            [sg.Text('Espessura do cilindro',
                     size=(20,0), 
                     font=font),
            sg.Slider(range=(1,5),
                      default_value=0,
                      orientation='h',
                      size =(15,20),
                      key = 'sliderThick',
                      font=font),
            sg.Text('cm',size=(8,1), font=font)],
            
            [sg.Button('Simular', font=font1),sg.Button('Fechar', font=font1)],
            [sg.Output(size=(50,20), font=font),sg.Canvas(key='figCanvas')],
        ]
        
        
        #Janela
        _VARS['window'] = sg.Window('CONFIGURAR SIMULAÇÃO',
                            layout,
                            finalize=True,
                            resizable=True,
                            font=font1,
                            location=(100, 100),
                            element_justification="left")
        #Extrair dados da tela
        self.button, self.values =  _VARS['window'].Read()
        
    
        drawChart()

    def Iniciar(self):
        while True:
            self.button, self.values =  _VARS['window'].Read()
            
            if self.button == 'Simular':
                hist = self.values['sliderHist']
                energy = self.values['sliderEnergy']
                thick = self.values['sliderThick']
            
                kpar = dict(
                    electron = self.values['electron'],
                    photon = self.values['photon'],
                    positron = self.values['positron'],
                )
                
                material = dict(
                    PMMA=self.values['PMMA'],
                    adipose = self.values['adipose'],
                    water = self.values['agua'],
                    muscle = self.values['muscle'],
                    bone = self.values['bone'],
                    lung = self.values['lung'],
                    soft = self.values['soft'])
                
                for i in material:
                    if material[i]:
                        break
            
                k = 0
                for j in (kpar):
                    if kpar[j]:
                        break
                    else:
                        k+=1
                #configurando o arquivo penEasy.in
                #parametros:   filename, hist, update, new_z, energy, material, radius_x, name_geo,particle type, espessura cilindro
                set_in.set_in('run/penEasy.in', hist*1e3, 10, 100, energy*1e3, i, 5, 'cylinder.geo',k+1,thick)
                #print(k+1)
                #configurando o arquivo de geometria
                create_geometry_file('run/cylinder.geo',thick)
            
                print('INICIANDO SIMULAÇÃO')
                #rodar a simulação
                run.run(hist*1e3)
                
                #atualizar gráfico de resposta
                updateChart()
                
                #arquivo de saída
                #parametros: hist, energy, material, particle type, espessura cilindro:
                get_out(hist*1e3, energy, i,k+1,thick,initial_dir)
                os.chdir(initial_dir)
                
                #arquivo de saída
                #parametros: hist, energy, material, particle type, espessura cilindro:
                
                #graph.graph_SDD()
                #time.sleep(2)
        
                 
            elif self.button == 'Fechar' or  self.button == None or self.button ==sg.WIN_CLOSED:
                break

          
        
tela = TelaPython()
tela.Iniciar()
