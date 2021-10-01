import numpy as np
def mostrar():
    rescon = concatenar(x, y)
    resint = intercalar(x, y, pres_0, pres_1)
    print(f'al concatenar los vectores = {rescon}')
    print(f'al intercalar los vectores = {resint}')
def concatenar(x, y):
    r0 = x + y
    return r0
def intercalar (x, y, z_1, z_2):
    i = 0
    j = 0
    r1 = np.lista = []
    if z_1 > z_2:
        res = z_1 - z_2
        men = z_2
        vec_1 = x
    else:
        res = z_2 - z_1
        men = z_1
        vec_1 = y
    while (i+1) <= men:
        r1.append(x[i])
        r1.append(y[i])
        i += 1
    while j <= res:
        vec_1.pop(0)
        j += 1
    r1 = r1 + vec_1
    return r1
x = np.lista = []
y = np.lista = []
v0 = str(input(f'Con cual lista desea empezar X o Y --> '))
pres_0 = 0
pres_1 = 0
while True:
    if v0 == 'x' or v0 == 'X':
        i = 1
        pre_0 = int(input(f'cuanos valores desea ingresar a la lista X = {x} --> '))
        while i <= pre_0:
            v1 = int(input(f'lista X = {x}, ingrese el valor que desea ingresar a la lista --> '))
            x.append(v1)
            i += 1
        v0 = 'y'
        pres_0 += pre_0
    if v0 == 'y' or v0 == 'Y':
        i = 1
        pre_1 = int(input(f'cuanos valores desea ingresar a la lista  Y = {y} --> '))
        while i <= pre_1:
            v1 = int(input(f'lista Y = {y}, ingrese el valor que desea ingresar a la lista --> '))
            y.append(v1)
            i += 1
        v0 = 'x'
        pres_1 += pre_1
    v2 = str(input(f'desea continuar llenando alguna lista s/n --> '))
    if v2 == 's' or v2 == 'S':
        v0 = str(input(f'Con cual lista desea cuntinuar X o Y --> '))
    elif v2 == 'n' or v2 == 'N':
        if x == [] or y == []:
            print(f'lo siento pero las lista X, Y no pueden estar vacias :(')
            v2 = 's'
        else: break
mostrar()