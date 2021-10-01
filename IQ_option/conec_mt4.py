from iqoptionapi.stable_api import IQ_Option
from threading import Thread, Lock, get_ident
from datetime import datetime
import os
import time

api = IQ_Option('yordantarazona23@gmail.com', '1004925617*Cy')
#api = IQ_Option('yordantarazona9@gmail.com', '3228240575')

api.connect()

api.change_balance('PRACTICE') # PRACTICE / REAL

while True:
    if api.check_connect() == False:
        print(f"Error de Conexión")
        input("ENTER para salir")
        exit()
    else:
        print(f"Conexión Exitosa...")
        break
    time.sleep(1)

a = api.get_ALL_Binary_ACTIVES_OPCODE()
print(a)

