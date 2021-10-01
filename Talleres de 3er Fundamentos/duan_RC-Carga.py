import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

ver = plt.figure()
ax = ver.gca()

E = 5
C = 100 * 10**(-6)
R = 2000

t = np.linspace(0,1,1000)
T = R * C

q = C*E*(1-np.exp((-1/T)*t))
i = (E/R)*np.exp((-1/T)*t)

def Actualizar(cuen):
    ax.clear()
    ax.plot(t[:cuen],q[:cuen], label='Carga de capacitor')
    ax.plot(t[:cuen],i[:cuen],label='Corriente')
    plt.xlabel('Tiempo')
    plt.ylabel('Q, I')
    plt.title('Circuito RC')
    plt.legend()

ver_1 = FuncAnimation(ver,Actualizar)

plt.show()
