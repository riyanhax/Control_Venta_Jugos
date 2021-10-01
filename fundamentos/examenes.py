"""
def examenes(dato):
    #cop = dato[0][0]
    concop = 0
    for i in range(0,len(dato[0])):
        for k in range(0,len(dato[0])):
            print(k)


dato = [[1,2,1,2,1],1]
examenes(dato)


def contarElementosLista(lista):


    return {i: lista.count(i) for i in lista}


lista = [1,2,3,2,1,4,2,5,2,4,2,3]
resultado = contarElementosLista(lista)  # {'a': 3, 'b': 1, 'c': 3}
print(resultado)
maximo = max(resultado, key=resultado.get)
print(resultado[2])
print("El valor mas repetido es el ", maximo, " con ", resultado[maximo], " veces")"""

def ordenamientoBurbuja(lista, tam):
    for i in range(1, tam):
        for j in range(0, tam - i):
            if (lista[j] > lista[j + 1]):
                k = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = k

def SinCopExamenes(dato):
    ordenamientoBurbuja(dato[0], len(dato[0]))


def CopExamenes(dato):
    CopDet = 0
    Cop = 0
    cont = 0
    print(dato)
    for i in range(min(dato[0]), max(dato[0])+1):
        cont += 1
        Cop += dato[0].count(i)
    Cop -= cont
    for i in range(0, len(dato[0])):
        for k in range(i-dato[1],i):
            if (k >= 0 and (dato[0][k] == dato[0][i])):
                #print("k   ",k,dato[0][k],"",dato[0][i],i,"   i")
                CopDet+=1
                dato[0][k] = 0
    return (Cop,CopDet)

dato = [[1,2,3,1,2,3,1,2,1,1,2,3,2,1,3,2,3,2,2],2]
r = CopExamenes(dato)
print(r)