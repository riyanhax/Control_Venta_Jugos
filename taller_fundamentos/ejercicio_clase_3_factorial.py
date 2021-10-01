''' El factorion es un numero natural que es igual a la suma de los factoriales de los digitos que lo componen
 Ejemplo 145   1!+4!+5! =145

Elaborar las siguientes funciones
 Funcion Factorial    parametro numero
Funcion Factorion     Parametro numero
 si el numero es factorion retorna 1
 si el numero no  es factorion retorna 0

Funcion Principal
'''
def factoril(num):
    fac1 = 1
    i = 1
    while i <= num:
        fac1 = fac1 * i
        i = i +1
    return fac1
def factorion(num):
    aux = num
    sum = 0
    while num > 0:
        quita = num % 10
        num //= 10
        sum = sum + factoril(quita)
    if sum == aux:
        return 'Si'
    else:
        return 'No'
v1 = int(input(f'Digite el numero --> '))
a = factorion(v1)
print(f'El numero "{a}" es factorion.')