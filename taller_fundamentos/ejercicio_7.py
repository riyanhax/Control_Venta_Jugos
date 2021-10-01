'''7.Hacer un programa en python para capturar por teclado un número N (de cualquier cantidad de cifras), descomponerlo en sus
        dígitos y calcular: La sumatoria de sus cifras pares y La sumatoria de las cifras impares
        Ejemplo:
        N es 1275
        Sumatoria de dígitos pares 2 porque el único dígito par es 2
        Sumatoria impares 13 porque los dígitos impares son 1 7 y 5
'''
num = int(input("Ingrese un número enteros : "))   # 123
sumpar = 0
sumimp = 0
try:
     while num > 0:
        quita = num % 10
        num //= 10
        if quita % 2 == 0:
            sumpar = sumpar + quita
        else:
            sumimp = sumimp + quita
except ValueError:
    print("Ese número no es valido. Inténtalo de nevo !")
print('la suma de los pares es --> ',sumpar)
print('la suma de los impares es --> ',sumimp)