'''
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
dias = int(input(f'El numero de dias: '))
km = int(input(f'La cantidad de kilometros que corrio en el primer dias: '))
def distancia(dia, distancia):
    i = 2
    cont = distancia
    while i <= dia:
        if i % 3 != 0:
            distancia = (distancia * 2) + 10
            cont = cont + distancia
        else:
            distancia = distancia / 2
            cont = cont + distancia
        i = i + 1
    return distancia, cont
a, y = distancia(dias, km)
print(f'Los kilometros que corrio en el ultimo dia son : {a}')
print(f'Los kilometros acomulados son : {y}')