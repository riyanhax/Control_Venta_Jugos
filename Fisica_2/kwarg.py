import time
def fuerza_elec(tipo, *kwargs):
    r = 0
    if tipo == 1:
        print(f'--> {kwargs}')
        r = kwargs[0] - (kwargs[1] * kwargs[2])
    elif tipo == 2:
        r = (kwargs[0] * kwargs[1]) + (kwargs[0] * kwargs[2])
    elif tipo == 3:
        r = kwargs[0] / (kwargs[1] + kwargs[2])
    elif tipo == 4:
        r = ((kwargs[0]**2)*kwargs[1]) + ((kwargs[0]**2)*kwargs[2])
    return r
def resis_serie(tipo, *kwargs):
    r = 0
    if tipo == 1:
        r = kwargs[0] + kwargs[1]
    elif tipo == 2:
        r = (kwargs[0]*kwargs[1]) + (kwargs[2]*kwargs[3])
    elif tipo == 3:
        for i in kwargs:
            r += i
    return r
def resis_serie_req(tipo, kwargs):
    r = 0
    if tipo == 3:
        for i in kwargs:
            r += i
    elif tipo == 2:
        for i in kwargs:
            r += 1/i
        r = 1/r
    return r
def paralelo(tipo, *kwargs):
    r = 0
    if tipo == 1:
        for i in kwargs:
            r += i
    return r
kwa = []
while True:
    print('''
             |-----------------------------------------------|
             |        [1] --> Fuerza Electromotriz           |
             |        [2] --> Resistores en Serie            |
             |        [3] --> Resistores en Paralelo         |
             |        [0] --> salir                          |
             |-----------------------------------------------|''')
    pre = int(input(f'Cual es tú elección --> '))
    if pre == 1:
        pre1 = int(input(f'Cual formula desea --> '))
        if pre1 == 1:
            print(f'Recuerda las variable en su orden "e, I, r".')
            e = int(input(f'Cual es el valor de "e" --> '))
            I = int(input(f'Cual es el valor de "I" --> '))
            r = int(input(f'Cual es el valor de "r" --> '))
            res = fuerza_elec(pre1, e, I, r)
            print(f'La respuesta es --> {res}')
            time.sleep(1)
        elif pre1 == 2:
            print(f'Recuerda las variable en su orden "I, R, r".')
            I = int(input(f'Cual es el valor de "I" --> '))
            R = int(input(f'Cual es el valor de "R" --> '))
            r = int(input(f'Cual es el valor de "r" --> '))
            res = fuerza_elec(pre1, I, R, r)
            print(f'La respuesta es --> {res}')
            time.sleep(1)
        elif pre1 == 3:
            print(f'Recuerda las variable en su orden "e, R, r".')
            e = int(input(f'Cual es el valor de "e" --> '))
            R = int(input(f'Cual es el valor de "R" --> '))
            r = int(input(f'Cual es el valor de "r" --> '))
            res = fuerza_elec(pre1, e, R, r)
            print(f'La respuesta es --> {res}')
            time.sleep(1)
        elif pre1 == 4:
            print(f'Recuerda las variable en su orden "I, R, r".')
            I = int(input(f'Cual es el valor de "I" --> '))
            R = int(input(f'Cual es el valor de "R" --> '))
            r = int(input(f'Cual es el valor de "r" --> '))
            res = fuerza_elec(pre1, I, R, r)
            print(f'La respuesta es --> {res}')
            time.sleep(1)
    elif pre == 2:
        pre1 = int(input(f'Cual formula desea --> '))
        if pre1 == 1:
            print(f'Recuerda las variable en su orden "I1, I2".')
            I1 = int(input(f'Cual es el valor de "I1" --> '))
            I2 = int(input(f'Cual es el valor de "I2" --> '))
            res = resis_serie(pre1, I1, I2)
            print(f'La respuesta es --> {res}')
            time.sleep(1)
        elif pre1 == 2:
            print(f'Recuerda las variable en su orden "I1, R1, I2, R2".')
            I1 = int(input(f'Cual es el valor de "I1" --> '))
            R1 = int(input(f'Cual es el valor de "R1" --> '))
            I2 = int(input(f'Cual es el valor de "I2" --> '))
            R2 = int(input(f'Cual es el valor de "R2" --> '))
            res = resis_serie(pre1, I1, R1, I2, R2)
            print(f'La respuesta es --> {res}')
            time.sleep(1)
        elif pre1 == 3:
            v1 = int(input(f'Recuerda las variable en su orden "R", cuantos valores son:'))
            i = 1
            while i <= v1:
                kwa.append(int(input(f'Cual es el valor de "{i}" --> ')))
                i += 1
            res = resis_serie_req(pre1, kwa)
            print(f'La respuesta es --> {res}')
            time.sleep(1)
    elif pre == 3:
        pre1 = int(input(f'Cual formula desea --> '))
        if pre1 == 1:
            print(f'Recuerda las variable en su orden "I1, I2".')
            I1 = int(input(f'Cual es el valor de "I1" --> '))
            I2 = int(input(f'Cual es el valor de "I2" --> '))
            res = paralelo(pre1, I1, I2)
            print(f'La respuesta es --> {res}')
            time.sleep(1)
        elif pre1 == 2:
            v1 = int(input(f'Recuerda las variable en su orden "R", cuantos valores son:'))
            i = 1
            while i <= v1:
                kwa.append(int(input(f'Cual es el valor de "{i}" --> ')))
                i += 1
            res = resis_serie_req(pre1, kwa)
            print(f'La respuesta es --> {res}')
            time.sleep(1)
    elif pre == 0:
        break
print(f'Que tenga buen dia :)')

a = fuerza_elec(1,2,3,4)
print(f'el resultado es  --> {a}')