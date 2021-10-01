'''
Realizar un programa en python dado un vector definido v=[1,5,78,12,16,15,23,2]

Elaborar las siguientes funciones

•
•	Función primo: Recibe como parámetro el número y retorna 1 si el numero es primo o retorna 0 si no lo es.
•	Función primos: Recibe como parámetro el vector y revisa todos los valores y retorna la cantidad de números primos que existen
	Funcion Vprimos: Recibe como parametro el vector y n genera el vector de primos
•	Función principal: El vector definido y hace el llamado a las funciones y las impresiones
'''
import numpy as np
import random
def buscar(vec1):
    vec3 = np.lista = []
    for i in range(0, len(vec1)):
        x = primo(vec1[i])
        if x == 1:
            vec3.append(i)
    return vec3
def primo(num):
    j = 0
    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1
def primos(vec1):
    vec2 = np.lista = []
    cont = 0
    for i in range(0, len(vec1)):
        x = primo(vec1[i])
        if x == 1:
            vec2.append(vec1[i])
            cont += 1
    return vec2, cont
def mostrar():
    a, b = primos(vec1)
    c = buscar(vec1)
    print(f'La cantidad de numeros primos son --> "{b}"\n'
          f'Los numeros primos son --> "{a}"\n'
          f'y estan en los indices --> "{c}" del vector principal.')
pre = int(input(f'[1] llenar el vector\n'
                f'[2] el sistema genere un vector --> '))
vec1 = np.lista = []
if pre == 1:
    print(f'Digite los los valores, para salir ingrase (0)')
    i = 0
    while True:
        v1 = int(input(f'[{i}] valor --> '))
        vec1.append(v1)
        i += 1
        if v1 == 0:
            vec1.remove(0)
            break
elif pre == 2:
    pre1 = int(input(f'De cuantos valores -->'))
    i = 0
    while i <= pre1:
        vec1.append(random.randint(1, 100))
        i += 1
    print(f'El vector q el sistema genero es --> {vec1}')
mostrar()
