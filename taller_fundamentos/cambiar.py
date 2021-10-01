'''1. Dado un numero de 3 cifras totalmente diferentes hallar el número mayor que se forma, el número menor que se forma
 Ejemplo: 174 Mayor=741 Menor= 147'''

import numpy as np
def mostrar():
    cont1 = 0
    most = ordenar(a)
    if most == -1:
        print('Los digitos del numero son todos iguales')
    else:
        print(f'el número mayor que se forma es --> ', most)
        while most > 0:
            quita = most % 10
            cont1 = (cont1 * 10) + quita
            most //= 10
        print(f'el número nemor que se forma es --> ', cont1)
def ordenar(x):
    i = 0
    cont = 0
    if ((x[i] > x[i+1]) and (x[i] > x[i+2])):
        if (x[i+1] > x[i+2]):
            cont = (cont * 10) + x[i]
            cont = (cont * 10) + x[i+1]
            cont = (cont * 10) + x[i+2]
        else:
            cont = (cont * 10) + x[i]
            cont = (cont * 10) + x[i+2]
            cont = (cont * 10) + x[i+1]
    elif ((x[i+1] > x[i]) and (x[i+1] > x[i+2])):
        if (x[i] > x[i+2]):
            cont = (cont * 10) + x[i + 1]
            cont = (cont * 10) + x[i]
            cont = (cont * 10) + x[i+2]
        else:
            cont = (cont * 10) + x[i + 1]
            cont = (cont * 10) + x[i + 2]
            cont = (cont * 10) + x[i]
    elif ((x[i+2] > x[i]) and (x[i+2] > x[i+1])):
        if (x[i] > x[i+1]):
            cont = (cont * 10) + x[i+2]
            cont = (cont * 10) + x[i]
            cont = (cont * 10) + x[i+1]
        else:
            cont = (cont * 10) + x[i + 2]
            cont = (cont * 10) + x[i + 1]
            cont = (cont * 10) + x[i]
    else:
        cont = -1
    return cont
v1 = int(input("Ingrese un número de 3 digito enteros : "))
a = np.lista = []
try:
    num = int(v1)
    while num > 0:
        quita = num % 10
        a.append(quita)
        num //= 10
except ValueError:
    print("Ese número no es valido. Inténtalo de nevo !")
mostrar()