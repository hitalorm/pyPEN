'''
get_out.py       
Subrotina para obter os resultados finais da simulação

                Autor: Hitalo Rodrigues Mendes
                (hitalo.rm@gmail.com)
                
                Data: 2021/09/21
'''

import pandas as pd
import numpy as np
import os 

def open_SDD():
    col = ['xBinIndex','xLow(cm)','xMiddle(cm)','yBinIndex','yLow(cm)','yMiddle(cm)','zBinIndex',
               'zLow(cm)','zMiddle(cm)','dose','+-2sigma']

    df = pd.read_csv('tallySpatialDoseDistrib-3D.dat',names = col, skiprows = 14, delimiter = '\s+')
    
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

def create_resultado(initial_dir):
    df = pd.DataFrame()
    df.to_excel(initial_dir + "/resultados/output.xlsx",
             sheet_name='resultados', index=False)
    
    return df


def get_out(hist, energy, material, p_type, thick, initial_dir):
    
    data_exist = os.path.isfile(initial_dir + "/resultados/output.xlsx")
    if data_exist:
        df = pd.read_excel(open(initial_dir + "/resultados/output.xlsx", 'rb'),
              sheet_name='resultados')
    else:
        df = create_resultado(initial_dir)
    
    type = ['Elétron','Fóton','Pósitron']
    i = len(df)
    df.at[i,'Histórias'] = hist
    df.at[i,'Energia(keV)'] = energy
    df.at[i,'Material'] = material
    df.at[i,'Tipo de partícula'] = type[p_type-1]
    df.at[i,'Espessura cilindro (cm)'] = thick
    
    
    
    edp = open_edp()
    df.at[i,'Energia depositada (keV)'] = float(edp['Energy'][0])/1e3
    df.at[i,'Incerteza energia depositada (keV)'] = float(edp['+-2sigma'][0])/2e3
    
    
    
    sdd = open_SDD()
    sdd = sdd[['zMiddle(cm)','dose','+-2sigma']]
    sdd['zMiddle(cm)'] = pd.to_numeric(sdd['zMiddle(cm)'])
    sdd['dose'] = pd.to_numeric(sdd['dose'])
    
    sdd = sdd.rename(columns={'zMiddle(cm)': 'Profundidade(cm)',
                              'dose': 'Dose (eV/g)',
                             '+-2sigma': 'Incerteza'})
    

        
    a = []
    for j in range(i):
        b = pd.read_excel(open(initial_dir + "/resultados/output.xlsx",'rb'),
                  sheet_name='simula_'+str(j+1))# + str(j+1))
        a.append(b)

    filename = initial_dir + "/resultados/output.xlsx"
    
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    # Save the file
    
    
    df.to_excel(writer,
             sheet_name='resultados', index=False)
    
    sdd.to_excel(writer,
             sheet_name='simula_' + str(i+1), index=False)

    for j in range(len(a)):
        a[j].to_excel(writer,
             sheet_name='simula_' + str(j+1), index=False)

    writer.save()

#df = pd.read_excel(open("resultados/output.xlsx",'rb'),
#                  sheet_name='1')# + str(j+1))
#print(df)

#get_out(100000.0, 10.0, 'water', 2 ,1.0, '/home/hmendes/Dropbox/Doutorado/Interface Gráfica')
