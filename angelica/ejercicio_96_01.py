def mostrar(vector):
    v = vector
    cont = [0,0,0,0]
    vect = []
    prom = 0
    for i in range(0, len(vector)):
        idic = INDIC(v[i][2], v[i][3])
        prom += v[i][1]
        vect.append(v[i][1])
        if (idic == "Desnutrido"):
            cont[0] += 1
        elif (idic == "Peso normal"):
            cont[1] += 1
        elif (idic == "Sobre peso"):
            cont[2] += 1
        print(
            f'Codigo: {v[i][0]} \n'
            f'Edad: {v[i][1]} \n'
            f'Estatura: {v[i][2]} \n'
            f'Masa: { v[i][3]} \n'
            f'IMC {idic} \n')

    print(f"\n Desnutrido --> {cont[0]} \n"
          f" Peso normal  --> {cont[1]} \n"
          f" Sobre peso  --> {cont[2]}  \n")

    menor, mayor = Persona(vect)
    prom = prom/len(vector)
    print(f" Promedio --> {prom} \n"
          f" Mayor     --> {mayor} \n"
          f" Menor     --> {menor} \n")

def Persona(vec1):
    may = vec1[0]
    men = vec1[0]
    for i in range(0, len(vec1)):
        if (vec1[i]>may):
            may=vec1[i]
        if (vec1[i]<men):
            men = vec1[i]
    return men, may

def INDIC(estatura, masa):
    imc = masa / estatura**2
    if imc < 21:
        return "Desnutrido"
    elif imc >= 21 and imc <= 25:
        return "Peso normal"
    elif imc > 25:
        return "Sobre peso"

def llenar(can):
    vect = []
    for i in range(0, can):
        dato1 = int(input(f"ID #[{i+1}] -->"))
        dato2 = int(input(f"Edad [{i+1}] -->"))
        dato3 = float(input(f"Estatura en metros -->"))
        dato4 = int(input(f"Peso en kilos -->"))
        vect.append([dato1,dato2,dato3,dato4])
    return vect

Cant = int(input(f"Cantidad de personas : "))
vect = llenar(Cant)
mostrar(vect)