def ordenamiento(lista, lista2, tam):
    for i in range(1, tam):
        for j in range(0, tam - i):
            if (lista[j] < lista[j + 1]):
                k = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = k

                k = lista2[j + 1]
                lista2[j + 1] = lista2[j]
                lista2[j] = k

def imprimeLista(lista1, lista2, tam):
    print("V1    V2")
    for i in range(0, tam):
        print(lista1[i],"<-->",lista2[i])

def leeLista(can, vec):
    lista = []
    for i in range(0, can):
        lista.append(int(input(f"vector {vec} Ingrese numero %d : " % (i+1))))
    return lista

can = int(input("Cantidad de numeros a ingresar: "))
print("\nLista v1\n")
v1 = leeLista(can, 'V1')
print("\nLista v2\n")
v2 = leeLista(can, 'V2')
ordenamiento(v1, v2, can)
imprimeLista(v1, v2, can)