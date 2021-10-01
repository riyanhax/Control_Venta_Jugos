'''
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
cont1=0
cont2=0
cont3=0
while True:
    print(f'|       Automotor y sus Tarifas               |')
    print(f'|.............................................|')
    print(f'|       [1] Vehiculo : $3.500                 |')
    print(f'|       [2] Camion : $12.000                  |')
    print(f'|       [3] Tractomula : $16.000              |')
    print(f'|       [0] Finalizar                         |')
    v1 = int(input(f'opcion automotor es :'))
    if v1 == 1:
        cont1 = cont1 + 1
    elif v1 == 2:
        cont2 = cont2 + 1
    elif v1 == 3:
        cont3 = cont3 + 1
    elif v1 == 0:
        if cont1 > cont2 and cont1 > cont3:
            pantalla = (f'el transito es: Vehiculo con :{cont1}')
        elif cont2> cont1 and cont2 > cont3:
            pantalla = (f'el transito es: Camion con :{cont2}')
        elif cont3 > cont1 and cont3 > cont2:
            pantalla = (f'el transito es: Tractomula con :{cont3}')
        else:
            pantalla = (f'el transito es: Vehiculo :{cont1}, Camion :{cont2} y Tractomula :{cont3}')
        break
def vista():
    a,b,c,d = calculos(cont1,cont2,cont3)
    print(f'     Total es de: ${d}\n'
           f'    Total por Vehiculo es de:${a}\n'
           f'    Total por Camiones de:${b}\n'
           f'    Total por Tractomula es de:${c}\n')
def calculos(a, b, c):
    Vehiculo = a * 3500
    Camiones = b * 12000
    Tractomula = c * 16000
    total = Vehiculo + Camiones + Tractomula
    return (Vehiculo, Camiones, Tractomula, total)
vista()
print(pantalla)