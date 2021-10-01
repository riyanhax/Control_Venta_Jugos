"""
Desarrollar un programa modular(con funciones) que
solicite un numero N de cualquier cantidad de digitos
y determine con funciones:
1) Cantidad de Digitos
2) Determinar si es Capicua ---> 12521  es Capicua
3) Formar un nuevo numero solo con los pares

Ejemplo
Si el numero ingresado es: 614413
Respuesta 1: tiene 6 digitos
Respuesta 2: No es Capicua
Respuesta 3: 446
"""
def candig (num):
    cont = 0
    aux = 0
    while num >= 1:
        quita = num % 10
        if quita % 2 == 0:
            aux = (aux * 10) + quita
        cont += 1
        num //= 10
    return cont, aux
def capicua(num):
    num1 = num
    cont = 0
    while num1 > 0:
        quita = num1 % 10
        cont = (cont * 10) + quita
        num1 //= 10
    if cont == num:
        return 1
num = int(input(f'Digite el numero --> '))
can, par = candig(num)
cap = capicua(num)
if cap == 1:
    cap = 'SI'
else:
    cap = 'NO'
print(f'El numero ingresado es --> {num} .\n'
      f'Respuesta 1 --> tiene {can} digitos.\n'
      f'Respuesta 2 --> {cap} es Capicua.\n'
      f'Respuesta 3 --> {par} nuemro formado con pares.')





