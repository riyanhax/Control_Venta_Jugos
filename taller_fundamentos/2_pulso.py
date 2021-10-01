'''2. Calcular el número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico; la fórmula que se
        aplica cuando el sexo es femenino es:
        núm. pulsaciones = (220 - edad)/10
        y si el sexo es masculino:
        núm. pulsaciones = (210 - edad) /10
'''

v1 = int(input('dijite su edad --> '))
v2 = str(input('cual es tu genero M o F --> '))
if ((v2 == 'M') or (v2 == 'm')):
    v3 = (210 - v1) / 10
elif ((v2 == 'F') or (v2 == 'f')):
    v3 = (220 - v1) / 10
print('Su numero de pulsaciones durante ejercicios aerobicos debe ser de: ', v3, ' cada 10 segundos')
