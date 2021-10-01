import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics

"""
temps = [84,49,61,40,83,67,45,66,70,
         69,80,58,68,60,67,72,73,70,
         57,63,70,78,52,67,53,67,75,
         61,70,81,76,79,75,76,58,31]   

"""

temps =[0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,0,1,0,1,0,1,1,0,0,1,0,1,0,0,1,1,1,0,0,1]

temps = np.unique(temps)

media = np.mean(temps)
print('Média:',media)

mediana = statistics.median(temps)
print("Mediana:",mediana)

desvioPadrao = np.std(temps)
print('Desvio Padrão:',desvioPadrao)

#Gráfico
plt.boxplot(x=temps)
plt.show()
