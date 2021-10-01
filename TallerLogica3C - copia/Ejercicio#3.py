# Ejercicio 3
'''

Yordan daniel Tarazona – 1004925617
Yessica María Granados Gauta – 1004851758
Angie yuliana lagos – 1005061253
Jean Carlos fuentes – 1005062696

    Calcular el valor de la cuota mensual y el numero de cuotas a pagar, por la realizacion
    de un prestamo en un banco con las siguientes condiciones: Si el prestamo es menor de $500000
    se paga un interes de 10% sobre el total del prestamo y las cuotas mensuales quedan de un 3%
    del monto total. Si el prestamo esta entre $500000 y $1000000(inclusive) se paga un interes del 7% y
    las cuotas quedan de un 5% del monto total. Y si el prestamo es superior a $1000000 se paga un interes
    del 4% y las cuotas quedan de un 7% del monto total.
'''
import time
def prestamo(valorpres, valorintr, valorcapt):
    capitalmes = (valorpres * valorcapt) / 100
    interesmes = (valorpres * valorintr) / 100
    x = valorpres / capitalmes
    cuota = capitalmes + (interesmes/x)
    return capitalmes, interesmes, cuota, x
v1 = int(input(f'Hola Bienvenido 💪 ( ͡❛ ͜ʖ ͡❛) 👊\n'
               f'Porfavor digite el valor del prestamo : $ '))
if (v1 >= 0 and v1 < 500000):
    inte = 10
    capt = 3
elif (v1 >= 500000 and v1 <= 1000000):
    inte = 7
    capt = 5
else:
    inte = 4
    capt = 7
a, b, c, d = prestamo(v1, inte, capt)
print(f'Calculando datos...\n'
      f'💪 (︡❛ ‿❛︠) 👊')
time.sleep(1)
print(f'Para un prestamo de : ${v1}\n'
      f'el interes es de {inte}% equivalente a total de : ${round(b,2)}\n'
      f'el interes  del  {inte}% por mes equivale a un  : ${round((b/d),2)}\n'
      f'el capital es de {capt}% equivalente a total de : ${round(a,2)}\n'
      f'valor de las cuotas por mes es de : ${round(c,2)}\n'
      f'con un total en cuotas de : {round(d,2)}\n'
      f'el saldo fin en total es de : ${v1 + b}')