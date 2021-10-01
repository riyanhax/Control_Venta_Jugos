'''Desarrolle un programa con dos funciones, una función que reciba en sus argumentos 10 valores enteros y
muestre por pantalla cuantos son pares y otra función que reciba en sus argumentos 10 valores enteros y
muestre por pantalla cuantos son impares
'''
import numpy as np
def pares(par):
    j = 0
    b = np.arra = []
    while True:
        par[j]
        if par[j] % 2 == 0:
            b.append(par[j])
        j = j + 1
        if j == 10: break
    return b
def impares(imp):
    z = 0
    c = np.arra = []
    while True:
        imp[z]
        if imp[z] % 2 != 0:
            c.append(imp[z])
        z = z + 1
        if z == 10: break
    return c
def mostrar():
    pare = pares(a)
    impa = impares(a)
    print(f'los numeros Pares son ----> {pare}\n'
          f'los numeros Impares son --> {impa}')
a = np.lista = []
i = 0
while True:
    a.append(int(input(f'el numero en la posición {i+1} es --> ')))
    i = i + 1
    print(f'la lista va en = ',a)
    if i == 10: break
mostrar()