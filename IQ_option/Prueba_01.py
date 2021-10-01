from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
import time, sys, logging
import json

logging.disable(level=(logging.DEBUG))

try:
    ten_login = 0
    API = {}
    status = False
    print(f"\n\n informacion de usuario\n")
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
except KeyboardInterrupt:
    print(' .: Deteniendo BOT :.')

cont = 0
lucro = 0
valor = 2
# dir = ''
win = 0
cont_mg = 0

print('\n\n               Iniciando estrategia 😎\n\n'
      'Esperando Orden... 😎')
par = 'EURUSD'

while True:
    estr = 1
    now = datetime.now()
    seg = now.time().strftime('%S')
    if seg >= '59':
        buy = 0
        sell = 0
        print(
            '\n\n***********************************************************************************************************\n\n')
        indicador = API.get_technical_indicators(par)
        for i in indicador:
            if i['candle_size'] == 60 and (i['name'] == 'Commodity Channel Index (20)' or
                                           i['name'] == 'Exponential Moving Average (5)' or
                                           i['name'] == 'Hull Moving Average (9)'):
                # i['name'] == 'Relative Strength Index (14)' or
                # i['name'] == 'Exponential Moving Average (20)' or
                # i['name'] == 'Stochastic RSI Fast (3, 3, 14, 14)' or
                # i['name'] == 'Exponential Moving Average (10)' or
                if i['action'] == 'buy':
                    buy += 1
                elif i['action'] == 'sell':
                    sell += 1
                print(f"indicador: [{cont}], {str(i)}")
                cont += 1
        cont = 0
        print(f"buy: {buy} || sell: {sell}")
        if buy >= 2 and buy > sell:
            dir = 'CALL'
        elif sell >= 2 and sell > buy:
            dir = 'PUT'
        if buy < 2 and sell < 2:
            print(f"\n !! NO SE CUMPLE LA ESTRATEGIA ¡¡\n"
                  f"\n Esperando Nueva Orden... 😎")
            estr = 0
            """
        if win == 1 and cont_mg <= 3:
            valor *= 2
            cont_mg += 1
            MG = (f", MG {cont_mg}")
        else:
            win = 0
            cont_mg = 0
            valor = 2
            """
        if estr == 1:
            fech = now.time().strftime('%H:%M:%S')
            print(f"\n    Orden: {dir}, Valor: ${valor}{MG if cont_mg != 0 else ''}, Hora -- > {fech}\n")
            # st, id = API.buy_digital_spot(par, valor, dir, 1)
            st, id = API.buy(valor, par, dir, 1.5)
            if st:
                print(f"\n   || Esperando Resultados... 😎 ||\n")
                while True:
                    # status, val = API.check_win_digital_v2(id)
                    status, val = API.check_win_v3(id)
                    if status:
                        val = val if val > 0 else float('-' + str(abs(val)))
                        lucro += round(val, 2)

                        print('\n     WIN:' if val > 0 else '\n     LOSS:', round(val, 2), '\n     Lucro Líquido:',
                              round(lucro, 2))
                        print(f"\n  Esperando Nueva Orden... 😎 \n")

                        # stop_check(lucro, stop_gain, stop_loss)

                        if val < 0:
                            win = 1
                        else:
                            win = 0
                        break
            else:
                print('\nERRO AO REALIZAR ORDEM\n\n')
            # input(f"\n          BUY: [ {str(buy)} ]   ||   SELL: [ {str(sell)} ]\n"
            #       f"\n\n\n   [ENTER o ESPACIO] para continuar >> ")
    time.sleep(1)
