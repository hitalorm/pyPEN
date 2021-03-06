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
import interface_dose as d
import interface_track as t
import set_in
from create_geo import create_geometry_file
import run_simulation as run
import graph
from os import getcwd, chdir, remove
from get_out import export_sdd
from change_density import change_density
import webbrowser
import os



_VARS = {'window':False,
         'fig_agg': False,
         'pltFig': False}

font = ("Arial, 25")
font1 = ("Arial, 14")
font2 = ("Arial, 12")
font3 = ("Arial, 10")
initial_dir = getcwd()

track = False
dose = False
url = 'https://www.oecd-nea.org/jcms/pl_19590/penelope-2014-a-code-system-for-monte-carlo-simulation-of-electron-and-photon-transport?details=true' 

url1 = 'https://inte.upc.edu/en/shared/downloads/peneasy'

def win_main():
    #Layout

    layout = [
        [sg.Text('',font = font)],
        [sg.Text('Programa para simulação Monte Carlo\n usando o código PENELOPE versão 2014 \ncom a extensão penEasy versão 2015', font=font, justification='center')],
        [sg.Text('',font = font1)],
        [sg.Text('Hitalo Rodrigues Mendes',font = font1)],
        [sg.Text('Grupo de Física Radiológica Médica',font = font1)],
        [sg.Text('Instituto de Física Gleb Wataghin',font = font1)],
        [sg.Text('Universidade Estadual de Campinas',font = font1)],


        [sg.Text('',font = font)],
        [sg.Text('Manual PENOLPE 2014',
                 enable_events=True,text_color='blue',
                 key='URL', font=("Arial", 16,'underline'))],
        
        [sg.Text('penEasy 2015',
                 enable_events=True,text_color='blue',
                 key='URL1', font=("Arial", 16,'underline'))],
        
        [sg.Text('',font = font3)],
        [sg.Text('Tipo  de simulação',font = font)],
        [sg.Text('',font = font3)],

        [sg.Button('Deposição de dose', font=font1),
         sg.Button('Tracking de partículas', font=font1)]
    ]


    #Janela
    return sg.Window('CONFIGURAR SIMULAÇÃO',
                        layout,
                        finalize=True,
                        resizable=True,
                        font=font1,
                        location=(100, 100),
                        element_justification="center")
    #Extrair dados da tela
    #button, values =  _VARS['window'].Read()

window1, window2 = win_main(), None 

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        if window == window2:       # if closing win 2, mark as closed
            window2 = None
        elif window == window1:     # if closing win 1, exit program
            break

    elif event == 'URL':
        webbrowser.open(url)
    
    elif event=='URL1':
        webbrowser.open(url1)
    
    elif event == 'Tracking de partículas' and not window2:
        window2 = t.win_track()
        first = True
        track = True
        dose = False
        
    elif event == 'Deposição de dose' and not window2:
        window2 = d.win_dose()
        first = True
        dose = True
        track = False
        #_VARS['fig_agg'] = d.drawChart(window2['figCanvas'].TKCanvas, _VARS['pltFig'])
        
    elif event == 'Salvar Imagem':
        MYDIR = ("resultados")
        CHECK_FOLDER = os.path.isdir(MYDIR)

        if not CHECK_FOLDER:
            os.makedirs(MYDIR)

        if not _VARS['pltFig']:
            print('NENHUMA IMAGEM A SER SALVA')
        elif _VARS['pltFig']:
            if dose:
                _VARS['pltFig'].savefig('resultados/dose_profundidade-hist='+str("{0:.1e}".format(hist*1e5)) + '_' + str(int(energy))+'keV_'+i + '_' + j+'_thick='+ str(thick)+'cm.png')

            elif track:
                _VARS['pltFig'].savefig('resultados/track-hist='+str(int(hist)) + '_' + 
                                        str(int(energy))+'keV_'+i + '_' + j+'_thick='+ str(thick/10)+'cm_densidade=' + str(dens) + '.png')
    
            print('IMAGEM SALVA COM SUCESSO')
        
    elif event == 'Exportar gráfico como csv':
        MYDIR = ("resultados")
        CHECK_FOLDER = os.path.isdir(MYDIR)

        if not CHECK_FOLDER:
            os.makedirs(MYDIR)

        if not _VARS['pltFig']:
            print('NENHUM RESULTADO')
        elif _VARS['pltFig']:
            export_sdd(hist*1e5, energy, i,k+1,thick)
            print('DADOS EXPORTADOS COM SUCESSO')

    elif event == 'Simular':
        hist = values['sliderHist']
        energy = values['sliderEnergy']
        thick = values['sliderThick']
        
        kpar = dict(
            electron = values['electron'],
            photon = values['photon'],
            positron = values['positron'],
        )
        if dose:
            material = dict(
                PMMA=values['PMMA'],
                adipose = values['adipose'],
                water = values['agua'],
                muscle = values['muscle'],
                bone = values['bone'],
                lung = values['lung'],
                soft = values['soft'])
        elif track:
            material = dict(
                H=values['H'],
                C=values['C'],
                N=values['N'],
                O=values['O'],
                Al=values['Al'],
                Ag=values['Ag'],
                Cu=values['Cu'],
                Mo=values['Mo'],
                Pb=values['Pb'],
                W=values['W'],
                PMMA_1=values['PMMA'],
                adipose_1 = values['adipose'],
                water_1 = values['agua'],
                muscle_1 = values['muscle'],
                bone_1 = values['bone'],
                lung_1 = values['lung'],
                soft_1 = values['soft'])
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
        if dose:
            set_in.set_in('run/penEasy.in', hist*1e5, 3, 100, energy*1e3, i, 5, 'box.geo',k+1,thick, dose, track)
            create_geometry_file('run/box.geo',thick)

        elif track:
            dens = values['sliderDens']

            set_in.set_in('run/penEasy.in', hist, 10, 100, energy*1e3, i, 5, 'box.geo',k+1,thick/10, dose, track)
        #configurando o arquivo de geometria
            create_geometry_file('run/box.geo',thick/10)
            change_density('run/mat/'+i+'.mat',dens)
        print('INICIANDO SIMULAÇÃO')
        run.run(hist*1e5)

        #atualizar gráfico de resposta
        if dose:
            _VARS['fig_agg'], _VARS['pltFig'], first = d.drawChart(window2['figCanvas'].TKCanvas,
                                              _VARS['pltFig'],
                                              _VARS['fig_agg'],
                                              first)
        elif track:
            _VARS['fig_agg'], _VARS['pltFig'], first = t.drawChart(window2['figCanvas'].TKCanvas,
                                              _VARS['pltFig'],
                                              _VARS['fig_agg'],
                                              first)
        #arquivo de saída
        #parametros: hist, energy, material, particle type, espessura cilindro:
        #get_out(hist*1e3, energy, i,k+1,thick,initial_dir)
        try:
            remove('tallyParticleTrackStructure.dat')
        except OSError:
            pass

        chdir(initial_dir)


window.close()
