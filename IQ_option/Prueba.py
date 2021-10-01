import json

from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
import time, sys, logging

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


while True:
    if API.check_connect():
        print(' Conectado com sucesso!')
        break
    else:
        print(' Erro ao conectar')
        input('\n\n Aperte enter para sair')
        sys.exit()

cont = 0
buy = 0
m_b = 0
c_b = 0
sell = 0
m_s = 0
c_s = 0
while True:
    print('\n\n***********************************************************************************************************\n\n')
    indicador = API.get_technical_indicators('EURUSD')
    for i in indicador:
        if (i['candle_size'] == 60 or i['candle_size'] == 300) and (i['group'] == 'MOVING AVERAGES' or i['group'] == 'OSCILLATORS'): #'OSCILLATORS'  'MOVING AVERAGES'
            if cont == 0:
                m_b = i['value']
                m_s = i['value']
                #print(m_b)
            if i['action'] == 'buy':
                buy += i['value']
                if i['action'] == 'buy' and i['value'] < m_b:
                    m_b = i['value']
                c_b += 1
            elif i['action'] == 'sell':
                sell += i['value']
                if i['action'] == 'sell' and i['value'] < m_s:
                    m_s = i['value']
                c_s += 1
            print(f"indicador: [{cont}], {str(i)}")
            cont += 1
    cont = 0

    input(f"\n          BUY: [ {str(round(float(buy/c_b),6) if c_b != 0 else 'N/N')} ]   ||"
          f"   SELL: [ {str(round(float(sell/c_s),6)) if c_s != 0 else 'N/N'} ]\n"
          f"\n    BUY: [ {str(m_b)} ]   ||   SELL: [ {str(m_s)} ]"
          f"\n\n\n   [ENTER o ESPACIO] para continuar >> ")
    time.sleep(0.5)
