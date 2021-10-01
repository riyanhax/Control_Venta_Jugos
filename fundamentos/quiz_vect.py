'''
Realizar las siguientes funcione s
Llenar: Vector random números entre 0 200
Factoriones= Vector de factoriones un número factorion Ejemplo = 1!+4!+5! = 145 factorion
Narcisista= Vector narcisista un número narcisista es aquel que es igual a la suma de sus
dígitos elevados a la potencia de su número Ejemplo= 1^3+5^3^+3^3=153 <<<<----------------------------
Capicua= Vector capicua un número capicua es aquel que al leerlo de izquierda a derecha o
derecha a izquierda es el mismo número capicúa
Invertido= vector invertido
Espejo=vector espejo Ejemplo: 123 espejo 321 Ejemplo 14 Espejo 41
Suma pares= Vector con los valores pares
Suma impares= Vector con los valores impares
Números Positivos= Vector con los valores Positivo
10. Genere una vector para mejorar el ejercicio
'''

import random
def menu():
    print("\t\t|__________________________|")
    print("\t\t|   VALORES DE UN VECTOR   |")
    print("\t\t|--------------------------|")
    print("\t\t|    1. Factoriones        |")
    print("\t\t|    2. Narcisistas        |")
    print("\t\t|    3. Capicuas           |")
    print("\t\t|    4. Invertido          |")
    print("\t\t|    5. Espejo             |")
    print("\t\t|    6. Suma Pares         |")
    print("\t\t|    7. Suma Impares       |")
    print("\t\t|    8. Suma de todos      |")
    print("\t\t|    9. Número Positivos   |")
    print("\t\t|    10. XXXXXXXXXX        |")
    print("\t\t|    11. Fin del programa  |")
    print("\t\t|--------------------------|")
    op = int(input("Cual es su opcion? --> "))
    while (op < 1 or op > 11):
        op = int(input("ERROR:Valor fuera de rango\nCual es su opcion?"))
    return op
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
def capicua(num):
    num1 = num
    cont = 0
    while num1 > 0:
        quita = num1 % 10
        cont = (cont * 10 ) + quita
        num1 //= 10
    if cont == num:
        return 1
def invertir(vec1, x):
    vecinv = []
    x -= 1
    while True:
        vecinv.append(vec1[x])
        x -= 1
        if x < 0:
            break
    return vecinv
def inver_ind(vec1, x):
    i = 0
    cont = 0
    x -= 1
    while x >= 0:
        while vec1[i] > 0:
            quita = vec1[i] % 10
            cont = (cont * 10) + quita
            vec1[i] //= 10
        vec1[i] = cont
        cont = 0
        i += 1
        x -= 1
    return vec1
def suma(vec1, x):
    sum = 0
    if x == 0:
        for i in range(0, len(vec1)):
            if vec1[i] % 2 == 0:
                sum += vec1[i]
        return sum
    elif x == 1:
        for i in range(0, len(vec1)):
            if vec1[i] % 2 != 0:
                sum += vec1[i]
        return sum
    elif x == 2:
        for i in range(0, len(vec1)):
                sum += vec1[i]
        return sum
def narcista(num):
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
op = menu()
if op >= 1 and op <= 10:
    pre0 = int(input("Cuando valores desea en el vector? --> "))
    i = 1
    vec1 = []
    vec2 = []
    while i <= pre0:
        vec1.append(random.randint(0, 200))
        i += 1
    print(f'El vector es --> {vec1}')
    if op == 1:
        # vec1 = [123,145,452]
        for i in range(0, len(vec1)):
            res = factorion(vec1[i])
            if res == 'Si':
                vec2.append(vec1[i])
        if vec2 == []:
            print(f'En el vector no hay factoriones.')
        else:
            print(f'Los factoriones son --> {vec2}')
    elif op == 2:
        #vec1 = [123,153,452]
        for i in range(0, len(vec1)):
            res = narcista(vec1[i])
            #print('-->',pre0)
            if res == 1:
                vec2.append(vec1[i])
        if vec2 == []:
            print(f'En el vector no hay numeros narcistas.')
        else:
            print(f'Los numeros narcistas son --> {vec2}')
    elif op == 3:
        # vec1 = [11,145,22]
        for i in range(0, len(vec1)):
            res = capicua(vec1[i])
            # print('-->',res)
            if res == 1:
                vec2.append(vec1[i])
                # print('-->', vec2)
        if vec2 == []:
            print(f'En el vector no hay Capicuas.')
        else:
            print(f'Los Capicuas son --> {vec2}')
    elif op == 4:
        vec2 = invertir(vec1, pre0)
        print(f'El vector invertido es --> {vec2}')
    elif op == 5:
        vec2 = inver_ind(vec1, pre0)
        print(f'El vector espejo es --> {vec2}')
    elif op == 6:
        x = 0
        sumpar = suma(vec1, x)
        print(f'La suma de los pares del vector es --> {sumpar}')
    elif op == 7:
        x = 1
        sumimp = suma(vec1, x)
        print(f'La suma de los impares del vector es --> {sumimp}')
    elif op == 8:
        x = 2
        sumtod = suma(vec1, x)
        print(f'La suma de todos los datos del vector es --> {sumtod}')
    elif op == 9:
        #vec1 = [123,-145,452]
        for i in range(0, len(vec1)):
            #res = factorion(vec1[i])
            if vec1[i] < 0:
                vec2.append(vec1[i])
        if vec2 == []:
            print(f'En el vector no hay numeros negativos.')
        else:
            print(f'Los numeros negativos son --> {vec2}')
    elif op == 10:
        print(f'Lo siento por el momento no tenemos funciones en esta opción\nPor favor intenten con otra opción :)')
    op = menu()
elif op == 11:
    print(f'Gracias que tenga un buen reso de dia :) 👍')
