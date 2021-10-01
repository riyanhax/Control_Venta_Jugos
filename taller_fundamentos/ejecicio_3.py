'''3. Suponga que las tarifas de una compañía de gas se basan en el consumo de acuerdo con la siguiente información: los primeros
    70 metros cúbicos de gas usado tiene un costo mínimo de 500 pesos, los siguientes 100 metros cúbicos de gas usado 50 pesos por
    metro cúbico, los siguientes 230 metros cúbicos de gas usado 25 pesos por metro cúbico, por encima de 400 metros cúbicos de gas
    usado 15 pesos por metro cúbico. Dada la lectura anterior y actual de gas en metros cúbicos, calcule el valor de la factura; teniendo
    en cuenta que si la lectura actual es menor a la anterior hay una rebaja del 20% en las lecturas menores de 70 y mayores de 170
    metros cúbicos; además si la lectura actual es igual al 50% de la lectura anterior se hará una rebaja del 50% a las lecturas mayores
    de 170 y menores de 400 metros cúbicos
'''

v1 = int(input(f'Digite el consumo altual de Gas --> '))
v2 = int(input(f'Digite el consumo anterior de Gas --> '))
if v1 <= 70:
    tal = 500
if v1 > 71 and v1 < 170:
    fal = v1 - 70
    tal = 500 + fal * 50
if v1 > 171 and v1 < 400:
    fal = v1 - 170
    tal = 5500 + (fal * 25)
if v1 > 400:
    fal = v1 - 400
    tal = (fal * 15) + 11250
print(f'El total a pagar sin decuento es de --> ',tal)
if v1 < v2:
    if v1 < 70 or v1 > 170:
        tal = tal * 0.8
    lecv2 = v2 * 0.50
    if v1 == lecv2:
        if v1 > 170 and v1 < 400:
            tal = tal * 0.50
print(f'El total a pagar con decuento es de --> ',tal)