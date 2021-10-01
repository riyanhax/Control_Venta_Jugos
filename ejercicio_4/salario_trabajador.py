"""
4. Un empleado trabajar 40 horas semanales en una empresa y recibe un salario de 260.000 pesos semanales.
Si excede de las 40 horas la empresa debe pagar un recargo del 30% por hora extra trabajada. Hacer un programa
que dadas las horas semanales trabajadas de un empleado, retorne el salario a pagar según las condiciones anteriores.
"""
def calculo(horastr, minutr):
    if horastr == 40 and minutr == 0:
        print("El salrio del empleado es de : $260.000")
    elif horastr < 40:
        salariom = (minutr / 60)
        salarioh = ((horastr + salariom) * 260000) / 40
        print("El salario del empleado es de : $", salarioh)
    else:
        salariom = (minutr / 60)
        horastotal = horastr + salariom
        salrioext = ((30 * 260000) / 100) * (horastotal - 40)
        print("El salario del empleado es de : $", salrioext + 260000)
print('Digite las horas trabajadas del empeado :')
horastr = int(input("->"))
print("Con cunatos minutos : ")
minutr = int(input("->"))
calculo(horastr, minutr)