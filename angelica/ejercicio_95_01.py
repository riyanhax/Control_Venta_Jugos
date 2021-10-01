def Menores(vector):
    contador = [0,0]
    for k in range(0, len(vector)):
        if vector[k][1] < 18:
            if vector[k][2] == 1:
                contador[0] += 1
            elif vector[k][2] == 2:
                contador[1] += 1
    return contador

def Descuento(ed, zona):
    valor = 0
    if ed < 18:
        if zona == 2:
            valor = (500000 * 30) / 100
        elif zona == 1:
            valor = (1000000 * 30) / 100
    return valor

def llenar(Cant):
    vector = []
    for i in range(0, Cant):
        x1 = int(input(f"Codigo del estudiante [{i+1}]-->"))
        x2 = int(input(f"Edad del estudiante [{i+1}] -->"))
        x3 = int(input(f"Zona [1] Urbana,\n"
                       f"     [2] Rural  -->"))
        vector.append([x1,x2,x3])
        print("")
    return vector

def mostrar(vector):
    v = vector
    for i in range(0, len(vector)):
        descuento = Descuento(vector[i][1],vector[i][2])
        if (v[i][2] == 1):
            matri = 1000000
        else:
            matri = 500000
        print(
            f"Codigo: {v[i][0]}\n"
            f"Edad: {v[i][1]} \n"
            f"Zona: {v[i][2]} \n"
            f"Decuento: {descuento} \n"
            f"Matricula: {matri} \n"
            f"Total: {(matri - descuento)} \n")

    m = Menores(vector)
    print(f"Urbana  |  Rural\n"
          f"  {m[0]}         {m[1]}\n")

Cant = int(input(f"cantidad de alumnos: "))
vector = llenar(Cant)
mostrar(vector)