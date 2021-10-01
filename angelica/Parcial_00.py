def Total(lista1, lista2, lista3):
    tal = 0
    for i in range(0, len(lista1)):
        tal += (lista1[i] * lista3[i])
        if lista2[i] == "Pesado" or lista2[i] == "pesado":
            tal += ((lista1[i] * lista3[i]) * 15) / 100
    return tal

def llenar(Cant):
    lista1 = []
    lista2 = []
    lista3 = []
    lista4 = []
    for i in range(0, Cant):
        dato1 = int(input(f"Referencia #[{i + 1}] -->"))
        lista1.append(dato1)
        dato2 = int(input(f"Valor -->"))
        lista2.append(dato2)
        dato3 = str(input(f"Tipo -->"))
        lista3.append(dato3)
        dato4 = int(input(f"Cantidad disponible -->"))
        lista4.append(dato4)
    return lista1, lista2, lista3, lista4

Cant = int(input("Cual es la cantidad de productos: "))
l1, l2, l3, l4 = llenar(Cant)
tal = Total(l2, l3, l4)
print(f"El valor total del inventario es de : ${tal}")