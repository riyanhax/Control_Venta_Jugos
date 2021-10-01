import numpy as np
def invertir(vec1, x):
    vecinv = np.lista = []
    x -= 1
    while True:
        vecinv.append(vec1[x])
        x -= 1
        if x < 0:
            break
    return vecinv
def mostra():
    newvec = invertir(vec, i)
    print(f'El nuevo vector invertido es --> {newvec}')
i = 0
vec = np.lista = []
while True:
     vec.append(int(input(f'Digite el valor del indice --> {i} --->')))
     i += 1
     pre = str(input(f'Desea continuar s/n -->'))
     if pre == 'n' or pre == 'N':
        break
mostra()