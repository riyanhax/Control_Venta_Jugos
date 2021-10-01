# Ejercicio 2
'''

Yordan daniel Tarazona – 1004925617
Yessica María Granados Gauta – 1004851758
Angie yuliana lagos – 1005061253
Jean Carlos fuentes – 1005062696

    Juan Pablo Montoya, entrena todos los días, recorriendo cierta cantidad de kilómetros, de tal
    forma que todos los días recorre el doble de lo que recorrió el día anterior más 10 km. Pero cada
    3 días recorre solo la mitad de lo que recorrió el día anterior. Realice una función que dado el
    número de kilómetros recorridos el primer día del entrenamiento y un número n de días y halle
    el total de kilómetros acumulados hasta ese día (el n-ésimo día).
    Por ejemplo, si el primer día recorrió 5 Km....
    Día Kms Recorridos Acumulado
    1     5               5
    2    (5*2)+10= 20     25
    3    20/2 = 10        35
    4   (10*2)+10 = 30    65
    5   (30*2)+10 = 70    135
    6    70/2 = 35        170
    7   (35*2) +10 = 80   250
'''
import time
def calculadistancia(dias, distan):
    x = 2
    almacena = distan
    while x <= dias:
        if x % 3 != 0:
            distan = (distan * 2) + 10
            almacena = almacena + distan
        else:
            distan = distan / 2
            almacena = almacena + distan
        print(f'El dia {x} corrio {int(distan)} kilometros')
        x = x + 1
    return distan, almacena
print(f'Hola bienvenido 💪 (︡❛ ‿❛︠) 👊')
dia = int(input(f'El numero de dias de ejercicio --> '))
kilometros = int(input(f'La cantidad de kilometros recorridos en el primer dias --> '))
print(f'Cargando ...\n'
      f'💪 (︡❛ ‿❛︠) 👊')
time.sleep(1)
a, b = calculadistancia(dia, kilometros)
print(f'Cargando ...\n'
      f'💪 (︡❛ ‿❛︠) 👊')
time.sleep(1)
print(f'Los kilometros recorridos en el ultimo dia # {dia} son : {int(a)}\n'
      f'Los kilometros acomulados durante los {dia} son : {int(b)}')