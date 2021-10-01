'''La universidad de Pamplona desea llevar un registro de los 100 estudiantes deportistas vinculados a las selecciones de la
universidad. Existen 3 selecciones
Codigo         Nombre
1015           Futbol
1030           Rugby
1045           Taekwondo
De cada estudiante se conoce: Cedula, Sexo (1 Hombre, 2 Mujer), Edad, Código de la Selección a la que pertenece.
Realice con funciones: Llenado de la matriz. Determine el porcentaje de Hombres y mujeres (de toda la matriz). Determine la
seleccion con el deportista mas joven. Determine el número de deportistas por seleccion.'''

from random import randint

def crearmatriz():
    datos = []
    for i in range(0, 100):
        v = [0] * 4
        datos.append(v)
    return datos


def llenar(d,no, n):
    nombres=["Jorge ", "Miguel", "Jose ","Maria "," Marta","Magaly"]
    apellidos=["Rodriguez ","Sanchez ","Salamanca ","Cariongo ","Alvarez ","Malaguez "]
    print("\nrecoleccion de la informacion de los estudiantes\n")
    for i in range(n):
        d[i][0]= randint(10000,99999) #cc
        d[i][1]= randint(1,2)         #sexo 1 hombre 2 mujer
        d[i][2] = randint(16, 29)     #edad
        d[i][3] = randint(1, 3)       #seleccion
        d[i][3] = d[i][3]*15 + 1000
        if(d[i][1]==1):
          no[i] =nombres[ randint(0,2)] # escoje entre 0, 1 o 2 que son nombres masculinos
        else:
          no[i] = nombres[randint(3, 5)]# escoje entre 3, 4 o 5 que son nombres femeninos
        no[i] = no[i] + apellidos[randint(0,5)] + apellidos[randint(0,5)]

def porsex(d, n):
    hom = 0
    for i in range(0, n):
        if (d[i][1] == 1):
            hom = hom + 1
    hom = (hom / n) * 100
    muj = 100 - hom

    print("\nEL PORCENTAJE DE MUJERES EN LAS SELECCIONES ES DE: ", muj, "%")
    print(" Y EL PORCENTAJE DE HOMBRES EN LAS SELECCIONES ES DE: ", hom, "%")


def masjov(d,no, n):
    jov = d[0][2]
    se = d[0][3]
    quien = 0 # guarda la posicion donde se encuentra el alumno mas joven
    for i in range(0, n):
        if (d[i][2] < jov):
            jov = d[i][2]
            se = d[i][3]
            quien = i

    if (se == 1015):
        print("\n La seleccion de futboll tiene el alumno mas joven con ", jov, " años")
    else:
        if (se == 1030):
            print("\n La seleccion de rugby tiene el alumno mas joven con ", jov, " años\n")
        else:
            print("\n La seleccion de taekondo tiene el alumno mas joven con ", jov, " años\n")
    print("Y  se  llama ",no[quien])

def aluxsel(d, n):
    fut = 0
    rugby = 0
    tae = 0
    for i in range(0, n):
        if (d[i][3] == 1015):
            fut = fut + 1
        elif (d[i][3] == 1030):
            rugby = rugby + 1
        else:
            tae = tae + 1

    print("\n La seleccion de futbol tiene: ", fut, " alumnos")
    print("\n la seleciion de rugby tiene ", rugby, " alumnos")
    print("\n La seleccion de taekondo tiene ", tae, " alumnos\n")



def mostrar(d,no,n):
    print("INFORMACION DE LOS ESTUDIANTES DE LAS SELECCIONES DE LA UNIVERSIDAD")
    print("      Nombre                 cedula  sexo   edad   Seleccion")
    for i in range(0,n):
        print("%-30s"%no[i],d[i][0],end=' ')

        if(d[i][1]==1):
           print(" Hombre",end=' ' )
        else:
           print(" Mujer ",end=' ' )

        print(d[i][2], end='   ')
        if (d[i][3] == 1015):
            print(" Futbol ")
        elif (d[i][3] == 1030):
            print(" Rugby ")
        else:
            print(" Taekondo ")

print(" programa para manejar la informacion de las selecciones de la universidad")
n=int(input(" numero de estudiantes que manejar(maximo 100)"))
nomb=[" "]*n
datos=crearmatriz()
llenar(datos,nomb,n)
mostrar(datos,nomb,n)
porsex(datos,n)
masjov(datos,nomb,n)
aluxsel(datos,n)