'''
Un supermercado vende n productos (n dado por teclado), cada producto
tiene su código y precio, realizar:
-Llenar: Guarda la información de los productos, validar el código de dos
dígitos y no se repita. val valor unitario random este entre 1000 y 15000
-Ordenar:Ordena los vectores de código y valor unitario en forma
 descendente tomando como referencia los códigos
-Valor a pagar: Calcula el valor que debe pagar un cliente, conociendo
 el código, la cantidad de artículos, un cliente lleva una
 cantidad indeterminada de artículos, termina cuando el
 cliente de un código 0 para el articulo
- mostrar la información en forma de columna
- Genere las funciones necesarias para solucionar el ejercicio y mejorar
el ejercicio
'''
from random import randint
def mostrar(cod, val, canti, sum):
    print("\n|============================|")
    print("| DATOS DE LAS PERSONAS      |")
    print("|============================|")
    print("| No |   Codigo   |   Valor  |")
    for i in range(0, canti):
        men = "| " + '{:>2s}'.format(str(i + 1)) + " | "
        men = men + '{:>11s}'.format(str(cod[i])) + "| "
        men = men + '{:>8s}'.format(str(val[i])) + " | "
        print("|----+------------+----------|")
        print(men)
    print("|----+------------+----------|")
    print("|           Total |  ",sum," |")
    print("|----------------------------|")
def ordenar(cod,valor,n):
    for i in range(0,n):
        for j in range(i+1,n):
            if(valor[i]<valor[j]):
                aux=valor[i]
                valor[i]=valor[j]
                valor[j]=aux

                aux=cod[i]
                cod[i]=cod[j]
                cod[j]=aux
def buscar(dato, vect):
    for i in range(0, len(vect)-1):
        if dato == vect[i]:
            return 1
def validar(dato, i):
    while dato < 10:
        print('Los codigos deben ser de 2 cifras.')
        dato = int(input(f'Escriba el codigo No.{i + 1} -->'))
    return 1, dato
def llenar(canti):
    cod = []
    val = []
    for i in range(0, canti):
        cod.append(int(input(f'1-Escriba el codigo No.{i+1} -->')))
        a, b = validar(cod[i], i)
        if a == 1:
            cod.pop(i)
            cod.append(b)
        if i >= 1:
            while True:
                res = buscar(cod[i], cod)
                if res == 1:
                    print(f'El codigo {cod[i]} ya se encuentra.')
                    cod.pop(i)
                    cod.append(int(input(f'Escriba el codigo No.{i + 1} -->')))
                else:
                    break
        val.append(randint(1000, 15000))
        print(cod)
    return cod, val
def total(y):
    sum = 0
    for i in range(0, len(y)):
        sum += y[i]
    return sum
cuanto = int(input(f'Cuantos articulos desea -->'))
x, y = llenar(cuanto)
ordenar(x, y, cuanto)
suma = total(y)
mostrar(x, y, cuanto, suma)
