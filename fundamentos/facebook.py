''':cvardef narcista(num):
    aux0 = num
    aux1 = num
    sum = 0
    i = 0
    while aux0 > 0:#3
        aux0 % 10
        aux0 //= 10
        i += 1
    while num > 0:
        quita = num % 10
        num //= 10
        sum += quita**i
    if sum == aux1:
        return 1
num = int(input(f'Cual es el numero: '))
res = narcista(num)
if res == 1:
    print(f'El numero: {num} si es narcista.')
else:
    print(f'El numero: {num} no es narcista.')
'''
def sumpares(num):
    sum = 0
    while num > 0:
        quita = num % 10
        num //= 10
        if quita % 2 == 0:
            sum += quita
    return sum
num = int(input(f'Cual es el numero: '))
res = sumpares(num)
print(f'La suma de los pares es = {res}')