def buscar(vector):
    menor = vector[0]
    for i in range(0, len(vector)):
        if (vector[i] < menor):
            menor = vector[i]
            pos = i
    return menor, pos

def llenar(cant):
    vector = []
    for i in range(0,cant):
        num = int(input(f"Numero en la posicion: [{i}] --> "))
        vector.append(num)
    return vector

cant = int(input(f"Cantidad de numeros --> "))
vect = llenar(cant)
men, pos = buscar(vect)
print(f"el numero mas pequeño es: [{men}] y el esta en la posicion: [{pos}]")
