'''
La nota final de un estudiante de Programación, se compone de los siguientes porcentajes: 60% Examen, 25% Quices y 15% Trabajos.
 Las calificaciones corresponden a números decimales entre 0 y 5. (validar que la nota este entre 0 y 5)
 Hacer una función que conociendo las tres calificaciones retorne la definitiva
 Hacer otra función que conociendo las notas de Quices y trabajos retorne la nota que debe sacar en el examen para aprobar la materia con la nota mínima de 3.0.
Genere una función para mejorar el ejercicio.
'''
def loquefalta(n1, n2):
    notaexa = 3.0 - (n1 + n2)
    return notaexa
def calnota(n1, n2, n3):
    no1 = (n1 * 0.15)
    no2 = (n2 * 0.25)
    no3 = (n3 * 0.60)
    totalnot = no1 + no2 + no3
    return totalnot
opc = int(input(f'[1] proceso completo de notas, [2] proceso solo de nota minima. Opción ='))
if opc == 1:
    print("Cual es la nota definitiva de los Exmenes sabiendo que equivalen al 60% :")
    notaexamen = float(input())
    print("Cual es la nota definitiva de los Quices sabiendo que equivalen al 25% :")
    notaquiz = float(input())
    print("Cual es la nota definetiva de los trabajos sabiendo que equivalen al 15% :")
    notatrabajos = float(input())
    if notaquiz < 0 or notaexamen < 0 or notatrabajos < 0 or notaquiz > 5 or notaexamen > 5 or notatrabajos > 5:
        print(f'Error!, porfavor verifique q las notas sean >= 0 , <= 5')
    else:
        a = calnota(notatrabajos, notaquiz, notaexamen)
        lanota = "la nota definitiva es de : "
if opc == 2:
    print("Cual es la nota definitiva de los Quices sabiendo que equivalen al 25% :")
    notaquiz = float(input())
    print("Cual es la nota definetiva de los trabajos sabiendo que equivalen al 15% :")
    notatrabajos = float(input())

    if notaquiz < 0 or notatrabajos < 0 or notaquiz > 5 or notatrabajos > 5:
        print(f'Error!, porfavor verifique q las notas sean >= 0 , <= 5')
    else:
        a = loquefalta(notatrabajos, notaquiz)
        lanota = "la nota minima debe ser de : "
print(lanota,a)