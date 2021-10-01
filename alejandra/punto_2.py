def invertir(vec1):
    vecinv = []
    x = len(vec1)-1
    while x >= 0:
        vecinv.append(vec1[x])
        x -= 1
    return vecinv

def destruir(num):
    a = []
    while num > 0:
        if num >= 100000:
            quita = num % 100
            a.append(quita)
            num //= 100
        if num < 100000:
            quita = num % 10
            a.append(quita)
            num //= 10
        if num < 1000:
            quita = num % 10
            a.append(quita)
            num //= 10
        if num < 100:
            quita = num % 100
            a.append(quita)
            num //= 100
    aux = invertir(a)
    return aux

def porcien(x, y, matri):
    des = 0
    info = 0
    if x < 5:
        if y > 10:
            des = (35 * matri) / 100
            info = 35
        elif (y > 6 and y < 9):
            des = (25 * matri) / 100
            info = 25
    elif (x > 5 and x < 10):
        if y > 10:
            des = (28 * matri) / 100
            info = 28
        elif (y > 6 and y < 9):
            des = (9 * matri) / 100
            info = 9
    return des, info

def calMatricula(dato,matri):
    valor = 0
    desc = 0
    info = 0
    reca = 0
    if dato[1] == 1:
        desc = matri
    if dato[1] == 2:
        desc = matri/2
        valor = matri - desc
    else:
        if dato[3] > 4:
            reca = (12 * matri) / 100
            r, info = porcien(dato[4], dato[0], matri)
            desc = r
            valor = (matri - desc) + reca
        elif dato[3] <= 4:
            r, info = porcien(dato[4],dato[0], matri)
            desc = r
            valor = matri - desc
    return valor, desc, info, reca

def bonosis(x, y):
    bono = 0
    if x < 5:
        if y == 1:
            bono = 230000
        elif (y == 2 or y == 3):
            bono = 200000
    elif (x > 5 and x < 10):
        if y == 1:
            bono = 180000
        elif (y == 2 or y == 3):
            bono = 100000
    return bono

matri = int(input(f'¿Cual es el valor de la matricula? -->'))
while True:
    num = int(input(f'Digite el codigo --> '))
    if (num >= 1000000 and num <= 9999999):
        break
    else:
        print(f'Codigo no valido!')

r = destruir(num)
rta, des, info, reca = calMatricula(r, matri)
bono = bonosis(r[4], r[2])
print(f'Familia --> {r[0]}.\n'
      f'Sisben --> {r[1]}.\n'
      f'Estracto --> {r[2]}.\n'
      f'Carrera --> {r[3]}.\n'
      f'Puesto --> {r[4]}.\n'
      f'El descuento es del {info}% --> ${des}.\n'
      f'Con el recargo del 12% --> {reca}.\n'
      f'El estudiante tiene un bono de --> ${bono}.\n'
      f'El valor a pagar por la matricula es de --> ${rta-bono}.')