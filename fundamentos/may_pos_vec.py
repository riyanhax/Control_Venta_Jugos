import numpy as np

def mayor(vec1,n):
    j = 0
    pos = np.lista = []
    may=vec1[0]
    for i in range(0,n):
        if(vec1[i]>may):
            may=vec1[i]
            while j <= n:
                if may == vec1[j]:
                    pos.append(i)
    print(" el valor mayor es:",may," y esta en la posicion;",pos )
    return may, pos
def mostra():
    may, pos = mayor(vec, i)
    print(" el valor mayor es:",may, " y esta en la posicion;", pos)
i = 0
vec = np.lista = []
while True:
     vec.append(int(input(f'Digite el valor del indice --> {i} --->')))
     i += 1
     pre = str(input(f'Desea continuar s/n -->'))
     if pre == 'n' or pre == 'N':
        break
mostra()