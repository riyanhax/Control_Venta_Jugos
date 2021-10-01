import numpy as np
def factorial(x):
    fac1 = 1
    i = 1
    while i <= (x):
        fac1 = fac1 * i
        i = i + 1
    return fac1
def fac_vec(vec1, x):
    vec2 = np.lista = []
    i = 0
    while i < x:
        vec2.append(factorial(vec1[i]))
        i += 1
    return vec2
def llenar(vec1, x):
    for i in range(0, x):
        vec1.append(int(input(f" Ingrese el {i} dato --> ")))
def mostar():
    a = fac_vec(vec1, x)
    print(f'el factorial del vector es --> {a}')
x = int(input(f'Cuantos valores desea ingrasar --> '))
vec1 = np.lista = []
llenar(vec1, x)
mostar()
