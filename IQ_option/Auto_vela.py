from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
import time, sys, logging

logging.disable(level=(logging.DEBUG))

API = IQ_Option('yordantarazona23@gmail.com', '1004925617*Cy')
API.connect()

API.change_balance('PRACTICE')  # PRACTICE / REAL

while True:
    if API.check_connect():
        print(' Conectado com sucesso!')
        break
    else:
        print(' Erro ao conectar')
        input('\n\n Aperte enter para sair')
        sys.exit()

def tiempo(x):
    # minu = float(((datetime.now()).strftime('%M,%S'))[1:])
    now = datetime.now()
    seg = now.time().strftime('%S')
    if x == 0:
        if seg >= '59':
            return True
    elif x == 1:
        if seg <= '2':
            return True


def payout(par):
    a = API.get_all_profit()
    b = int(100 * a[par]['turbo'])
    return b

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
    perf = API.get_profile_ansyc()
    print(f"Usuario: {perf['name']}")
    balance = (API.get_balance())
    print("Balance : " + str(balance))


par = 'EURUSD'
valor = 1
dir = ''
profit = [0,0]
loss = [0,0]
cont = 1
cntr = 0
win1 = 0

info()
#pay = payout(par)
pay = 60
paymax = (100 - pay) / 100

while True:
    if tiempo(0):
        vela = API.get_candles(par, 60, 1, time.time())
        if vela[0]['open'] < vela[0]['close']:
            dir = 'CALL'
        else:
            dir = 'PUT'
        if dir == 'CALL' or dir == 'PUT':
            break
while True:
    if tiempo(1):
        if pay >= 60:
            print(f"\n*******************************************************\n\n")
            now = datetime.now()
            hora = now.time().strftime('%H:%M:%S')
            print(f"Orden a la: ''{dir}'', Pagando el [{pay}%], Hora: {hora}")
            status, id = API.buy(valor, par, dir, 1)
            #print(f"pps: {status}, ids: {id}")
            if status:
                print(f"\n     Orden Aceptada :) ")
                while True:
                    chek, win = API.check_win_v3(id)
                    if chek:
                        break
                if win < 0:
                    print(f"\n Orden Perdida :( \n")
                    loss[0] += 1
                    loss[1] += valor
                    valor = (valor * 2) + paymax
                    print(f"MG #{cont}, calor: ${valor}\n")
                    cont += 1
                    if dir == 'CALL':
                        dir = 'PUT'
                    else:
                        dir = 'CALL'
                else:
                    print(f"\n Orden Ganada :) \n"
                          f"\n Orden: [{dir}], lucro: ${round(win,2)}")
                    profit[0] += 1
                    profit[1] += win
                    valor = 1
                    cont = 1
                if cntr == 10:
                    balance = (API.get_balance())
                    print("\n--------------")
                    print("\n\nGanadas : " + str(profit[0]) + "     Perdidas : " + str(loss[0]))
                    print("\nprofit : " + str(profit[1]) + "      loss : " + str(loss[1]))
                    print(f"\n Total(P-L) --> ${round((profit[1]-loss[1]),2)}")
                    print("\n\n--------------")
                    print("\n\n*******************************\n"
                          "\n\n  Balance : " + str(balance) + "\n"
                          "********************************\n")
                    cntr = 0
                else:
                    cntr = cntr + 1
            else:
                print(f"\n\n   !! Orden Rechazada ¡¡   \n\n")
        else:
            now = datetime.now()
            min = now.time().strftime('%M')
            if min == 1 or min == 20 or min == 40:
                print(f"\n\n !! No operar ingreso --> '' {pay}% '' ¡¡ ")
        #time.sleep(0.5)