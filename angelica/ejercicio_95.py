def calDescuento(ed, zona):
    valor = 0
    if ed < 18:
        if zona == 2:
            valor = (500000 * 30) / 100
        elif zona == 1:
            valor = (1000000 * 30) / 100
    return valor

def calMenores(lista):
    cont = [0,0]
    for i in range(0, len(lista)):
        if lista[i][1] < 18:
            if lista[i][2] == 1:
                cont[0] += 1
            elif lista[i][2] == 2:
                cont[1] += 1
    return cont

def llenar(can):
    lista = []
    for i in range(0, can):
        dato1 = int(input(f"Codigo del estudiante [{i+1}]-->"))
        dato2 = int(input(f"Edad del estudiante [{i+1}] -->"))
        dato3 = int(input(f"Zona [1] Urbana, [2] Rural  -->"))
        lista.append([dato1,dato2,dato3])
        print("")
    return lista

def mostrar(lista):
    m = lista
    r = calMenores(lista)
    print(f'\n                      HISTORIAL \n'
          f'|-------------------------------------------------------------------|\n'
          f'|  Codigo  | Edad  | Zona |  Descuento  |  Matricula   |   Total    |\n'
          f'|----------|-------|------|-------------|--------------|------------|')
    for i in range(0, len(lista)):
        des = calDescuento(lista[i][1],lista[i][2])
        if (m[i][2] == 1):
            matri = 1000000
        else:
            matri = 500000
        print(
            f'|{"%9s" % m[i][0]} | {"%5s" % m[i][1]} | {"%4s" % m[i][2]} | {"%11s" % des} | {"%12s" % matri} | '
            f'{"%10s" % (matri - des)} ')
        print(f'|----------|-------|------|-------------|--------------|------------|')

    print(f"|=================|\n"
          f"|     Menores     |\n"
          f"|=================|\n"
          f"| Urbana --> {r[0]}    |\n"
          f"| Rural  --> {r[1]}    |\n"
          f"|=================|")

can = int(input(f"Cual es la cantidad de alumnos --> "))
mostrar(llenar(can))