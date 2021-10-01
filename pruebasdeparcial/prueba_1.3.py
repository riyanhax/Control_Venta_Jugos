valor=int(input(f'Digite el valor de la compra\t:'))
des = 0
d = 0
if (valor >= 1000000):
    if (valor >= 1000000 and valor < 4000000):
        d = 2.4
        des = (valor*d)/100
    if (valor >= 4000000 and valor <= 8000000):
        d = 10
        des = (valor*d)/100
    if (valor > 8000000):
        d = 12
        des = (valor*d)/100
    print(f'La compra total es de :{valor} con un descuento de {des} equivalente al {d}% y el valor a pagar es de :{valor-des}')
else:
    print(f'La compra total es de :{valor} con un descuento de {des} equivalente al {d}% y el valor a pagar es de :{valor-des}')