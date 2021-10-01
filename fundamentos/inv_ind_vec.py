import numpy as np
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
def mostra():
    newvec = inver_ind(vec, i)
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