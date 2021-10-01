def mostrar():
    prin = navega(v1)
    print(f'El valor a pagar por los {v1} minutos de internt son --> ${prin}')
def navega(x):
    if x >= 1 and x <= 15:
        val = 500
    elif x > 15 and x <= 30:
        val = 1000
    elif x > 30 and x <= 60:
        val = 1400
    else:
        val = ((x - 60) * 20) + 1400
    return val
v1 = int(input(f'Cuanto es el tiempo de servicio? --> '))
mostrar()