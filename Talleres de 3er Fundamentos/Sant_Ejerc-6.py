'''
6-En una empresa de taxis se desea registrar la información de las N (N dado por teclado)
carreras realizadas por sus móviles(taxis) a los clientes de la empresa, existen 5 Taxis.
Dada la siguiente información: Código del taxi, cedula del cliente, tipo de
servicio y valor del servicio. Donde: ( Leonel Santiago)
Determine:
 Cuál es el valor total producido por cada taxi.
 Cuál es el servicio que más se usa.
 Que cliente paga más por un servicio.
Ejemplo de representación de la información en forma de matriz (arreglo
bidimensional):
Número del taxi Cedula Cliente Tipo servicio Valor
02 88030900 03 5000
03 60623890 01 2500
01 79120765 02 3000
'''

def crearmatriz():
    datos = []
    for i in range(0, 100):
        v = [0] * 4
        datos.append(v)
    return datos
def llenar(d, n):
    print("\nrecoleccion de la informacion del servicio\n")
    print(f'|----------------------------------------------|\n'
          f'|         Taxi                Servicio         |\n'
          f'|----------------------------------------------|\n'
          f'|          [1]                   [1]           |\n'
          f'|          [2]                   [2]           |\n'
          f'|          [3]                   [3]           |\n'
          f'|         [...5]                               |\n'
          f'|----------------------------------------------|\n')
    for i in range(n):
        print(f'Servicio No.{i + 1}')
        d[i][0] = int(input(f'Codigo del taxi : '))  # codigo taxi
        d[i][1] = int(input(f'Cedula del cliente : '))  # CC
        d[i][2] = int(input(f'Tipo de servicio : '))  # tipo de sevicio
        d[i][3] = int(input(f'Valor del servicio : '))  # valor del servicio
        if d[i][2] < 0 or d[i][2] > 3:
            while True:
                print(f'Error! Verifique los datos de  (Tipo del servicio).')
                d[i][2] = int(input(f'Tipo de servicio : '))  # tipo de sevicio
                if d[i][2] > 0 and d[i][2] <= 3:
                    break
        if d[i][0] < 0 or d[i][0] > 5:
            while True:
                print(f'Error! Verifique los datos de  (Codigo del taxi).')
                d[i][0] = int(input(f'Codigo del taxi : '))  # tipo de sevicio
                if d[i][0] > 0 and d[i][0] <= 5:
                    break
        print('===============================================================')
def Valortaxi(d,n):
    VecValor = [0]*5
    for i in range(n):
        valor = d[i][3]
        if d[i][0] == 1:
            b = 0
            a = VecValor[b]
            a += valor
            VecValor[b] = a
        elif d[i][0] == 2:
            b = 1
            a = VecValor[b]
            a += valor
            VecValor[b] = a
        elif d[i][0] == 3:
            b = 2
            a = VecValor[b]
            a += valor
            VecValor[b] = a
        elif d[i][0] == 4:
            b = 3
            a = VecValor[b]
            a += valor
            VecValor[b] = a
        elif d[i][0] == 5:
            b = 4
            a = VecValor[b]
            a += valor
            VecValor[b] = a
    return VecValor
def servimax(d,n):
    max1 = 0
    max2 = 0
    max3 = 0
    maxT = []
    for j in range(n):
        if d[j][2] == 1:
            max1 += 1
        elif d[j][2] == 2:
            max2 += 1
        elif d[j][2] == 3:
            max3 += 1
    if max1 > max2 and max1 > max3:
        maxT.append(1)
    elif max2 > max1 and max2 > max3:
        maxT.append(2)
    elif max3 > max2 and max3 > max1:
        maxT.append(3)
    elif max1 > 0 or max2 > 0 or max3 > 0:
        if max1 == max2 and max1 == max3:
            a = (1,2,3)
            maxT.append(a)
        elif max1 == max2:
            a = (1,2)
            maxT.append(a)
        elif max1 == max3:
            a = (1,3)
            maxT.append(a)
        elif max2 == max3:
            a = [2,3]
            maxT.append(a)
    return maxT
def clienmax(d,n):
    max = d[0][3]
    for j in range(n):
        if d[j][3] > max:
            max = d[j][3]
            quien = d[j][1]
        elif d[j][3] == max:
            max = d[j][3]
            quien = d[j][1]
    return max,quien
def pantall(d,n):
    for i in range(n):
        print(f'|     "{d[i][0]}"     |"{d[i][1]}"|    "{d[i][2]}"    | "{d[i][3]}" |')
    print('|-----------------------------------------|\n')
print(f'Programa de taxi')
n = int(input(f'Cualtos clientes (maximo 5) :'))
dat = crearmatriz()
llenar(dat,n)
print(f'|-----------------------------------------|\n'
      f'| Codigo taxi | CC | Tip Servi |   Valor  |\n'
      f'|-----------------------------------------|')
pantall(dat,n)
vxt = Valortaxi(dat,n)
print('===============================================================')
print(f'\nVolores por Taxi:\n')
for i in range(n):
    print(f'Taxi {dat[i][0]} = {vxt[i]} ')
print('===============================================================')
svm = servimax(dat,n)
print(f'\nEl servicio mas usado es el = {svm}\n')
print('===============================================================')
ctm1,ctm2 = clienmax(dat,n)
print(f'\nEl cliente que mejor pago es el = {ctm2} con un valor de = {ctm1}\n')
print('===============================================================')
