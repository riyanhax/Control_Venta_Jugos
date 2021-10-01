'''
Se lee la información de 100 estudiantes, el código, la nota final, el
departamento (1. SISTEMA, 2. ELECTRÓNICA, 3.TELECOMUNICACIONES), y el
ciclo de formación al que pertenece (1 para los Primeros 5 semestres y 2
para los 5 últimos semestres).
Representando esta información en una matriz...
Se debe calcular e imprimir
* mostrar la información de todos los alumnos en forma de columna
* Cuantos estudiantes hay en cada departamento
* El código del estudiante o estudiantes con la nota final más alta
* El promedio de notas de los estudiantes de primer ciclo, y segundo
ciclo
* El listado de los alumnos que pasaron y los que perdieron un alumno
pierde si la nota es menor 3.0
* El promedio por departamento
'''

from random import randint, uniform

def Matriz():
    matriz = []
    for i in range(0, 100):
        vecaux = [0] * 8
        matriz.append(vecaux)
    return matriz

def generainfo(M):
    nombres=["Jorge ", "Miguel", "Jose ","Maria "," Marta","Magaly"]
    apellidos=["Rodriguez ","Sanchez ","Salamanca ","Cariongo ","Alvarez ","Malaguez "]
    departamento = ['SISTEMA','ELECTRÓNICA','TELECOMUNICACIONES']
    for i in range(0,100):
        M[i][1] = randint(10000,99999)       #cc
        M[i][2] = randint(1,2)               #sexo 1 hombre 2 mujer
        M[i][3] = randint(16, 29)            #edad
        M[i][4] = round(uniform(1,5),1)      #nota
        M[i][5] = departamento[randint(0,2)] #departamento
        M[i][6] = randint(1,2)               #ciclo
        if(M[i][1]==1):
          M[i][0] =nombres[ randint(0,2)]      # escoje entre 0, 1 o 2 que son nombres masculinos
        else:
          M[i][0] = nombres[randint(3, 5)]     # escoje entre 3, 4 o 5 que son nombres femeninos
        M[i][0] = M[i][0] + apellidos[randint(0,5)] + apellidos[randint(0,5)]
def pordepa(M):
    veccuan = [0]*3
    for i in range(0,100):
        if M[i][5] == 'SISTEMA':
            veccuan[0] += 1
        elif M[i][5] == 'ELECTRÓNICA':
            veccuan[1] += 1
        elif M[i][5] == 'TELECOMUNICACIONES':
            veccuan[2] += 1
    return veccuan
def notmas(M):
    aux = M[0][4]
    quien = Matriz()
    mayor = []
    for i in range(0,100):
        if M[i][4] > aux:
            aux = M[i][4]
            quien[0][0] = M[i][0]
            quien[0][1] = M[i][1]
    mayor.append(aux)
    j = 1
    for i in range(0,100):
        if aux == M[i][4] and quien[0][1] != M[i][1]:
            mayor.append(M[i][4])
            quien[j][0] = M[i][0]
            quien[j][1] = M[i][1]
            j += 1
    return mayor, quien
def promciclo(M):
    vecprom = []
    a1 = 0
    a2 = 0
    con1 = 0
    con2 = 0
    for i in range(0,100):
        if M[i][6] == 1:
            a1 += M[i][4]
            con1 += 1
        elif M[i][6] == 2:
            a2 += M[i][4]
            con2 += 1
    vecprom.append(round((a1 / con1),2))
    vecprom.append(round((a2 / con2),2))
    return vecprom
def Pasa(M):
    vecpasa = []
    vecnopasa = []
    for i in range(0,100):
        if M[i][4] >= 3:
            vecpasa.append(M[i][0])
        else:
            vecnopasa.append(M[i][0])
    return vecpasa,vecnopasa
def promdepa(M):
    vecprom = []
    a1 = 0
    a2 = 0
    a3 = 0
    con1 = 0
    con2 = 0
    con3 = 0
    for i in range(0,100):
        if M[i][5] == 'SISTEMA':
            a1 += M[i][4]
            con1 += 1
        elif M[i][5] == 'ELECTRÓNICA':
            a2 += M[i][4]
            con2 += 1
        elif M[i][5] == 'TELECOMUNICACIONES':
            a3 += M[i][4]
            con3 += 1
    vecprom.append(round((a1 / con1),2))
    vecprom.append(round((a2 / con2),2))
    vecprom.append(round((a3 / con3),2))
    return vecprom
m = Matriz()
generainfo(m)
print(f'\n                                      INFORMACION \n'
      f'\n'
      f'|             Nombres           |  CC   |Sexo|Edad|Nota |     Departamento     |Ciclo|\n'
      f'|-------------------------------|-------|----|----|-----|----------------------|-----|')
for i in range(0,100):
    print(f'|{"%30s" %m[i][0]} | {"%5s" %m[i][1]} | {"%2s" %m[i][2]} | {"%2s" %m[i][3]} | {"%3s" %m[i][4]} | '
          f'{"%20s" %m[i][5]} | {"%2s" %m[i][6]}  |')
    print(f'|-------------------------------|-------|----|----|-----|----------------------|-----|')
vcuan = pordepa(m)
print(f'\n          ESTUDIANTES POR DEPARTAMENTO \n'
      f'|    SISTEMA    |  ELECTRÓNICA  | TELECOMUNICACIONES |\n'
      f'|---------------|---------------|--------------------|')
for i in range(0,3):
    print(f'|{"%10s" %vcuan[i]}', end="     ")
print('     |\n'
      '|---------------|---------------|--------------------|\n')
mayor,quien = notmas(m)
print(f'                      MEJORES NOTAS\n'
      f'|            Nombres            | Codigo | Nota|\n'
      f'|-------------------------------|--------|-----|')
for i in range(0,len(mayor)):
    print(f'|{"%30s" %quien[i][0]} | {"%6s" %quien[i][1]} | {"%3s" %mayor[i]} |')
    print(f'|----------------------------------------------|')
vpromci = promciclo(m)
print(f'\n          PROMEDIO POR CICLO ')
print(f'Promedio del ciclo No. 1 --> {vpromci[0]}')
print(f'Promedio del ciclo No. 2 --> {vpromci[1]}')

pasa,nopasa = Pasa(m)
print('==========================================================\n')
print(f'        LOS QUE PASARON SON :\n')
for i in range(0,len(pasa)):
    print(f'{pasa[i]}')
print('==========================================================\n')
print(f'        LOS QUE NO PASARON SON :\n')
for i in range(0,len(nopasa)):
    print(f'{nopasa[i]}')

print('============================================================\n')
vpromdepa = promdepa(m)
print(f'            PROMEDIO POR DEPARTAMENTOS\n')
print(f'Promedio por depa (SISTEMA) --> {vpromdepa[0]}')
print(f'Promedio por depa (ELECTRONICA) --> {vpromdepa[1]}')
print(f'Promedio por depa (TELECOMUNICACIONES) --> {vpromdepa[2]}')