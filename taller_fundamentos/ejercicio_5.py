'''5. Se dice que un número N es número perfecto si la suma de sus divisores propios es igual a él mismo.
        El conjunto de divisores propios de un número N, está formado por todos sus divisores, Excepto él mismo. Ej., los divisores
        propios de 9 son 1 y 3. Los divisores propios de 6 son 1,2 y 3.
        Por lo tanto 6 es un número perfecto porque la suma de sus divisores propios 1 + 2 +3 es igual a él mismo (a 6). Y 9 no es perfecto
'''

def numperfec(num):
    cont = 0
    i = 1
    '''    for i in range(1,num):
                if num % i == 0:
                    cont += i
    '''
    while True:
        if num % i == 0:
            cont += i
            i += 1
        else:
            break
    if cont == num:
        r = 'Si'
    else:
        r = 'No'
    return r
v1 = int(input(f'Digite un numero --> '))
res = numperfec(v1)
print(f'El numero ({v1}) "{res}" es un numero perfecto :)')