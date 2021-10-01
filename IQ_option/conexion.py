from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
import time

api = IQ_Option('yordantarazona23@gmail.com', '1004925617*Cy')
#api = IQ_Option('yordantarazona9@gmail.com', '3228240575')

api.connect()

api.change_balance('PRACTICE') # PRACTICE / REAL

while True:
    if api.check_connect() == False:
        print(f"Error de Conexión")
    else:
        print(f"Conexión Exitosa...")
        break
    time.sleep(1000)

def info():
    # informacion
    '''
            name
            first_name
            last_name
            email
            city
            nickname
            currency
            currency_char
            address
            created
            postal_index
            gender
            birthdate
            balance
    '''
    perf = api.get_profile_ansyc()

    print(f"Usuario: {perf['name']}\n"
          f"Saldo: ${perf['balance']}")

def tiempo():
    #minu = float(((datetime.now()).strftime('%M,%S'))[1:])
    now = datetime.now()
    minu = now.time().strftime('%S')
    if minu >= '28' and minu <= '29':
        return True

def operacion(acc,a,b):
    #operaciones
    if tiempo():
        if acc == 0:
            api.buy(1, par, 'PUT', 1)
            print("VENTA")
            print(f"buy --> {a}, sell --> {b}")
        elif acc == 1:
            api.buy(1, par, 'CALL', 1)
            print("COMPRA")
            print(f"buy --> {a}, sell --> {b}")
        perf = api.get_profile_ansyc()
        print(f"Saldo: ${perf['balance']}")

def orden(a,b):
    if a >= 15 or b >= 15:
        if b > a:
            operacion(0,a,b)
        if a > b:
            operacion(1,a,b)

"""
indicador = api.get_technical_indicators(par)
for i in indicador:
    if i['candle_size'] == 60:
        print(i)
        #time.sleep(1000)
"""

info()
par = 'EURUSD'
while True:
    indicador = api.get_technical_indicators(par)
    m1 = {}
    gen = {}
    for i in indicador:
        v = i['action']
        g = i['group']
        todo = i['candle_size']
        if g == 'MOVING AVERAGES':
            if todo == 60:
                if v not in m1:
                    m1[v] = 0
                m1[v] += 1

        if v not in gen:
            gen[v] = 0
        gen[v] += 1

        a = 0
        b = 0
        if 'buy' in gen:
            if gen['buy'] != "":
                a = gen['buy']
        if 'sell' in gen:
            if gen['sell'] != "":
                b = gen['sell']
        orden(a,b)
        print(f"general: {gen}")

        """
                if 'buy' in m1:
            if m1['buy'] >= 1:
                a = m1['buy']
                print(a)
                api.buy(1, par, 'CALL', 1)
        """
        time.sleep(1)
