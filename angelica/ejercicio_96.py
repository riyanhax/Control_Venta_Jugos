def IMC(esta, masa):
    imc = masa / pow(esta,2)
    rta = ""
    if imc < 21:
        rta = "Desnutrido"
    elif imc >= 21 and imc <= 25:
        rta = "Peso normal"
    elif imc > 25:
        rta = "Sobre peso"
    return rta

def individuo(vec1):
    may = vec1[0]
    men = vec1[0]
    for i in range(0, len(vec1)):
        if (vec1[i]>may):
            may=vec1[i]
        if (vec1[i]<men):
            men = vec1[i]
    return may, men

def llenar(can):
    lista = []
    for i in range(0, can):
        dato1 = int(input(f"ID #[{i+1}] -->"))
        dato2 = int(input(f"Edad [{i+1}] -->"))
        dato3 = float(input(f"Estatura en metros -->"))
        dato4 = int(input(f"Peso en kilos -->"))
        lista.append([dato1,dato2,dato3,dato4])
        print("")
    return lista

def mostrar(lista):
    m = lista
    cont = [0,0,0,0]
    vect = []
    pro = 0
    print(f'\n                      HISTORIAL \n'
          f'|-------------------------------------------------------|\n'
          f'|  Codigo  | Edad  | Estatura |  Masa  |      IMC       |\n'
          f'|----------|-------|----------|--------|----------------|')
    for i in range(0, len(lista)):
        imc = IMC(m[i][2], m[i][3])
        pro += m[i][1]
        vect.append(m[i][1])
        if (imc == "Desnutrido"):
            cont[0] += 1
        elif (imc == "Peso normal"):
            cont[1] += 1
        elif (imc == "Sobre peso"):
            cont[2] += 1
        print(
            f'|{"%9s" % m[i][0]} | {"%5s" % m[i][1]} | {"%8s" % m[i][2]} | {"%6s" % m[i][3]} | {"%14s" % imc} | ')
        print(f'|----------|-------|----------|--------|----------------|')
    print(f"\n|=====================|\n"
          f"|          IMC        |\n"
          f"|=====================|\n"
          f"| Desnutrido --> {cont[0]}    |\n"
          f"| Peso normal  --> {cont[1]}  |\n"
          f"| Sobre peso  --> {cont[2]}   |\n"
          f"|=====================|\n")
    may,men = individuo(vect)
    print(f"|=====================|\n"
          f"|    INDIVIDUOS       |\n"
          f"|=====================|\n"
          f"| Promedio --> {pro/len(lista)}   |\n"
          f"| Mayor     --> {may}    |\n"
          f"| Menor     --> {men}    |\n"
          f"|=====================|")

can = int(input(f"En cuantos se realizara el proceso? --> "))
mostrar(llenar(can))