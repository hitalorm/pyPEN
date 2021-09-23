'''
graph.py         

Subrotina para plotar gráfico de dose em profundidade

                Autor: Hitalo Rodrigues Mendes 
                        (hitalo.rm@gmail.com)

                Data: 2021/09/21
'''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import get_out
import matplotlib

def graph_SDD():
    df = get_out.open_SDD()
    data = df[['zLow(cm)','zMiddle(cm)','dose','+-2sigma']].values
    data = data.astype('float')
    data = data.transpose()
    
    data[2:4] = data[2:4]/np.max(data[2])
    plt.cla()
    plt.clf()
    
    matplotlib.rcParams.update({'font.size': 15})
    plt.title('Dose Depositada em Profundidade')
    plt.errorbar(data[0],data[2], yerr = data[3]/2, fmt = 'o')
    plt.xlabel("Profundidade(cm)")
    plt.ylabel('Dose Relativa (%)')
    plt.step(data[1],data[2])
    #plt.show()

def blanck():
    plt.plot()
#print(open_edp())
