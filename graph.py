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
from matplotlib import rcParams
from scipy.integrate import trapz


def graph_SDD():
    df = get_out.open_SDD()
    data = df[['zLow(cm)','zMiddle(cm)','dose','+-2sigma']].values
    data = data.astype('float')
    data = data.transpose()
    
    integra = np.sum(data[2]*0.1)/(data[0,-1]+0.1)
    
    plt.cla()
    plt.clf()
    
    
    rcParams.update({'font.size': 15})
    plt.subplots_adjust(left=0.15, bottom=.14, right=.98, top = 0.90,
                wspace=0.2, hspace=0.3)

    plt.title( 'Dose total = '+ str("{0:.2f}".format(integra)) + ' (eV/g/hist)')
    plt.errorbar(data[0],data[2], yerr = data[3]/2, fmt = 'o')
    plt.xlabel("Profundidade(cm)")
    plt.ylabel('Dose Depositada (eV/g/hist)')
    plt.step(data[1],data[2])
    #plt.show()

def blanck():
    plt.plot()


def graph_track():
    rcParams.update({'font.size': 13})

    col = ['kpar','body','mat','x','y','z','u','v','w','e','elost','wght','tallymode','ilb(5)']
    df = pd.read_csv('tallyParticleTrackStructure.dat', names = col, delimiter = '\s+', skiprows = 7)
    print(len(df))
    df = df[df['kpar'] != "#"]
    
    title = ['Elétron','Fóton','Pósitron']
    
    cor = ['red','blue','green']
    #fig,ax  = plt.subplots(1,3,figsize = [15,6])#figure()
    
    plt.subplots_adjust(left=0., bottom=0., right=.93, top = 1,
                wspace=0.25, hspace=0.35)

    plt.title('Tracking de Partículas')
    for i in range(3):
        
        ax = plt.subplot(1,3,i+1, projection='3d')
    
        sliced = df[df['kpar']==str(i+1)]
        sliced = sliced.values
        sliced = sliced.astype(float)

        
        ax.set_title(title[i])
        ax.plot(sliced[:,3],sliced[:,4],sliced[:,5], color = cor[i], linewidth = 0.5)
        ax.set_xlabel('x', fontsize = 18,labelpad=10)
        ax.set_ylabel('y', fontsize = 18,labelpad=10)
        ax.set_zlabel('z', fontsize = 18,labelpad=10)

