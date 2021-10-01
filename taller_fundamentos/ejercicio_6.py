'''6. Dado un número natural n encuentre su raíz digital.
        Raíz digital de un natural: se calcula el natural m sumando los dígitos que componen a n. El proceso se repite sobre el nuevo
        número hasta que el resultado sea de un dígito.
        Ejemplo: 347 3 + 4 + 7 = 14 1 + 4 = 5 RD(347) = 5
'''

numero = int(input("Ingrese un número enteros : "))
sum = 0
num = int(numero)
while num > 0:
    quita = num % 10
    num //= 10
    sum = sum + quita
    if num == 0:
        if sum < 10:
            break
        else:
            num += sum
            sum = sum * 0
print(f'La raiz digital de ({numero}) es --> ',sum)