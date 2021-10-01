import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

classes = ['81-83','83-85','85-87','87-89','89-91',
            '91-93','93-95','95-97','97-99',]
classes = np.asarray(classes)

temperaturaRuptura = np.unique(classes)

frequencia = [6,7,17,30,43,28,22,13,3]
frequencia = np.asarray(frequencia)

somaFreq = sum(frequencia)

frequenciaRelativa = np.round(100*(frequencia/somaFreq),2)
print('Frequencia Relativa:')
print(frequenciaRelativa)

# Plotagem do histograma
plt.title('resistência à ruptura de barras cerâmicas tratadas')
plt.xlabel('Temperatura(C°)')
plt.ylabel('Frequencia Relativa')

plt.bar(temperaturaRuptura,frequenciaRelativa)
plt.show()
