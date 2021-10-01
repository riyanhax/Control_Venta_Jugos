'''
Desarrollar un programa que permita cargar  nombres  y edades de n personas
 Luego de realizar la carga por teclado de todos los datos
 Realizar las siguientes funciones:
 llenar: parametro nombre y edad y n cantidad de personas
imprimir: parametro nombre y edad y n cantidad de personas y muestra la informacion por columnas
mayores: los nombres de las personas mayores de edad (mayores o iguales a 18 anos)
ordenar: Tomando como vector base  la edad ordenando de mayor a menor
imprimir: los nombres  y las edades de las personas
mayoredad: decir la persona con mayor edad  y cuantos años tiene

'''
# ---------------------------------------------------
def llenar( n):
    nomb=[]    # vectores son variables locales
    edad=[ ]
    for i in range(0, n):
        print("Informacion de la persona No", i + 1)
        nomb.append(input("Nombre: "))
        temp = int(input("Edad(15-60): "))    # temp para asegurarnos que el dato es correcto
        while (temp < 15 or temp > 60):
            temp = int(input("ERROR:edad fuera de rango\nEdad(15-60): "))
        edad.append(temp)   # cuando el dato es correcto se agrega al vector
    return(nomb,edad)  # retornar los vectores se vuelven externos para usarlos en otras funciones

# ---------------------------------------------------
def imprimir(nom, eda, n):
    print("\t\t INFORMACION DE LA PERSONA\n      Nombre          Edad  ")
    for i in range(0, n):
        print( "  %10s" % nom[i], "  %10d  " % eda[i])
# ---------------------------------------------------
def ordenar(nomb, edad, n):
    for i in range(0, n):
        for j in range(i + 1, n):
            if (edad[i] < edad[j]):

                temp = edad[i]
                edad[i] = edad[j]
                edad[j] = temp

                temp = nomb[i]
                nomb[i] = nomb[j]
                nomb[j] = temp
# ====================================================
def mayores(nom,ed):
    l = len(ed)
    for i in range(0,l):
      if(ed[i]>17):
        print (nom[i])
# ====================================================
def mayoredad(nomb, edad, n):
    mayor = edad[0]
    quien = 0
    for i in range(1, n):
        if (edad[i] > mayor):
            mayor = edad[i]
            quien = i
    print("la persona con mayor edad  es: ", nomb[quien], " con los siguientes años--> ",mayor)
#=====================================================
n = int(input("Cantidad de personas? "))
(nombres,edades)=llenar( n)
print("\n Informacion Original:")
imprimir(nombres, edades, n)
ordenar(nombres, edades, n)
print("\n Informacion Ordenada por edades:")
imprimir(nombres,edades, n)
mayoredad(nombres,edades, n)
print ("\n Lista de todos los mayores de edad")
mayores(nombres,edades)