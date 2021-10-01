'''
    Calcular el valor de la cuota mensual y el numero de cuotas a pagar, por la realizacion
    de un prestamo en un banco con las siguientes condiciones: Si el prestamo es menor de $500000
    se paga un interes de 10% sobre el total del prestamo y las cuotas mensuales quedan de un 3%
    del monto total. Si el prestamo esta entre $500000 y $1000000(inclusive) se paga un interes del 7% y
    las cuotas quedan de un 5% del monto total. Y si el prestamo es superior a $1000000 se paga un interes
    del 4% y las cuotas quedan de un 7% del monto total.
'''
prest = int(input(f'valor del prestamo :  '))
if (prest >= 0 and prest < 500000):
    interes = 10
    cuenta = 3
elif (prest >= 500000 and prest <= 1000000):
    interes = 7
    cuenta = 5
else:
    interes = 4
    cuenta = 7
def calculo(pres, intr, capt):
    cont = (pres * capt) / 100
    inters = (pres * intr) / 100
    a = pres / cont
    cuota = cont + (inters/a)
    return cont, inters, cuota, a
a, b, c, d = calculo(prest, interes, cuenta)
print(f'Para un prestamo de : {prest}')
print(f'cuotas por mes es de : ${round(c,2)}')
print(f'total en cuotas de : {round(d,2)}')
print(f'total final es de : ${prest + b}')
