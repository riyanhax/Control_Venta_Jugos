'''Haga un programa en python de manera modular (usando funciones) para el siguiente problema: la empresa “rapinet”
ofrece el servicio de Internet de acuerdo a las siguientes condiciones:
La tarifa se cobra por horas y minutos de la siguiente forma: Si el número de minutos es menor de 30 no se le cobran
los minutos extras (solo las horas enteras) si los minutos están entre 30 y 45 se cobra a 15 pesos los minutos que
exceden de 30 y si los minutos son mayores de 45 se le cobra una hora completa.
La tarifa por horas depende del número de horas que navegue de acuerdo a la siguiente tabla
Tiempo de navegación Valor a pagar por hora
De 1 a 5 horas 1500 pesos por hora
De 5 a 10 horas 1200 pesos por hora
Más de 10 horas 900 pesos por hora
La empresa ofrece el 10% de descuento sobre el total a pagar, para las personas cuya cuenta supere los 10000 pesos.
Dado por teclado el tiempo de navegación de cada una de las personas que reciben el servicio en un día, hacer un
programa en python
que calcule el total a pagar de cada una de las personas que hacen uso del servicio y el total recaudado por la empresa
en un día.
Para ello desarrolle las siguientes funciones
 Una función llamada “calcular” que calcule el total a pagar (sin descuento) conociendo el número de horas y
minutos navegados
 Una función llamada “descuento” que calcule el total de dinero a descontar por el servicio de Internet,
conociendo el total a pagar sin descuento.
En la función principal se debe capturar las horas y minutos de navegación de cada uno de los clientes del día.
Como no se conoce el número de clientes que atiende la empresa durante el día, el proceso termina cuando el
número de horas navegadas sea un número negativo.
En la función principal también hay que calcular el total recaudado por la empresa en dicho día.
'''

def calcular(numHor):
    valor = 0
    if numHor <= 30:
        valor = (numHor * 1500) / 60
    elif numHor > 30 and numHor <= 45:
        res = numHor - 30
        valor = (res * 15) + 750
    elif numHor > 45 and numHor <= 300:
        valor = 1500
    elif numHor > 300 and numHor <= 600:
        valor = 1200
    else:
        valor = 900
    return valor
def descuento(valo):
    if valo >= 10000:
        valdes = (valo * 10) / 10000
    else:
        valdes = 0
    return valdes
suma = 0
while True:
    minu = int(input('cual fue el numero de minutos de servicio :'))
    if minu < 0:
        break
    a = calcular(minu)
    b = descuento(a)
    r = a - b
    print('el valor sin descuento es de $',a,' y con descuento es de $',b)
    print('el total a pagar es de $',r)
    suma = suma + r
print('el total recaudado es de $',suma)