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
        #perf = api.get_profile_ansyc()
        #print(f"Saldo: ${perf['balance']}")

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
    m5 = {}
    m15 = {}
    gen = {}
    print(indicador)
    for i in indicador:
        v = i['action']
        print('esta es v '+v)
        #g = i['group']
        g = 'MOVING AVERAGES'
        todo = i['candle_size']
        #itodo = 60
        if v == 'buy' or v == 'sell':
            if g == 'MOVING AVERAGES':
                if todo == 60:
                    if v not in m1:
                        m1[v] = 0
                    m1[v] += 1
                if todo == 300:
                    if v not in m5:
                        m5[v] = 0
                    m5[v] += 1
                """
                if todo == 900:
                    if v not in m15:
                        m15[v] = 0
                    m15[v] += 1
                   """

            if v not in gen:
                gen[v] = 0
            gen[v] += 1

        print(f"Grupo: {g}")
        print(f"todo: {todo}")

        print(f"m1:  {m1}\n"
              f"m5:  {m5}\n"
              f"m15: {m15}\n"
              f"gen: {gen}\n")

        a = 0
        b = 0
        if 'buy' in m1 and 'buy' in m5:
            if m1['buy'] != "" and m5['buy'] != "":
                a = m1['buy']
                a += (m1['buy'])/2
        if 'sell' in m1 and 'sell' in m5:
            if m1['sell'] != "" and m5['sell'] != "":
                b = m5['sell']
                b += (m5['sell'])/2
        orden(a, b)


        """
        a = 0
        b = 0
        if 'buy' in gen:
            if gen['buy'] != "":
                a = gen['buy']
        if 'sell' in gen:
            if gen['sell'] != "":
                b = gen['sell']
        orden(a,b)
        #print(f"general: {gen}")
        """


        """
                if 'buy' in m1:
            if m1['buy'] >= 1:
                a = m1['buy']
                print(a)
                api.buy(1, par, 'CALL', 1)
        """
        time.sleep(1)