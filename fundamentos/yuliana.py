'''
En una empresa se piensa contratar a máximo 20 empleados, de los cuales se
necesita saber la cédula, edad y salario a que aspira, datos que serán
almacenados en tres vectores paralelos. Dada la cantidad de candidatos a
contratar por teclado (no sobrepasar de 20), introducir los datos de cada
uno.
Si el candidato es menor a 30 años y aspira un salario entre 500.000 y
800.000 este se puede contratar. Se debe tener en cuenta que quienes reciban
un salario menor a 600.000 tendrán una bonificación de 5% de su salario.
Haga un programa en Python con uso de funciones que permita al final saber:
* Cuantos pueden ser contratados según el salario a que aspiran-----------------------------
* El total de la nómina que debe pagar la empresa, según los posibles
 contratados.---------------------------------------
* Cuantos de los posibles contratados tienen bonificación------------------------------------
* Cual de los posibles contratados tiene mayor edad.----------------------------------------
* En la función principal además debe imprimir la información de cada uno
de los posibles contratados (cédula, edad, salario) con su correspondiente
bonificación

'''
def mayed(edad):
    if edad > 17:
        return 1
    else:
        return 0
def contratar(edad, salario):
    bonifica = 0
    if edad < 30 and (salario >= 500000 and salario <= 800000):
        if salario >= 500000 and salario < 600000:
            bonifica += (salario*5)/100
        return 1, bonifica
    else:
        return 0, bonifica
def max20(num):
    if num <= 20:
        return 1
    else:
        return 0
def llenar(canti):
    cedula = []
    edad = []
    salario = []
    maxnum = max20(canti)
    while maxnum != 1:
        print('Dato no valido.')
        canti = int(input(f'Cuantos empleados son -->'))
        maxnum = max20(canti)
    for i in range(0, canti):
        cedula.append(int(input(f'Escriba el numero de la cedula No.{i+1} -->')))
        edad.append(int(input(f'Edad del empleado No.{i+1} -->')))
        salario.append(int(input(f'Salario del empleado No. {i + 1} -->')))
    return cedula, edad, salario
def contar(cedula, edad, salario):
    cuantaspi = 0
    cuantboni = 0
    cuantmayed = 0
    sumsalario = 0
    aprov = []
    boni = []
    for i in range(0, len(cedula)):
        contra, bonif = contratar(edad[i], salario[i])
        mayored = mayed(edad[i])
        if contra == 1:
            cuantaspi += 1
            if mayored == 1:
                if bonif > 0:
                    cuantboni += 1
                cuantmayed += 1
                aprov.append('Si')
            elif mayored == 0:
                aprov.append('No')
            boni.append(bonif)
            sumsalario += salario[i] + cuantboni
        elif contra == 0:
            aprov.append('No')
            boni.append(bonif)
    return cuantaspi,cuantmayed, cuantboni, sumsalario, aprov, boni
def pantall(cedula, edad, salario, aprov, boni):
    print("\n|=======================================================|")
    print(f"|                      INFORMACIÓN                      |")
    print("|=======================================================|")
    print("| No |  Codigo  |  Edad  | Salario  | bonifica | Aprov. |")
    for i in range(0, len(cedula)):
        men = "| " + '{:>2s}'.format(str(i + 1)) + " | "
        men = men + '{:>9s}'.format(str(cedula[i])) + "| "
        men = men + '{:>7s}'.format(str(edad[i])) + "| "
        men = men + '{:>8s}'.format(str(salario[i])) + " | "
        men = men + '{:>8s}'.format(str(boni[i])) + " | "
        men = men + '{:>7s}'.format(str(aprov[i])) + "| "
        print("|----+----------+--------+----------+----------+--------|")
        print(men)
    print("|-------------------------------------------------------|")
canti = int(input(f'Cuantos empleados son -->'))
v, x, y = llenar(canti)
aspi, maed, boni, sum, aprov, bonific = contar(v, x, y)
pantall(v, x, y, aprov, bonific)
print(f'cuantos segun salario "{aspi}"\n'
      f'cuantos segun edad "{maed}"\n'
      f'cuantos con bonificaón "{boni}"\n'
      f'El total de la nómina es de "{sum}"')