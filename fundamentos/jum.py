'''
#1.

num_1 = int(input(f'Digite el valor en el que empieza: '))
num_2 = int(input(f'Digite el valor en el que termina: '))
sum = 0
for i in range(num_1, num_2 + 1):
    sum = sum + i
print(f'El promedio de los numeros de "{num_1}" asta el "{num_2}" es {sum/(num_2-(num_1-1))}')

#--------------------------------------------------------------------------------------------------------

#2.

num_1 = int(input(f'Digite el valor que este entre 100 y 999: '))
if num_1 >= 100 and num_1 <= 999:
    while True:
        x = ','
        if num_1 == 0:
            x = '.'
        print(num_1, end=f'{x}')
        num_1 = num_1 - 1
        if num_1 < 0:
            break
else:
    print('El numero no se encuentra dento de la condición.')

#-------------------------------------------------------------------------------------------------------

#3.

num_1 = int(input(f'Digite hasta cual tabla desea: '))
num_2 = int(input(f'Digite de cunatos valores: '))
for i in range(1, num_1 + 1):
    for j in range(1, num_2 + 1):
        print(i,'x',j,'=',(i*j))
    print('----------------')

#-------------------------------------------------------------------------------------------------------

#4

num_1 = int(input(f'Digite el numero que desea validar: '))
i = 1
cont = 0
while i <= num_1:
    if num_1 % i == 0:
        cont = cont + 1
    print('--',i)
    i = i + 1
if cont == 2:
    print(f'El numero "{num_1}" si es primo')
else:
    print(f'El numero "{num_1}" no es primo')

'''

