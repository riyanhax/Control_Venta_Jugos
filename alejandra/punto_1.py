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
        if num >= 1000:
            quita = num % 100
            a.append(quita)
            num //= 100
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

def porcien(x, y):
    des = 0
    print(x,y)
    if x <= 5:
        if y > 10:
            des = (35 * 450000) / 100
        elif (y > 6 and y < 9):
            des = (25 * 450000) / 100
    elif x > 5 and x < 10:
        if y > 10:
            des = (28 * 450000) / 100
        elif y > 6 and y < 9:
            des = (9 * 450000) / 100
    return des

def calMatricula(dato):
    valor = 0
    desc = 0
    if dato[1] > 4:
        des = (12 * 450000) / 100
        r = porcien(dato[2],dato[0])
        desc = r
        valor = (450000 - desc) + des
    elif dato[1] <= 4:
        r = porcien(dato[2],dato[0])
        desc = r
        valor = 450000 - desc
    return valor, desc


while True:
    num = int(input(f'Digite el codigo --> '))
    if (num >= 1000 and num <= 99999):
        break
    else:
        print(f'Codigo no valido!')
r = destruir(num)
rta, des = calMatricula(r)
print(f'El descuento es de ${des}\n'
      f'El valor a pagar por la matricula es de ${rta}.')