def calculo(x):
    if x > 0:
        v1 = 'positivo'
    elif x < 0:
        v1 = 'negativo'
    else:
        v1 = 'neutro'
    return v1
r = int(input('dijite el numero : '))
a = calculo(r)
print('el numero ingresado es = "',a,'"')