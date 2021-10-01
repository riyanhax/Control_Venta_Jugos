'''
Dado un número entero N por teclado, hacer un programa en C con funciones para que calcule calcular la siguiente expresión
R=(x/y)^z   (24/4)=6
donde X es la suma de los divisores pares de N; Y es la suma de los divisores impares de N y Z es el número de dígitos de
N.
Ejemplo: Si el número N es 12 los divisores pares de 12 son 2,4,6 y 12 por lo tanto X=24 y los divisores impares de 12 son 1 y 3
por lo tanto Y= 4. Además 12 tiene 2 cifras(Z=2), por lo tanto la expresión es igual a 6 36
es decir que el programa debe imprimir 36.
'''

def divisores(num):
    sumpar = 0
    sumimp = 0
    i = 1
    while i <= num:
        if num % i == 0 and i % 2 == 0:
            sumpar = sumpar + i
        elif num % i == 0 and i % 2 != 0:
            sumimp = sumimp + i
        i = i + 1
    return sumpar / sumimp
def digitos(num):
    cont = 0
    while num > 0:
        num = num // 10
        cont = cont + 1
    return cont
def poten(x, y):
    i = 1
    pot = 1
    while i <= y:
        pot = pot * x
        i += 1
    return pot
v1 = int(input(f'Digite el numero --> '))
a = poten(divisores(v1),digitos(v1))
print(f'El resultado es --> {a}')
