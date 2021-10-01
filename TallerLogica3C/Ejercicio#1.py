# Ejercicio1
'''

Yordan daniel Tarazona – 1004925617
Yessica María Granados Gauta – 1004851758
Angie yuliana lagos – 1005061253
Jean Carlos fuentes – 1005062696

    Un peaje de la ciudad quiere que usted sistematice el control del pago de los peajes, por este pasan tres tipos de automotores:
    1. Vehiculos, 2. Camiones y 3. Tractomulas no se sabe cuantos de estos pasan al dia por el peaje,
    pero cuando el dia finaliza se registra un tipo de automotor cero 0.
    El cobro por cada tipo de automotor es el siguiente:
     Tipo Valor
     1. Vehiculo $ 3.500
     2. Camion $ 12.000
     3. Tractomula $ 16.000
    Desarrolle un programa en python donde conociendo el tipo de automotor determinar:
    El valor a pagar por cada automotor que pase por el peaje
    Total recaudado en el peaje en ese dia.
    Total recaudado por cada tipo de automotor.
    Cual es el tipo de Automotor que mas transita por el peaje.
'''
import time
def peaje(x, y, z):
    veh = x * 3500
    cam = y * 12000
    tra = z * 16000
    res = veh + cam + tra
    return (veh, cam, tra, res)
def mostrar():
    a,b,c,d = peaje(c1,c2,c3)
    print(f'\n |--------------------------------------------------------|\n'
           f'|    Total recaudado es de: ${d}\n'
           f'|    Total racaudado por {Ve} es de:${a}\n'
           f'|    Total racaudado por {Ca} es de:${b}\n'
           f'|    Total racaudado por {Tr} es de:${c}\n'
           f' | -------------------------------------------------------|\n')
c1=0
c2=0
c3=0
Ve = 'Vehiculo'
Ca = 'Camion'
Tr = 'Tractomula'
while True:
    print(f'\n|---------------------------------------------|\n'
          f'|    Tipos de Automotor y sus Tarifas         |\n'
          f'|---------------------------------------------|\n'
          f'|       [1] {Ve} ----> $3.500             |\n'
          f'|       [2] {Ca} ------> $12.000            |\n'
          f'|       [3] {Tr} --> $16.000            |\n'
          f'|       [0] Finalizar                         |\n'
          f'|---------------------------------------------|\n')
    v1 = int(input(f'El tipo de Automotor es :'))
    if v1 < 0 or v1 > 3:
        print(f'!Error¡ Porfavor seleccione una opción del menu.')
    if v1 == 1:
        c1 = c1 + 1
    elif v1 == 2:
        c2 = c2 + 1
    elif v1 == 3:
        c3 = c3 + 1
    elif v1 == 0:
        print(f'  cargando...\n'
              f'💪 (︡❛ ‿❛︠) 👊')
        time.sleep(1.1)
        if c1 > c2 and c1 > c3:
            mastra = (f'El que mas transito es {Ve} con :{c1} veses')
        elif c2 > c1 and c2 > c3:
            mastra = (f'El que mas transito es {Ca} con :{c2} veses')
        elif c3 > c1 and c3 > c2:
            mastra = (f'El que mas transito es {Tr} con :{c3} veses')
        else:
            mastra = (f'----> todos transitaron igual: {Ve} ----> {c1} veses\n'
                      f'                               {Ca} ------> {c2} veses\n'
                      f'                               {Tr} --> {c3} veses\n')
        break
    if v1 >= 0 and v1 <= 3:
       mostrar()
    print(f'  cargando...\n'
          f'💪 (︡❛ ‿❛︠) 👊')
    time.sleep(1)
mostrar()
print(mastra)