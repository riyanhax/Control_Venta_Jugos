'''
2. En el prestigioso colegio “El arca de Noé” estudian 1935 estudiantes. Allí solo cursan 5
asignaturas y solo hay tres cursos 6,7 y 8 de cada uno se ha registrado la siguiente
información correspondiente al segundo bimestre: Código del estudiante, curso, nota
asignatura 1, nota asignatura 2, nota asignatura 3, nota asignatura 4, nota asignatura 5.
Usted debe hacer un hacer un programa que ( Duván jaimes)
permita establecer:
 El promedio de cada estudiante.
 El promedio de cada curso
 El código del mejor estudiante del colegio
 El promedio general del colegio
 Imprimir en orden descendente los cursos de acuerdo al promedio que se obtuvo en cada
uno de ellos
'''

from random import randint,uniform

def matriz():
    datos = []
    for i in range(0, 9999):
        v = [0] * 7
        datos.append(v)
    return datos
def llenar(dato, num):
    for i in range(num):
        dato[i][0] = randint(29999999,199999999)
        dato[i][1] = randint(6,8)
        for j in range(2,7):
            dato[i][j] = uniform(1,5)
        if i > 0:
            j = 0
            while j < i:
                j += 1
                if dato[j-1][0] == dato[i][0]:
                    dato[i][0] = randint(29999999, 199999999)
                    j = 0
def PromEst(dato,num):
    sum = 0
    quien = 0
    masalta = 0
    vecpromest = []
    for i in range(num):
        for j in range(2, 7):
            sum += dato[i][j]
        prom = round((sum/5),2)
        sum = 0
        if i >= 1:
            if prom > masalta:
                masalta = prom
                quien = dato[i][0]
        else:
            masalta = prom
        vecpromest.append(prom)
    return vecpromest, masalta, quien
def PromCur(dato,num):
    sum1 = 0
    sum2 = 0
    sum3 = 0
    cont1 = 0
    cont2 = 0
    cont3 = 0
    for i in range(num):
        for j in range(2, 7):
            if dato[i][1] == 6:
                sum1 += dato[i][j]
                cont1 += 1
            elif dato[i][1] == 7:
                sum2 += dato[i][j]
                cont2 += 1
            elif dato[i][1] == 8:
                sum3 += dato[i][j]
                cont3 += 1
    sum1 = round((sum1/cont1),2)
    sum2 = round((sum2/cont2),2)
    sum3 = round((sum3/cont3),2)
    vecpromcur = [sum1,sum2,sum3]
    return vecpromcur
def promgen(promcur,num):
    sum = 0
    for i in range(num):
        sum += promcur[i]
    prom = round((sum/num),2)
    return prom
def ordenar(sal,n):
    x = [6,7,8]
    for i in range(0, len(sal)):
        for j in range(i + 1, len(sal)):
            if (sal[i] < sal[j]):
                temp = sal[i]
                sal[i] = sal[j]
                sal[j] = temp

                temp = x[i]
                x[i] = x[j]
                x[j] = temp
    return sal,x
while True:
    num = int(input(f'Numero de estudiantes (20-9999):'))
    if num >= 20 and num <= 9999:
        break
    else:
        print('Numero no valido!')
dato = matriz()
llenar(dato,num)
promest,masalta,quien = PromEst(dato,num)
promcur = PromCur(dato,num)
promgene = promgen(promcur,3)
prom,curso = ordenar(promcur,num)

print(f'|--------------------------------------------------|\n'
      f'| No |   |    Codigo  |      |Peomedio|    | Curso |\n'
      f'|--------------------------------------------------|')
for i in range(num):
    print(f'{"|%4s|" %(i+1)}   {"|%12s" %dato[i][0]}|  ==  {"|%8s" %promest[i]}|    {"|%4s" %dato[i][1]}   |\n'
          f'|--------------------------------------------------|')
print(f'\n|===========================================|')
for i in range(0,3):
    print(f' |       Curso = {"%2s" % (i+6)}  Promedi = {"%4s" %promcur[i]}        |')
print(f'|===========================================|\n')
print(f'\n|==============================================|\n'
      f' | El promedio general del colegio es de {"%4s" %promgene} |\n'
      f'|==============================================|\n')
print('\n|------------------|')
print('| Curso | Promedio |')
for i in range(len(promcur)):
    print("|%4s" % curso[i],'  |',"%6s" %prom[i], '  |')
print('|------------------|')
print('\n-------------------------------------------------------------------------')