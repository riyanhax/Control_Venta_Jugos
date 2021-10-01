import sys
from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
import time, logging

logging.disable(level=(logging.DEBUG))

#user = str(input(f"Correo o Usuario --> "))
#pwd = str(input(f"Contraseña --> "))

#api = IQ_Option(user,pwd)
api = IQ_Option('yordantarazona23@gmail.com', '1004925617*Cy')
#api = IQ_Option('yordanubuntu@gmail.com', 'nadroymccm23')
#api = IQ_Option('yordantarazona9@gmail.com', '3228240575')

api.connect()

api.change_balance('PRACTICE') # PRACTICE / REAL

while True:
    if api.check_connect() == False:
        print(f"Error de Conexión")
    else:
        print(f"Conexión Exitosa...")
        break
    time.sleep(1)

def banca():
    return api.get_balance()

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
    seg = now.time().strftime('%S')
    #if seg >= '28':
    if seg >= '58' and seg <= '59':
        return True

def stop_check(lucro, gain, loss):
    if lucro <= float('-' + str(abs(loss))):
        print('Stop Loss batido!')
        sys.exit()

    if lucro >= float(abs(gain)):
        print('Stop Gain Batido!')
        sys.exit()

def orden(a,b):
    if a >= 10 or b >= 10:
        if a > b:
            return 1
        if b > a:
            return 0
    else:
        return -1

def tec_indicator():
    indicador = api.get_technical_indicators(par)
    buy = {}
    sell = {}
    for i in indicador:
        v = i['action']
        if i['candle_size'] == 60:
            if v == 'buy':
                if v not in buy:
                    buy[v] = 0
                buy[v] += 1
            if v == 'sell':
                if v not in sell:
                    sell[v] = 0
                sell[v] += 1
        if i['candle_size'] == 60:
            if v == 'buy':
                if v not in buy:
                    buy[v] = 0
                buy[v] += 1
            if v == 'sell':
                if v not in sell:
                    sell[v] = 0
                sell[v] += 1

    a = 0
    b = 0
    if 'buy' in buy:
        if buy['buy'] != "":
            # a = buy['buy']
            a = (buy['buy']) / 2
    if 'sell' in sell:
        if sell['sell'] != "":
            # b = sell['sell']
            b = (sell['sell']) / 2
    return a,b

##################################################################################

info()

par = 'EURUSD'
#par = 'EURJPY'
valor = 2
lucro = 0
stop_loss = float(int(banca()) // 5)
stop_gain = float(int(banca()) // 2)
accion = ''
win = 0
cont_mg = 0

while True:
    now = datetime.now()
    seg = now.time().strftime('%S')
    if seg >= '57' or seg <= '59':

        a,b = tec_indicator()
        acc = orden(a, b)
        if acc != (-1):
            if tiempo():

                if win == 1:
                        valor *= float(2.2)
                        cont_mg += 1
                        print(f"MG #{cont_mg}")
                else:
                    win = 0
                    cont_mg = 0
                    valor = 2

                print(f"\n\nbuy --> {a}, sell --> {b}\n")
                if acc == 0:
                    accion = 'PUT'
                    print(f"VENTA --> ${valor}")
                elif acc == 1:
                    accion = 'CALL'
                    print(f"COMPRA --> ${valor}")

                fech = now.time().strftime('%H:%M:%S')
                print(f"Hora -- > {fech}\n")

                v1, id = api.buy(valor, par, accion, 1)

                #v1, id = api.buy_digital_spot(par,valor,accion,1)

                print(f"accion: {acc}, valor: {valor}")

                print(f"pps: {v1}, ids: {id}")

                if v1:
                    while True:

                        #status, val = api.check_win_digital_v2(id)
                        status, val = api.check_win_v3(id)

                        if status:
                            val = val if val > 0 else float('-' + str(abs(val)))
                            lucro += round(val, 2)

                            print('\nWIN:' if val > 0 else '\nLOSS:', round(val, 2), '\nLucro Líquido:',
                                  round(lucro, 2))

                            stop_check(lucro, stop_gain, stop_loss)

                            if val < 0:
                                win = 1
                            else:
                                win = 0
                            break
                else:
                    print('\nERRO AO REALIZAR ORDEM\n\n')

                time.sleep(1)
        now = datetime.now()
        min = now.time().strftime('%M')
        if min == '10' or min == '20' or min == '30' or min == '40' or min == '50' or min == '1':
            print(f"No se cumplio la estrategia :(")

