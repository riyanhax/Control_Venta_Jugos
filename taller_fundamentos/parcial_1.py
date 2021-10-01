'''
En una empresa de telefonía, solo por el día de hoy, se esta ofreciendo una
promoción de acceso a Internet, consistente en lo siguiente: Las tarifas
mensuales normales (sin descuento) dependen del tipo de acceso y del estrato
así:                    _________________________
                       |          Estrato?       |
 ----------------------+-------------------------|
|  Tipo de acceso      | Del 1 al 3 | Del 4 al 6 |
|----------------------+------------+------------|
| 1. Internet Fácil    |  65.000    |  82.000    |
| 2. Internet Familiar |  75.000    |  97.000    |
| 3. Internet Extremo  |  85.000    | 120.000    |
|----------------------+------------+------------|

Según el número de teléfono de la línea por la que se accede a Internet, se
ofrece un descuento igual al número de dos cifras formado por los primeros
dígitos impares. Por ejemplo si el número es 5681232 el primer digito impar es
3 y el siguiente es 1 por lo tanto se obtuvo el número 31 y este será el
descuento a aplicar. Si el número telefónico no tiene dígitos impares entonces
el porcentaje de descuento se obtiene buscando el tercer digito y multiplicando
por 10.

  Implementar las siguientes funciones
* Función tienedigitosimpares (N) que retorne 1 si el número dado como parámetro
  tiene dígitos impares y 0 si no tiene dígitos impares
* Función extraer(num) que retorna un número de máximo dos cifras, conformado
  por los primeros 2 dígitos impares del número dado como parámetro, si el
  número solo tiene un digito impar debe retornar este.
  Ejemplos: extraer(5683145) retorna 51 y extraer(8682144) retorna 1
* Función, digito(N,num) que retorne el dígito N-ésimo de un número num de tipo
  entero largo, teniendo en cuenta que el dígito 0 es el dígito más a la derecha
  (el menos significativo). La función devolverá -1 si el número no tiene
  suficientes dígitos.
  Ejemplos:
  digito (0,233456) retorna 6
  digito (1,43456) retorna 5
  digito (4,3456) retorna -1
* Función cuotamensual(telefono, tipoacceso, estrato) que recibe como parámetros
  el número de la línea telefónica, el tipo de acceso que se desea contratar y
  el estrato residencial del cliente, para retornar el valor de la cuota mensual
  según las condiciones de la promoción (haga uso de las funciones implementadas
  anteriormente).

* En el main hay que construir el código necesario para atender a una fila de
  clientes que acudieron a la empresa a comprar el acceso de Internet (no se
  sabe cuantos clientes hay, el proceso termina cuando el numero telefónico
  tecleado sea cero). De igual manera en el main se debe imprimir cuanto dinero
  recibirá mensualmente la empresa por las ventas realizadas en el día de hoy
  que se ofreció la promoción.
* Realizar una función que considere necesaria para mejorar el ejercicio
'''
import time
def mostrar():
    cuota, descu, tel = cuotamensual(tele, tipo, estr)
    print(f'La cuota mensual del cliente con el numero --> {tel} es de --> ${cuota+descu} \n'
          f'se le descuentan por la promocion --> $-{descu} para un total de --> ${cuota}')
    return cuota
def tienedigitosimpares(N):
    r = 0
    while N > 0:
        quita = N % 10
        N //= 10
        if quita % 2 != 0:
            r = r + 1
    if r >= 1:
        return 1
    elif r == 0:
        return 0
def extraerimp(num):
    r = 0
    i = 0
    while num > 0:
        quita = num % 10
        num //= 10
        if quita % 2 != 0 and i <= 1:
            r = (r * 10) + quita
            i = i + 1
    return r
def extraerpar(num):
    r = 0
    i = 0
    while num > 0:
        quita = num % 10
        num //= 10
        i = i + 1
        if i == 3:
            r = quita * 10
    return r
#def digito(N,num):
def cuotamensual(telefono, tipoacceso, estrato):
    dig = tienedigitosimpares(telefono)
    if dig == 1:
        d = extraerimp(telefono)
    elif dig == 0:
        d = extraerpar(telefono)
    if tipoacceso == 1:
        if estrato >= 1 and estrato <= 3:
            cuotamen = 65000 - d
        elif estrato >= 4 and estrato <= 6:
            cuotamen = 82000 - d
    elif tipoacceso == 2:
        if estrato >= 1 and estrato <= 3:
            cuotamen = 75000 - d
        elif estrato >= 4 and estrato <= 6:
            cuotamen = 97000 - d
    elif tipoacceso == 3:
        if estrato >= 1 and estrato <= 3:
            cuotamen = 85000 - d
        elif estrato >= 4 and estrato <= 6:
            cuotamen = 120000 - d
    return cuotamen, d, telefono
print(f'                        _________________________\n'
f'                       |          Estrato?       |\n'
f'|----------------------+-------------------------|\n'
f'|  Tipo de acceso      | Del 1 al 3 | Del 4 al 6 |\n'
f'|----------------------+------------+------------|\n'
f'| [1] Internet Fácil    |  65.000    |  82.000   |\n'
f'| [2] Internet Familiar |  75.000    |  97.000   |\n'
f'| [3] Internet Extremo  |  85.000    | 120.000   |\n'
f'|----------------------+------------+------------|\n')
cont = 0
i = 0
j = 0
while True:
    i = i + 1
    tele = int(input(f'Porfavor ingrese el numero de telefon -->'))
    tipo = int(input(f'Tipo de acceso q desea -->'))
    estr = int(input(f'Cual es su estrato? -->'))
    tel = int(tele)
    while tel > 0:
        quita = tel % 10
        tel //= 10
        j = j + 1
    while j < 7 or j > 15 or tipo > 3 or tipo < 1 or estr < 1 or estr > 6:
        print(f'Porfavor verifique los datos.')
        if j < 7 or j > 15:
            tele = int(input(f'Porfavor ingrese el numero de telefon -->'))
            j = 10
        elif tipo > 3 or tipo < 1:
            tipo = int(input(f'Tipo de acceso q desea -->'))
        elif estr > 6 or estr < 1:
            estr = int(input(f'Cual es su estrato? -->'))
    mostrar()
    valor = mostrar()
    cont = cont + valor
    proc = str(input(f'Desea continuar con otro cliente s/n -->'))
    if proc == 'N' or proc == 'n':
        break
print(f'El total de ventas es de --> "{i}"\n'
      f'El dinero que recibirá mensualmente es de --> ${cont}')
time.sleep(1)
print(f'Gracias por usar nuestros servicios.')
