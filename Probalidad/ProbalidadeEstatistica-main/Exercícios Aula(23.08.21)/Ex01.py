import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
amostra =[  
    2, 1, 2, 4, 0, 1, 3, 2, 0, 5, 3, 3, 1, 3, 2, 4, 7, 0, 2, 3,
    0, 4, 2, 1, 3, 1, 1, 3, 4, 1, 2, 3, 2, 2, 8, 4, 5, 1, 3, 1,
    5, 0, 2, 3, 2, 1, 0, 6, 4, 2, 1, 6, 0, 3, 3, 3, 6, 1, 2, 3,
]
"""

amostra =[0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,0,1,0,1,0,1,1,0,0,1,0,1,0,0,1,1,1,0,0,1]
amostra = np.asarray(amostra)

eixoX, frequencia = np.unique(amostra,return_counts= True )

print('Valores:')
print(eixoX)  

print('Frequencia:')
print(frequencia)

print('Frequencia Relativa:')
frequenciaRelativa = np.round(100*frequencia/amostra.size,2)
print(frequenciaRelativa)

# plt.hist(amostra, bins=9)
plt.bar(eixoX, frequenciaRelativa)
# plt.show()