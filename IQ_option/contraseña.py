import time
from datetime import datetime
import logging as lg
import getpass

dir = 'PUT'
print('Verificando Entrada... 📊 || ', end='')
print(f"Direccion --> {dir}{' 📈' if dir == 'CALL' else ' 📉'}")
while True:
    entrar1 = False
    entrar2 = False
    entrar3 = False
    hora = datetime.now().strftime('%H:%M:%S')
    minutos = float(((datetime.now()).strftime('%M.%S'))[1:])
    entrar1 = True if (minutos >= 4.0 and minutos <= 4.02) or (minutos >= 9.0 and minutos <= 9.02) else False
    entrar2 = True if (minutos >= 2.58 and minutos <= 3) or (minutos >= 7.59 and minutos <= 8) else False
    entrar3 = True if (minutos <= 0.02) or (minutos >= 5.0 and minutos <= 5.02) else False
    if entrar1 == True:
        print(f"\nHora 1 -- > {hora}\n")
    if entrar2 == True:
        print(f"\nHora 2 -- > {hora}\n")
    if entrar3 == True:
        print(f"\nHora 3 -- > {hora}\n")
    time.sleep(0.5)