from iqoptionapi.stable_api import IQ_Option
import time, json, logging
from datetime import datetime
from dateutil import tz


API = IQ_Option('yordantarazona23@gmail.com', '1004925617*Cy')
API.connect()
API.change_balance('PRACTICE')  # PRACTICE / REAL

while True:
    if API.check_connect() == False:
        print('Erro ao se conectar')
        API.connect()
    else:
        print('Conectado com sucesso')
        break

    time.sleep(1)


def perfil():
    perfil = json.loads(json.dumps(API.get_profile_ansyc()))

    return perfil

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


def timestamp_converter(x):
    hora = datetime.strptime(datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    hora = hora.replace(tzinfo=tz.gettz('GMT'))

    return str(hora.astimezone(tz.gettz('America/Sao Paulo')))[:-6]


def banca():
    return API.get_balance()


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


par = API.get_all_open_time()

for paridade in par['turbo']:
    if par['turbo'][paridade]['open'] == True:
        print('[ TURBO ]: ' + paridade + ' | Payout: ' + str(payout(paridade, 'turbo')))

print('\n')

for paridade in par['digital']:
    if par['digital'][paridade]['open'] == True:
        print('[ DIGITAL ]: ' + paridade + ' | Payout: ' + str(payout(paridade, 'digital')))
"""
# Retorna o histórico, para pegar o histórico do digital, deve ser colocado 'digital-option' e para pegar binario,
#	deve ser colocado 'turbo-option'
status,historico = API.get_position_history_v2('turbo-option', 7, 0, 0, 0)

'''

:::::::::::::::: [ MODO DIGITAL ] ::::::::::::::::
FINAL OPERACAO : historico['positions']['close_time']
INICIO OPERACAO: historico['positions']['open_time']
LUCRO          : historico['positions']['close_profit']
ENTRADA        : historico['positions']['invest']
PARIDADE       : historico['positions']['raw_event']['instrument_underlying']
DIRECAO        : historico['positions']['raw_event']['instrument_dir']
VALOR          : historico['positions']['raw_event']['buy_amount']

:::::::::::::::: [ MODO BINARIO ] ::::::::::::::::
MODO TURBO tem as chaves do dict diferentes para a direção da operação(put ou call) 
	e para exibir a paridade, deve ser utilizado:
DIRECAO : historico['positions']['raw_event']['direction']
PARIDADE: historico['positions']['raw_event']['active']
'''

for x in historico['positions']:
   # print('PAR: '+str(x['raw_event']['active'])+' /  DIRECAO: '+str(x['raw_event']['direction'])+' / VALOR: '+str(x['invest']))
    print('LUCRO: '+str(x['close_profit'] if x['close_profit'] == 0 else round(x['close_profit']-x['invest'], 2) ) + ' | INICIO OP: '+str(timestamp_converter(x['open_time'] / 1000))+' / FIM OP: '+str(timestamp_converter(x['close_time'] / 1000)))
    print('\n')
"""