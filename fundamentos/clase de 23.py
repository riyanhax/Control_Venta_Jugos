'''
Desarrollar un programa en python que permita cargar nombres y edades de n personas
realizar el llenado por teclado
Realizar las siguiebtes funciones
llenar= Parametro nombre, edad, n cantidad de personas
imprimir= Parametro nombre, edad, n cantidad de personas y muestra la información por columnas
mayores= los nombres de las personas mayores de edad ( mayor de 17 años)
Ordenar= Tomando como vector base la edad
mayor edad= decir la persona con mayor edad y cuantos años tiene  ( Consulta)

def llenar(nom, eda):
    i = 0
    while True:
        print(f'Datos de la persona No.{i+1}')
        nom.append(input(f'Nombre --> '))
        eda.append(int(input(f'Edad --> ')))
        i += 1
        if nom == 'null':
            nom.pop('null')
            break
def mostrar(nom, eda):
    print("\t\t INFORMACION DE LAS PERSONAS\n Nombre   Edad")
    for i in range(0, len(nom)):
        print("%5s" % nom[i], "%8d" % eda[i])



nom = []
eda = []
llenar(nom, eda)
mostrar(nom, eda)
'''

a = float(input('valor A -->'))
b = float(input('valor b -->'))
c = float(input('valor c -->'))
v1 = (-b+(((b**2)-4)*(a*c))**(0.5))/(2*a)
v2 = (-b-(((b**2)-4)*(a*c))**(0.5))/(2*a)
print(f'el resultado es --> {v1}\n'
      f'el resultado es --> {v2}')
