from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
import time, sys, logging
import json

logging.disable(level=(logging.DEBUG))

print('''
	     BOT Multi Estrategia TG-3M-C3
 ---------------------------------------------
''')

try:
    ten_login = 0
    API = {}
    status = False
    print(f"\n  .:::[ informacion de usuario ]:::.\n")
    while status == False and ten_login < 3:
        API = IQ_Option('yordantarazona23@gmail.com', '1004925617*Cy')
        ten_login += 1
        status, rea = API.connect()
        if status == False:
            res = json.loads(rea)
            if 'code' in res and res['code'] == 'invalid_credentials':
                print(f"\n\nUsuario o Contraseña Invalidos!!\n\n")
            else:
                print(f"\n\nERROR al conectar: {res['message']}\n\n")
        else:
            break
    if status == False:
        raise ValueError('\n Demaciados Intentos!!! \n')
    print('\n       Conectado con Exito :)  \n')
    API.change_balance('PRACTICE')  # PRACTICE / REAL
except ValueError as ve:
    print(f"{ve}\n\n"
          f" .: Deteniendo BOT :.")
    sys.exit()
except KeyboardInterrupt:
    print(' .: Deteniendo BOT :.')
    sys.exit()

def stop(lucro, gain, loss):
    if lucro <= float('-' + str(abs(loss))):
        print('Perdidas max alcanzada (Stop Loss)! 😢')
        sys.exit()

    if lucro >= float(abs(gain)):
        print('Ganancias max alcanzada (Stop Gain)?! 🥳')
        sys.exit()

def Martingale(valor, payout):
    pass
    """
    lucro_esperado = valor * payout
    perca = float(valor)

    while True:
        if round(valor * payout, 2) > round(abs(perca) + lucro_esperado, 2):
            return round(valor, 2)
            break
        valor += 0.01
    """

def Payout(par):
    API.subscribe_strike_list(par, 1)
    while True:
        d = API.get_digital_current_profit(par, 1)
        if d != False:
            d = round(int(d) / 100, 2)
            break
        time.sleep(1)
    API.unsubscribe_strike_list(par, 1)

    return d

def Estrategia(lucro):
    if entrar1:
        print('\n\nIniciando Operación!    Estrategia Gemelas 😎')
        dir = False
        print('Verificando Entrada... 📊 || ', end='')
        velas = API.get_candles(par, 60, 5, time.time())

        velas[0] = 'g' if velas[0]['open'] < velas[0]['close'] else 'r' if velas[0]['open'] > velas[0]['close'] else 'd'
        # velas[1] = 'g' if velas[1]['open'] < velas[1]['close'] else 'r' if velas[1]['open'] > velas[1]['close'] else 'd'
        # velas[2] = 'g' if velas[2]['open'] < velas[2]['close'] else 'r' if velas[2]['open'] > velas[2]['close'] else 'd'

        # cores = velas[0] + ' ' + velas[1] + ' ' + velas[2]
        # print(cores)

        # if cores.count('g') > cores.count('r') and cores.count('d') == 0: dir = ('put' if tipo_mhi == 1 else 'call')
        # if cores.count('r') > cores.count('g') and cores.count('d') == 0: dir = ('call' if tipo_mhi == 1 else 'put')

        dir = 'CALL' if velas[0] == 'g' else 'PUT' if velas[0] == 'r' else ''
        if dir != '':
            Operacion(dir, lucro)
        else:
            print(f"\n ⚠️NO opera ALTO RIESGO.... ")
    if entrar2:
        print('\n\nIniciando Operación!    Estrategia Torres Gemelas 😎')
        dir = False
        print('Verificando Entrada... 📊 || ', end='')
        velas = API.get_candles(par, 60, 4, time.time())

        velas[0] = 'g' if velas[0]['open'] < velas[0]['close'] else 'r' if velas[0]['open'] > velas[0]['close'] else 'd'
        # velas[1] = 'g' if velas[1]['open'] < velas[1]['close'] else 'r' if velas[1]['open'] > velas[1]['close'] else 'd'
        # velas[2] = 'g' if velas[2]['open'] < velas[2]['close'] else 'r' if velas[2]['open'] > velas[2]['close'] else 'd'

        # cores = velas[0] + ' ' + velas[1] + ' ' + velas[2]
        # print(cores)

        # if cores.count('g') > cores.count('r') and cores.count('d') == 0: dir = ('put' if tipo_mhi == 1 else 'call')
        # if cores.count('r') > cores.count('g') and cores.count('d') == 0: dir = ('call' if tipo_mhi == 1 else 'put')

        dir = 'CALL' if velas[0] == 'g' else 'PUT' if velas[0] == 'r' else ''
        if dir != '':
            Operacion(dir, lucro)
        else:
            print(f"\n ⚠️NO opera ALTO RIESGO.... ")

def Operacion(dir, lucro):
    if dir:
        print(f"Direccion --> {dir}{' 📈' if dir == 'CALL' else ' 📉'}")

        valor_entrada = valor_entrada_b
        for i in range(martingale):

            status, id = API.buy_digital_spot(par, valor_entrada, dir, 1) if operacao == 1 else API.buy(
                valor_entrada, par, dir, 1)
            # status = False
            if status:
                while True:
                    try:
                        status, valor = API.check_win_digital_v2(id) if operacao == 1 else API.check_win_v3(id)
                    except:
                        status = True
                        valor = 0

                    if status:
                        valor = valor if valor > 0 else float('-' + str(abs(valor_entrada)))
                        lucro += round(valor, 2)

                        print('Resultado operação: ', end='')
                        print('WIN 💵 / $' if valor > 0 else 'LOSS 💸 / $', round(valor, 2), '/', round(lucro, 2),
                              ('/ ' + str(i) + ' GALE' if i > 0 else ''))

                        #valor_entrada = Martingale(valor_entrada, payout)
                        if valor < 0 or lucro < 0:
                            valor_entrada += float(1.5)

                        stop(lucro, stop_gain, stop_loss)

                        break

                if valor > 0: break

def payout(par, tipo, timeframe=1):
    if tipo == 'turbo':
        a = API.get_all_profit()
        return int(100 * a[par]['turbo'])

    elif tipo == 'digital':
        API.subscribe_strike_list(par, timeframe)
        while True:
            d = API.get_digital_current_profit(par, timeframe)
            if d != False:
                d = int(d)
                break
            time.sleep(1)
        API.unsubscribe_strike_list(par, timeframe)
        return d

perf = API.get_profile_ansyc()
balance = API.get_balance()
print(f":::::::[ BIENVENIDO 😎 ]:::::::\n"
      f"Usuario: {perf['name']}\n"
      f"Saldo: ${balance}")

par = API.get_all_open_time()

for paridade in par['turbo']:
    if par['turbo'][paridade]['open'] == True:
        print('[ TURBO ]: ' + paridade + ' | Payout: ' + str(payout(paridade, 'turbo')))

print('\n')

for paridade in par['digital']:
    if par['digital'][paridade]['open'] == True:
        print('[ DIGITAL ]: ' + paridade + ' | Payout: ' + str(payout(paridade, 'digital')))

while True:
    try:
        operacao = int(input('\n Cual Option? \n  1 - Digital\n  2 - Binaria\n  :: '))
        if operacao > 0 and operacao < 3: break
    except:
        print('\n Opcion no valida...')

par = input(' Cual es el PAR a operar? --> ').upper()
valor_entrada = float(input(' Valor a invertir? --> '))
valor_entrada_b = float(valor_entrada)

martingale = int(input(' Cuantos MG desea? --> '))
martingale += 1

stop_loss = float(input(' Valor max en Perdidas (Stop Loss)?  --> '))
stop_gain = float(input(' Valor max en Ganancias (Stop Gain)? --> '))

print(f"   Iniciando BOT... 😎")

lucro = 0
payout = Payout(par)

while True:
    hora = datetime.now().strftime('%H:%M:%S')
    minutos = float(((datetime.now()).strftime('%M.%S'))[1:])
    """
    entrar1 = True if (minutos <= 4.1) or minutos <= 9.1 else False
    entrar2 = True if (minutos >= 2.58 and minutos <= 3) or minutos >= 7.58 else False
    entrar3 = True if (minutos <= 0.1) or minutos >= 5.1 else False
    """
    entrar1 = True if (minutos >= 0.59 and minutos <= 1.01) or (minutos >= 5.59 and minutos <= 6.01) else False
    entrar2 = True if (minutos >= 3.59 and minutos <= 4.01) or (minutos >= 8.59 and minutos <= 9.01) else False
    if entrar1 == True:
        print(f"\n\nHora -- > {hora}")
        Estrategia(lucro)
    if entrar2 == True:
        print(f"\n\nHora -- > {hora}")
        Estrategia(lucro)

    time.sleep(0.2)