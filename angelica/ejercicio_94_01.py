def ordena(lista,tam):
    for i in range(0,tam-1):
        min=i
        for j in range(i+1,tam):
            if lista[min] > lista[j]:
                min=j
        aux=lista[min]
        lista[min]=lista[i]
        lista[i]=aux
    return lista

def mostrar(lista1, lista2, tam):
    print("lista #1")
    for i in range(0, tam):
        print(lista1[i], end="")
    print("")
    print("lista #2")
    for i in range(0, tam):
        print(lista2[i], end="")

can = int(input("Cantidad de numeros : "))
print("\nLista v1\n")
lista1 = []
for i in range(0, can):
    lista1.append(int(input(f"Ingrese numero : ")))
print("\nLista v2\n")
lista2 = []
for i in range(0, can):
    lista2.append(int(input(f"Ingrese numero : ")))
lista1 = ordena(lista1, can)
lista2 = ordena(lista2, can)
mostrar(lista1, lista2, can)