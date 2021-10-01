"""
1. La nota final de un estudiante de Programación, se compone de los siguientes porcentajes
60% Examen, 25% Quices y 15% Trabajos. Las calificaciones corresponden a números decimales entre 0 y 5.
Hacer un programa que muestre la nota definitiva
"""
n1 = 1
n2 = 1
n3 = 1
res1 = 0
res2 = 0
res3 = 0
print("Bienvenido al programa evaluador de notas")
print("Empesaremos con los Examenes, continuar s/n")
v2 = input('-->')
while True:
	if v2!="s" and v2!="n":
		print("Opcion invalida, Contuniar s/n")
		v2 = input()
	if v2=="s" or v2=="n": break
print("---------------------------------------------")
if v2=="s":
	while True:
		print("valor de la nota del Exemen: ",n1)
		v1 = float(input())
		while True:
			if v1 > 5 or v1 < 0:
				print("Dato no valido, valor de la nota del exemen: ",n1)
				v1 = float(input())
			if v1<=5 and v1>=0: break
		print("contuniar con otra nota de Examenes s/n")
		v2 = input()
		while True:
			if v2!="s" and v2!="n":
				print("Opcion invalida, Contuniar s/n")
				v2 = input()
			if v2=="s" or v2=="n": break
		n1 = n1+1
		res1 = res1 + v1
		resul1 = ((res1/(n1-1))*60)/100
		if v2=="n": break
	print("---------------------------------------------")
	print("contuniar con las notas de los Quices s/n")
	v2 = input()
	while True:
		if v2!="s" and v2!="n":
			print("Opcion invalida, Contuniar s/n")
			v2 = input()
		if v2=="s" or v2=="n": break
	print("---------------------------------------------")
	while True:
		print("valor de la nota del Quices: ",n2)
		v1 = float(input())
		while True:
			if v1>5 or v1<0:
				print("Dato no valido, valor de la nota del Quices: ",n2)
				v1 = float(input())
			if v1<=5 and v1>=0: break
		print("contuniar con otra nota de los Quices s/n")
		v2 = input()
		while True:
			if v2!="s" and v2!="n":
				print("Opcion invalida, Contuniar s/n")
				v2 = input()
			if v2=="s" or v2=="n": break
		n2 = n2+1
		res2 = res2 + v1
		resul2 = ((res2/(n2-1))*25)/100
		if v2=="n": break
	print("---------------------------------------------")
	print("contuniar con las notas de los Trabajos s/n")
	v2 = input()
	while True:
		if v2!="s" and v2!="n":
			print("Opcion invalida, Contuniar s/n")
			v2 = input()
		if v2=="s" or v2=="n": break
	print("---------------------------------------------")
	while True:
		print("valor de la nota del Trabajo: ",n3)
		v1 = float(input())
		while True:
			if v1>5 or v1<0:
				print("Dato no valido, valor de la nota del Trabajo: ",n3)
				v1 = float(input())
			if v1<=5 and v1>=0: break
		print("contuniar con otra nota de los Trabajos s/n")
		v2 = input()
		while True:
			if v2!="s" and v2!="n":
				print("Opcion invalida, Contuniar s/n")
				v2 = input()
			if v2=="s" or v2=="n": break
		n3 = n3+1
		res3 = res3 + v1
		resul3 = ((res3/(n3-1))*15)/100
		if v2=="n": break
	print("---------------------------------------------")
	resul = resul1+resul2+resul3
	print("Las notas del estudiante son, Examenes 60% :",resul1,", Quices 25% : ",resul2,", Trabajos 15% : ",resul3,", "
								"con una definitiva de un Total de : ",resul)
	print("---------------------------------------------")
else:
	print("Cancelo el proceso")
	print("Que tengas buen dia")
print("---------------------------------------------")
