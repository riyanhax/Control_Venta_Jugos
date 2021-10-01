'''
5. Una fábrica de bombas hidráulicas tiene una matriz con los insumos necesarios para la
    producción de un conjunto de motores. (Yordan Tarazona)
    Por ejemplo, suponiendo que la planta produce 7 motores y se utilizan 8 insumos en
    diferentes cantidades para su producción, la matriz sería:
    Capturar por teclado el número m de motores que fabrica la planta (máximo 50).-------
     Capturar por teclado el numero n de insumos necesarios para la fabricación de los-------
        motores (máximo 50).
     Capturar por teclado los datos de la matriz de Insumos/Motor.------------------
     Capturar por teclado los datos del arreglo de costos unitarios de insumos.------
     Capturar por teclado los datos del arreglo de pedidos del mes de cada motor.--------------------
     Capturar por teclado los datos del arreglo de insumos existentes en la planta.
     Obtener e imprimir un arreglo de m elementos, con el costo de producción de cada motor.
        Suponga que el costo de producción de un motor consiste en sumar el producto de insumos
        necesarios por el costo unitario de cada insumo.
     Obtener e imprimir un arreglo de n elementos, con la cantidad de unidades de cada
        insumo, necesaria para cumplir con los pedidos del mes.
     Obtener e imprimir un arreglo de n elementos, cuyos datos indiquen cual es el costo
        total por concepto de cada insumo para cumplir con los pedidos del mes.
     Obtenga e imprima el costo total (tomando en cuenta todos los insumos) para cumplir con
        la producción del mes.
     Obtenga e imprima un arreglo de n elementos, con la diferencia de los insumos necesarios
        para la producción mensual menos los insumos existentes en la planta, con el fin de poder
        surtir dichos insumos a tiempo.
'''

from random import randint, uniform
import time

def Matriz():
    matriz = []
    for i in range(0, 10):
        vecaux = [0] * 8
        matriz.append(vecaux)
    return matriz
def generainfo(M):
    for i in range(0,7):
        for j in range(0,8):
            M[i][j] = randint(0,50)
def vecped(n):
    vecped = [0]*n
    for i in range(0,n):
        vecped[i] = randint(0,100)
    return vecped
def vecuni(n):
    vecuni = [0] * n
    for i in range(0,n):
        v = uniform(1,5)
        vecuni[i] = round(v,1)
    return vecuni
def vecstk(n):
    vecstk = [0] * n
    for i in range(0, n):
        vecstk[i] = randint(1, 500)
    return vecstk
def veccos(M,VU):
    sumin = 0
    sumva = 0
    veccos = []
    for i in range(0,8):
        sumva += VU[i]
    for i in range(0, 7):
        for j in range(0, 8):
            sumin += M[i][j]
        veccos.append(round((sumin*sumva),2))
        sumin = 0
    return veccos
def vecinsmes(M,Vped):
    sumT = 0
    aux = []
    vecinsmes = Matriz()
    for i in range(0,7):
        cant = Vped[i]
        for j in range(0,8):
            sumT += M[i][j]*cant
            vecinsmes[i][j] = M[i][j] * cant
        aux.append(sumT)
        sumT = 0
    return vecinsmes,aux
def vecinscos(M,Vuni,Vped):
    sumT = 0
    aux1 = []
    for i in range(0, 8):
        for j in range(0, 7):
            sumT += (M[j][i] * Vped[j] * Vuni[i])
        aux1.append(sumT)
        sumT = 0
    return aux1

matriz = Matriz()
generainfo(matriz)
vped = vecped(7)
vuni = vecuni(8)
vstk = vecstk(8)
vcos = veccos(matriz,vuni)
vinsmes,aux = vecinsmes(matriz,vped)
vinscos = vecinscos(matriz,vuni,vped)


print(f'\n                                  INSUMOS            \n'
      f'                  |---------------------------------------|\n'
      f'                  |1   |2   |3   |4   |5   |6   |7   |8   |')
for i in range(0,7):
    print('                  |---------------------------------------|')
    print(f'Motor No. ({i+1})',end=" --> ")
    for j in range(0, 8):
        print("|%4s" %matriz[i][j],end="")
    print('|')
print('                  |---------------------------------------|\n')
time.sleep(0.5)
print(f'   PEDIDOS DE CADA MOTOR POR MES       ')
print(f'|----------------------------------|\n'
      f'|1   |2   |3   |4   |5   |6   |7   | Motor \n'
      f'|----------------------------------|')
for i in range(0,7):
    print("|%4s" % vped[i], end="")
print('| Cantidad \n'
      '|----------------------------------|\n')
time.sleep(0.5)
print(f'        VALOR UNITARIO DE INSUMO       ')
print(f'|---------------------------------------|\n'
      f'|1   |2   |3   |4   |5   |6   |7   |8   | Insumo \n'
      f'|---------------------------------------|')
for i in range(0,8):
    print("|%4s" % vuni[i], end="")
print('| Valor \n'
      '|---------------------------------------|\n')
time.sleep(0.5)
print(f'        EXISTENCIA DE INSUMOS       ')
print(f'|---------------------------------------|\n'
      f'|1   |2   |3   |4   |5   |6   |7   |8   | Insumo \n'
      f'|---------------------------------------|')
for i in range(0,8):
    print("|%4s" % vstk[i], end="")
print('| Existencia \n'
      '|---------------------------------------|\n')
time.sleep(0.5)
print(f'                        VALOR UNITARIO POR MOTOR       ')
print(f'|----------------------------------------------------------------------------|\n'
      f'|     1    |     2    |     3    |     4    |     5    |     6    |     7    | Motor \n'
      f'|----------------------------------------------------------------------------|')
for i in range(0,7):
    print("|%10s" % vcos[i], end="")
print('| Valor \n'
      '|----------------------------------------------------------------------------|\n')
time.sleep(0.5)
print(f'                                         INSUMOS PARA CUMPLIR LOS PEDIDOS       ')
print(f'                    Total  |-------------------------------------------------------|\n'
      f'                   Insumos |  1   |  2   |  3   |  4   |  5   |  6   |  7   |  8   | Insumo \n'
      f'                      v    |--v------v------v------v------v------v------v------v---|')
for i in range(0,7):
    print('                   |---------------------------------------------------------------|')
    print(f'Motor No. ({i + 1}) --> ', "|%6s" % aux[i], end=" ")
    for j in range(0,8):
        print("|%6s" %vinsmes[i][j], end="")
    print('| X Mes ')
print('                   |---------------------------------------------------------------|\n'
      '                     X Mes ')
time.sleep(0.5)
print(f'\n                  INSUMOS PARA COSTO TOTAL POR CONCEPTO       ')
print(f'|-----------------------------------------------------------------------|\n'
      f'|    1   |    2   |    3   |    4   |    5   |    6   |    7   |    8   | Insumo \n'
      f'|-----------------------------------------------------------------------|')
for i in range(0,8):
    print("|%8s" % round(vinscos[i],1), end="")
print('| Costo total por concepto')
print(f'|-----------------------------------------------------------------------|\n')




