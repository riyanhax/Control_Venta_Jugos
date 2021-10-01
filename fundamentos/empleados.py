'''
Almacenar en 4  vectores la informacion corrrespondiente a:Nombre(string), Codigo(entero), salario(float) y edad(entero)
de los  n empleados de una empresa (n dado por teclado).
Crear las funciones necesarias para realizar las siguientes acciones:
> Llenar: Para recolectar la informacion de los empleados.
> Imprimir: Muestra la informacion de todos los empleados en forma de columnas.
> Mayor salario: Muestra el nombre del empleado que gana el mayor salario. Asuma que no hay empates.
> Ordenar: Ordena de forma paralela de menor a mayor los vectores tomando como referencia el vector de salarios.
> Promedio: Muestra el promedio de los salarios pagados en la empresa
'''
# ---------------------------------------------------
def llenar(nom, cod, eda, sal, n):
    for i in range(0, n):
        print("Informacion del Empleado No", i + 1)
        cod[i] = int(input("Codigo:"))
        nom[i] = input("Nombre:")
        eda[i] = int(input("Edad:"))
        sal[i] = float(input("Salario:"))
# ---------------------------------------------------
def imprimir(nom, cod, eda, sal, n):
    print("\t\t INFORMACION DE LOS EMPLEADOS\n Codigo  Nombre   Edad   Salario")
    for i in range(0, n):
        print(" %5d" % cod[i], "%5s" % nom[i], "%8d" % eda[i], "%8s" % sal[i])
# ---------------------------------------------------
def mayorsal(nom, sal, n):
    mayor = sal[0]
    quien = 0
    for i in range(1, n):
        if (sal[i] > mayor):
            mayor = sal[i]
            quien = i
    print("El empleado con mayor salario es: ", nom[quien], " con ", mayor)
# ---------------------------------------------------
def ordenar(nom, cod, eda, sal, n):
    for i in range(0, n):
        for j in range(i + 1, n):
            if (sal[i] < sal[j]):
                temp = sal[i]
                sal[i] = sal[j]
                sal[j] = temp

                temp = eda[i]
                eda[i] = eda[j]
                eda[j] = temp

                temp = cod[i]
                cod[i] = cod[j]
                cod[j] = temp

                temp2 = nom[i]
                nom[i] = nom[j]
                nom[j] = temp2
# ---------------------------------------------------
def promedio(sal, n):
    suma = 0.0
    for i in range(0, n):
        suma = suma + sal[i]
    pro = suma / n
    print("El promedio de los salarios de los empleados es: %.2f" % pro)
# ====================================================
n = int(input("Cantidad de empleados? "))
nombres = [" "] * n
codigos = [0] * n
edades = [0] * n
salarios = [0.0] * n

llenar(nombres, codigos, edades, salarios, n)
print("Informacion Original:")
imprimir(nombres, codigos, edades, salarios, n)
mayorsal(nombres, salarios, n)
ordenar(nombres, codigos, edades, salarios, n)
print("Informacion Ordenada por Salario:")
imprimir(nombres, codigos, edades, salarios, n)
promedio(salarios, n)
