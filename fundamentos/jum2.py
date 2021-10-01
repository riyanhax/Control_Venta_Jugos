'''
Desarrollar un programa que permita cargar 5 nombres de personas y sus edades
respectivas. Luego de realizar la carga por teclado de todos los datos imprimir
los nombres de las personas mayores de edad (mayores o iguales a 18 años)
ordenar=tomando como vector base las edades de las personas
imprimir: los nombres y edades de las personas en columnas
'''
def llenar(edad,n):
    nomb=[]
    for i in range(0,n):
      nombre = input("Escriba el nombre No "+ str(i+1)+": ")
      nomb.append(nombre)
      edad[i] = int(input("Edad: "))
    return (nomb)
#-------------------------------
def mayores(nom,ed):
    l = len(ed)
    print ("Lista de todos los mayores de edad")
    for i in range(0,l):
      if(ed[i]>17):
        print (nom[i])
#================================
def ordenar(nomb,edad,n):
    for i in range(0,n):
        for j in range(i+1,n):
            if(edad[i]<edad[j]):
                aux=edad[i]
                edad[i]=edad[j]
                edad[j]=aux

                aux=nomb[i]
                nomb[i]=nomb[j]
                nomb[j]=aux

def imprimir(nomb, ed, n):
    print("\n|=============================|")
    print("| DATOS DE LAS PERSONAS       |")
    print("|=============================|")
    print("| No |   Nombre       | Edad  |")
    for i in range(0, n):
        men = "| " + '{:>2s}'.format(str(i + 1)) + " | "
        men = men + '{:>15s}'.format(str(nomb[i])) + "| "
        men = men + '{:>5s}'.format(str(ed[i])) + " | "
        print("|----+--------------+---------|")
        print(men)
    print("|-----------------------------|")

n=int(input(" ingrese la longitud del vector:"))
nomb=[""]*n
edad=[0]*n
nomb = llenar(edad,n)
mayores(nomb,edad)
ordenar(nomb,edad,n)
print("informacion ordenada por edades")
imprimir(nomb, edad, n)