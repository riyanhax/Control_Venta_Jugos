'''Hacer un programa en python utilizando funciones que lea un número entero positivo de cualquier cantidad de dígitos (cifras), que
averigüe e imprima lo siguiente: si la cantidad de cifras es impar averiguar si el número es capicúa (Ej:585,25352) y el si la
cantidad de cifras es par, averiguar si el número es múltiplo de 4 y termina en 8 (Ej:28).
NOTA: Debe tener las siguientes funciones:
 principal.
 Una función que reciba el número leído y devuelva 1 (UNO) si la cantidad de cifras es impar y devuelva 0 (CERO) si la
cantidad de cifras es par.
 Una función que reciba el número cuya cantidad de dígitos sea impar y que devuelva 1 (UNO) Si el número es capicúa
(Ej:585,25352) y devuelva 0 (CERO) si el número NO es capicúa. (Ej:485,35352).
 Una función que reciba el número cuya cantidad de dígitos sea par y que calcule e imprima si el número es múltiplo de 4 y
termina en 8. (Ej:28). '''

def cifras(x):
    i = 0
    while x > 0:
        x = x // 10
        i += 1
    if i % 2 == 0:
        val = 0
    else:
        val = 1
    return val
def capicua(y):
    y1 = y
    cont = 0
    while y1 > 0:
        quita = y1 % 10
        cont = (cont * 10 ) + quita
        y1 //= 10
    if cont == y:
        return 1
    else:
        return 0
def mult(num):
    quita = num % 10
    if num % 4 == 0 and quita == 8:
        print(f' El numero es multiplo de 4 y termina en 8')
    else:
        print(f'El numero no el multiplo de 4')
num = int(input(f'Ingrese el numero --> '))
v1 = cifras(num)
if  v1 == 1:
    y = capicua(num)
    if y == 1:
        print(f'El numero si es capicua ')
    else:
        print(f'El numero no es capicua ')
else:
    if v1 == 0:
        mult(num)
