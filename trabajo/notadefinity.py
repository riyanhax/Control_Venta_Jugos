"""
desarrollar un programa que conociendo las notas de Quices y trabajos muestre la nota
mínima que debe sacar en el examen para pasar la materia sabiendo que la nota mínima es 3.0.
"""
print("Cual es la nota definitiva de los Quices sabiendo que equivalen al 25% :")
notaquiz = float(input())
print("Cual es la nota definetiva de los trabajos sabiendo que equivalen al 15% :")
notatrabajos = float(input())
notaexa = 3.0 - (notaquiz + notatrabajos)
print("la nota minima que debe sacar el estudiante en los Examenes es : ",notaexa,", que equivale al 60 %" )