'''
Almacenar la informacion de n empleados :
codigo(4 digitos), edad(18-60), grupo sanguineo (1-8) y salario
la informacion es de tipo entero, dada por teclado
Tipos de sangre
1. A+  2. A-
3. B+  4. B-
5. AB+ 6. AB-
7. O+  8. O-
Hacer las siguientes funciones:
-Llenar: Validar la informacion. Codigo de 4 digitos y que NO hallan repetidos.
 La edad este entre 17 y 60, el tipo de sangre mayor a 1 y menor 9.
-Imprimir: Muestra la informacion siguiendo el siguiente modelo:
|=======================================|
|         DATOS DE LOS EMPLEADOS        |
|=======================================|
| No | Codigo | Edad | Salario | Sangre |
|----+--------+------+---------+--------|
| 1  |  1234  | 23   | 2300000 |    A-  |
|----+--------+------+---------+--------|
| 2  |  1235  | 25   |  800000 |    A+  |
|---------------------------------------|
-Informacion del empleado de mayor salario
-Ordenar (mayor a menor ) con base en el salario en forma paralela
-Cantidadxtipo: Mustra cuantos empleados hay de cada tipo de sangre.
-Donar: Solicitar el tipo de sangre y mostrar el listado de los
        donadores, siguiendo el siguient modelo.
|=======================================|
|   EMPLEADOS CANDIDATOS A DONACION     |  Preguntar el tipo de
 =======================================   Sangre. Existen tres
    | No | Codigo | Edad | Condicion |     Condiciones de donador
    |----+--------+------+-----------|     - Muy Joven <18
    | 1  |  1234  | 23   | Donante   |     - Muy Viejo >40
    |----+--------+------+-----------|     - Donador ( mayor 18 y menor de 40 años)
    | 2  |  1235  | 45   | Muy viejo |
    |---------------------------------|
-Nomina: Determina cuanto vale pagar el salario de todos los empleados , mostrar el salario promedio y el promedio de
         edad de los empleados.
'''
def mostrar(cod, ed, tips, val, canti, info, cond):
    if cond == 1:
        print("\n|============================================|")
        print(f"|       {info}             |")
        print("|============================================|")
        print("| No |  Codigo  |  Edad  | Salario  | Sangre |")
        for i in range(0, canti):
            men = "| " + '{:>2s}'.format(str(i + 1)) + " | "
            men = men + '{:>9s}'.format(str(cod[i])) + "| "
            men = men + '{:>7s}'.format(str(ed[i])) + "| "
            men = men + '{:>8s}'.format(str(val[i])) + " | "
            men = men + '{:>7s}'.format(str(tips[i])) + "| "
            print("|----+----------+--------+----------+--------|")
            print(men)
        print("|--------------------------------------------|")
    elif cond == 2:
        quien = mayorsalario(z, cuanto)
        print("\n|============================================|")
        print(f"|       {info}            |")
        print("|============================================|")
        print("| No |  Codigo  |  Edad  | Salario  | Sangre |")
        men = "| " + '{:>2s}'.format(str(1)) + " | "
        men = men + '{:>9s}'.format(str(cod[quien])) + "| "
        men = men + '{:>7s}'.format(str(ed[quien])) + "| "
        men = men + '{:>8s}'.format(str(val[quien])) + " | "
        men = men + '{:>7s}'.format(str(tips[quien])) + "| "
        print("|----+----------+--------+----------+--------|")
        print(men)
        print("|--------------------------------------------|")
    elif cond == 3:
        print("\n|==============================================|")
        print(f"|     EMPLEADOS CANDIDATOS A DONACION          |")
        print("|==============================================|")
        print("| No |  Codigo  |  Edad  |  Condicion | Sangre |")
        for i in range(0, canti):
            conded = validarcondicion(ed[i])
            men = "| " + '{:>2s}'.format(str(i + 1)) + " | "
            men = men + '{:>9s}'.format(str(cod[i])) + "| "
            men = men + '{:>7s}'.format(str(ed[i])) + "| "
            men = men + '{:>10s}'.format(str(conded)) + " | "
            men = men + '{:>7s}'.format(str(tips[i])) + "| "
            print("|----+----------+--------+------------+--------|")
            print(men)
        print("|----------------------------------------------|")
def ordenar(cod, ed, tips, valor, n, cond):
    for i in range(0,n):
        for j in range(i+1,n):
            if cond == 1:
                if (cod[i] > cod[j]):
                    aux = valor[i]
                    valor[i] = valor[j]
                    valor[j] = aux
                    aux = cod[i]
                    cod[i] = cod[j]
                    cod[j] = aux
                    aux = ed[i]
                    ed[i] = ed[j]
                    ed[j] = aux
                    aux = tips[i]
                    tips[i] = tips[j]
                    tips[j] = aux
            elif cond == 2:
                if (valor[i] < valor[j]):
                    aux = valor[i]
                    valor[i] = valor[j]
                    valor[j] = aux
                    aux = cod[i]
                    cod[i] = cod[j]
                    cod[j] = aux
                    aux = ed[i]
                    ed[i] = ed[j]
                    ed[j] = aux
                    aux = tips[i]
                    tips[i] = tips[j]
                    tips[j] = aux
def tiposangre(dato):
    res = ''
    if dato == 1:
        res = 'A+'
    elif dato == 2:
        res = 'A-'
    elif dato == 3:
        res = 'B+'
    elif dato == 4:
        res = 'B-'
    elif dato == 5:
        res = 'AB+'
    elif dato == 6:
        res = 'AB-'
    elif dato == 7:
        res = 'O+'
    elif dato == 8:
        res = 'O+'
    return res
def buscar(dato, vect):
    for i in range(0, len(vect)-1):
        if dato == vect[i]:
            return 1
def validarcod(dato, i):
    while dato < 1000:
        print('Los codigos deben ser de 2 cifras.')
        dato = int(input(f'Escriba el codigo No.{i + 1} -->'))
    return 1, dato
def validaredad(dato, i):
    while dato < 17 or dato > 60:
        print('La empleado debe ser mayor d edad.')
        dato = int(input(f'Edad del empleado No.{i+1} -->'))
    return 1, dato
def validartipsan(i):
    tip = int(input(f'Tipo de sangre del empleado No.{i+1} -->'))
    while tip < 1 or tip > 8:
        print('Tipo de sangre debe estar entre 1 y 8.')
        tip = int(input(f'Tipo de sangre del empleado No.{i+1} -->'))
    auxtipsan = tip
    tiposan = tiposangre(tip)
    return tiposan, auxtipsan
def mayorsalario(val,n):
    pos = 0
    may=val[0]
    for i in range(0,n):
        if(v[i]>may):
            may=v[i]
            pos = i
    return pos
def validarcondicion(ed):
    if ed < 18:
        res = 'Muy Joven'
        return res
    elif ed > 40:
        res = 'Muy Viejo'
        return res
    elif ed >= 18 and ed <= 40:
        res = 'Donante'
        return res
def llenar(canti):
    cod = []
    ed = []
    tipsan = []
    val = []
    auxtipsan = []
    for i in range(0, canti):
        cod.append(int(input(f'Escriba el codigo del empleado No.{i+1} -->')))
        a, b = validarcod(cod[i], i)
        if a == 1:
            cod.pop(i)
            cod.append(b)
        if i >= 1:
            while True:
                res = buscar(cod[i], cod)
                if res == 1:
                    print(f'El codigo {cod[i]} ya se encuentra.')
                    cod.pop(i)
                    cod.append(int(input(f'Escriba el codigo del empleado No.{i + 1} -->')))
                else:
                    break
        ed.append(int(input(f'Edad del empleado No.{i+1} -->')))
        a = validaredad(ed[i], i)
        if a == 1:
            cod.pop(i)
            cod.append(a)
        a , b = validartipsan(i)
        tipsan.append(a)
        auxtipsan.append(b)
        val.append(int(input(f'Salario del empleado No. {i+1} -->')))
    return cod, ed, tipsan, val, auxtipsan
def validarcantsangre(tispan, n):
    for i in range(1, n):
        cantidad = tispan.count(i)
        print(f'Tipo {tiposangre(tispan[i])} son: {cantidad}')
def total(z):
    sum = 0
    for i in range(0, len(z)):
        sum += z[i]
    prom = sum / len(z)
    return sum, prom
def validarpromed(ed):
    sum = 0
    for i in range(0, len(ed)):
        sum += ed[i]
    prom = sum / len(ed)
    return prom
while True:
    cuanto = int(input(f'Cuantos empleados son -->'))
    v, x, y, z, aux= llenar(cuanto)
    ordenar(v, x, y, z, cuanto, 1)
    inf1 = 'DATOS DE LOS EMPLEADOS  '
    mostrar(v, x, y, z, cuanto, inf1, 1)
    print('***************************************************')
    ordenar(v, x, y, z, cuanto, 2)
    inf2 = 'DATOS DE LOS EMPLEADOS X SALARIO'
    mostrar(v, x, y, z, cuanto, inf2, 1)
    print('***************************************************')
    inf3 = 'EMPLEADO DE MAYOR SALARIO'
    mostrar(v, x, y, z, 1, inf3, 2)
    print('***************************************************')
    mostrar(v, x, y, z, cuanto, 0, 3)
    validarcantsangre(aux, cuanto)
    a, b = total(z)
    print(f'El total es de: ${a}\n'
          f'El promedio es: ${b}')
    print(f'La edad promedio es de --> {validarpromed(x)}')
    print('***************************************************')
    pre = str(input(f'Desea continuar s/n --> '))
    if pre == 'N' or pre == 'n':
        break
print(f'Ten un buen resto de dia :)')