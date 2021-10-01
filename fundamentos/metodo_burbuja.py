def ordenamientoBurbuja(lista, tam):
    for i in range(1, tam):
        for j in range(0, tam - i):
            if (lista[j] > lista[j + 1]):
                k = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = k
    '''for i in range(0, n).
            for j in range(i+1, n):
                if lista[i] > lista[j]
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux'''
def selectionsort(lista,tam):
    for i in range(0,tam-1):
        min=i
        for j in range(i+1,tam):
            if lista[min] > lista[j]:
                min=j
        aux=lista[min]
        lista[min]=lista[i]
        lista[i]=aux
def insercionDirecta(lista,tam):
    for i in range(1,tam):
        v=lista[i]
        j=i-1
        while j >= 0 and lista[j] > v:
            lista[j+1] = lista[j]
            j=j-1
        lista[j+1]=v
def imprimeLista(lista, tam):
    for i in range(0, tam):
        print(lista[i],end='')
    print('')
def leeLista():
    lista = []
    cn = int(input("Cantidad de numeros a ingresar: "))
    for i in range(0, cn):
        lista.append(int(input("Ingrese numero %d : " % i)))
    return lista
A = leeLista()
ordenamientoBurbuja(A, len(A))
imprimeLista(A, len(A))
selectionsort(A, len(A))
print('--')
imprimeLista(A, len(A))
insercionDirecta(A, len(A))
print('--')
imprimeLista(A, len(A))