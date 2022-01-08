'''
get_out.py       
Subrotina para obter os resultados finais da simulação

                Autor: Hitalo Rodrigues Mendes
                (hitalo.rm@gmail.com)
                
                Data: 2021/09/21
'''

import pandas as pd

def open_SDD(filename):
    col = ['xBinIndex','xLow(cm)','xMiddle(cm)','yBinIndex','yLow(cm)','yMiddle(cm)','zBinIndex',
               'zLow(cm)','zMiddle(cm)','dose','+-2sigma']

    df = pd.read_csv(filename,names = col, skiprows = 14, delimiter = '\s+')
    
    for i in range(len(df)):
      if df['xBinIndex'][i] == '#':
        break
    

    df = df.iloc[:i]
    
    return df

def open_edp():
    col = ['Material','Energy','+-2sigma']
    df = pd.read_csv('tallyEnergyDeposition.dat', names = col, skiprows = 5, delimiter = '\s+')
    for i in range(len(df)):
      if df['Material'][i] == '#':
        break
    

    df = df.iloc[:i]
    
    return df


def export_sdd(hist, energy, material, p_type, thick):
    type = ['Elétron','Fóton','Pósitron']
    sdd = open_SDD('run/tallySpatialDoseDistrib-3D.dat')
    sdd = sdd[['zMiddle(cm)','dose','+-2sigma']]
    sdd['zMiddle(cm)'] = pd.to_numeric(sdd['zMiddle(cm)'])
    sdd['dose'] = pd.to_numeric(sdd['dose'])
    
    sdd = sdd.rename(columns={'zMiddle(cm)': 'Profundidade(cm)',
                              'dose': 'Dose (eV/g)',
                             '+-2sigma': 'Incerteza'})
    

    sdd.to_csv('resultados/hist='+str("{0:.1e}".format(hist))+ '_'+ str(int(energy))+'keV_'+type[p_type-1] + '_' + material + '_thick=' + str(thick) +'cm.csv')    
    
