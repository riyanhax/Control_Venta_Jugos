'''La biblioteca del iser  tiene sistematizado el total de libros que posee, y desea que usted cree un
programa que ayude en el control de préstamos y recolección de libros, la cantidad de personas que visitan la biblioteca
es indeterminada de ellos se conoce: Tipo de Servicio (1. Préstamo (Llevarse el libro para la casa) o 2. Entrega) y el
código del libro.
El proceso de préstamo y recolección termina cuando el tipo de servicio es 0.
Realice un programa que lea el tipo de servicio y el código del libro y si es un código debe determinar si se puede
prestar el libro o el valor a cobrar por los libros prestados (según el tipo de servicio solicitado) y al final imprimir
el total recaudado por prestamos de libros.
El código del libro está compuesto por 8 dígitos donde los tres primeros representan el área del Libro, los siguientes
dos la cantidad de libros que existen y los últimos 3 el identificador del libro.
Ej: Para el código 10105153
El área es 101 la cantidad de libros es 05 y su código de identificación es 153
Realice:
 Main()
 Función Validar código: Debe recibir el código del libro y este debe cumplir: ser un número de 8 dígitos, el área debe
estar entre 101 y 108 y la cantidad debe ser diferente de 0. Si cumple debe retornar un 1(uno), si no cumple debe
retornar un 0 (cero).
 Función Préstamo: La función debe recibir el código del libro y solo se pueden prestar libros del área 101, 102 y
104. La función debe retornar 1 (uno) si se puede prestar o 0 (cero) si no se puede realizar el préstamo
 Función Recolección: La función debe recibir el código del libro y dependiendo de la cantidad de ejemplares
disponibles se cobra un valor al usuario según la siguiente tabla, debe retornar el valor que se debe cobrar
Cantidad de ejemplares existentes Valor del servicio de préstamo
1 a 2 $2.000
3 a 6 $1.000
Mas de 6 $500
'''
def inver(x):
    cont1 = 0
    while x > 0:
        quita = x % 10
        cont1 = (cont1 * 10) + quita
        x //= 10
    return cont1
def valcod(num):
    codcan = 0
    codide = 0
    i = 0
    j = 0
    while i <= 2:
        quita = num % 10
        codide = (codide * 10) + quita
        num //= 10
        i = i + 1
    while j <= 1:
        quita = num % 10
        codcan = (codcan * 10) + quita
        num //= 10
        j = j + 1
    are = num
    can = inver(codcan)
    ide = inver(codide)
    if are > 100 and are < 109 and can != 0:
        return are, can, ide
    else:
        return 0
def prestamo(area):
    if area > 100 and area < 105:
        return 1
    else:
        return 0
def recol(cant):
    if cant > 0 and cant < 3:
        r = 2000
    elif cant > 2 and cant < 7:
        r = 1000
    else:
        r = 500
    return r
libro = int(input(f'ingrese el numero del libro que desea --> '))
while True:
    a, b, c = valcod(libro)
    res = int(input(f'[1] para prestamo, [0] para continuar.'))
    if res == 1:
        e = recol(b)
        d = prestamo(a)
        if d == 1:
            print(f'el libro "{libro} si puede ser pretado con un valor de "${e}" ')
        elif d == 0:
            print(f'el libro "{libro}" No puede ser prestado.')
    libro = int(input(f'ingrese el numero del libro que desea para continuar o [0] para salir --> '))
    if libro == 0:
        break
print(f'Gracias por usar nuestro servicio.')

