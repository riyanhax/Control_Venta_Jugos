


valores = [1,0,1,1,1,0,0,0,0,0,1,1,1,0,
           1,0,1,1,1,0,0,0,1,0,1,1,1,0,
           0,0,1,0,1,0,1,0,1,0,1,0,1,0,
           0,1,1,0,1,0,1,0,1,0,1,0,1,0,
           1,0,0,0,1,1,1]

uno = 0
cero = 0

for i in valores:
    if i == 1:
        uno += 1
    else:
        cero += 1
can = len(valores)
uno = (uno/can)*100
cero = (cero/can)*100
print(f"El % de q sea '1' --> {uno}\n"
      f"El % de q sea '0' --> {cero}")
