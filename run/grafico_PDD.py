import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('tallySpatialDoseDistrib-3D.dat',delimiter='\s+',skiprows=14)
dose = df.iloc[:199,9].values
dose = dose.astype('float')

err = df.iloc[:199,10].values
err = err.astype('float')
#print(dose)

plt.errorbar(range(len(dose)), dose, yerr=err)
plt.yscale('log')
plt.show()
