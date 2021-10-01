'''
La nota final de un estudiante de Programación, se compone de los siguientes porcentajes: 60% Examen, 25% Quices y 15% Trabajos.
 Las calificaciones corresponden a números decimales entre 0 y 5. (validar que la nota este entre 0 y 5)
 Hacer una función que conociendo las tres calificaciones retorne la definitiva
 Hacer otra función que conociendo las notas de Quices y trabajos retorne la nota que debe sacar en el examen para aprobar la materia con la nota mínima de 3.0.
Genere una función para mejorar el ejercicio.
'''
import time
def completo(nota1, nota2, nota3):
    promediono3 = (nota3 * 0.60)
    promediono2 = (nota2 * 0.25)
    promediono1 = (nota1 * 0.15)
    promed = promediono3 + promediono2 + promediono1
    return promed
def minimo(nota1, nota2):
    nota3 = 3.0 - (nota1 + nota2)
    return nota3
print(f'Hola bienvenido 💪 (︡❛ ‿❛︠) 👊')
print(f'|-----------------------------------|\n'
      f'|       Opciones del programa       |\n'
      f'|-----------------------------------|\n'
      f'|   [1] Proceso completo de notas   |\n'
      f'|   [0] Nota minima en Examen       |\n'
      f'|-----------------------------------|')
v1 = int(input(f'Porfavor digite su Opción --> '))
print(f'Recuerde que las notas deben ser de 0 al 5')
if v1 == 1:
    err = 0
    while err == 0:
       # notaexamen = float(input()
        examen = float(input(f'Cual es la nota definitiva de los Exmenes sabiendo que equivalen al 60% --> '))
        quiz = float(input(f'Cual es la nota definitiva de los Quices sabiendo que equivalen al 25% --> '))
        trabajos = float(input(f'Cual es la nota definetiva de los trabajos sabiendo que equivalen al 15% --> '))
        if quiz < 0 or examen < 0 or trabajos < 0 or quiz > 5 or examen > 5 or trabajos > 5:
            print(f'Error!, porfavor verifique q las notas sean >= 0 , <= 5')
        else:
            x = completo(trabajos, quiz, examen)
            nota = "la nota definitiva es de --> "
            err = err + 1
if v1 == 2:
    err = 0
    while err == 0:
        print("Cual es la nota definitiva de los Quices sabiendo que equivalen al 25% -->")
        quiz = float(input())
        print("Cual es la nota definetiva de los trabajos sabiendo que equivalen al 15% -->")
        trabajos = float(input())
        if quiz < 0 or trabajos < 0 or quiz > 5 or trabajos > 5:
            print(f'Error!, porfavor verifique q las notas sean >= 0 , <= 5')
        else:
            x = minimo(trabajos, quiz)
            nota = "la nota minima debe ser de --> "
            err = err + 1
    print(f'  cargando...\n'
          f'💪 (︡❛ ‿❛︠) 👊')
    time.sleep(1)
print(nota,x)
