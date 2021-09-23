'''
run_simulation.py
Subrotina para rodar a simulação automatizada

                Autor: Hitalo Rodrigues Mendes
                (hitalo.rm@gmail.com)
                
                Data: 2021/09/21
'''

import os
import platform
import subprocess
import time


def run(hist):
    #detect OS
    OS = platform.system()
    
    os.chdir('run')
    if OS =='Windows':
        p = subprocess.Popen('penEasy.exe<penEasy.in>res.out', shell=True)
    else:
        directory = os.getcwd()
        p = subprocess.Popen('./penEasy.x<penEasy.in>res.out', cwd = directory, shell=True)
    
    time.sleep(15)
    
    while p.poll() is None:
        file = open('res.out')
        lines = file.readlines()
        if lines[-1] == 'Have a nice day.\n':
            Finished=True
            print('SIMULAÇÃO ACABOU\n')
        else:
            file2 = open('tallyEnergyDeposition.dat')
            lines2 = file2.readlines()
            print('Simulação '+ str("{0:.1f}".format(int(lines2[12][1:-2])*100/hist))+'% concluída')
        file.close()
        time.sleep(10)
        
    print('SIMULAÇÃO ACABOU\n')
    
