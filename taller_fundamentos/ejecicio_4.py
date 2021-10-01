'''4. Hacer un programa que asista el proceso de elecciones democráticas. Se desea saber para que votara una persona (Senado o
    Cámara), para qué partido político y el número del candidato por el cual voto el pasado domingo, Si se da un número de 4 dígitos
    (que representa el voto de la persona) con los cual se puede deducir:
    El primer dígito nos indica el partido político
    Número Partido
    1 Liberal
    2 Conservador
    3 Partido de la U
    4 a 9 Otros Partidos
    El segundo dígito nos indica si el voto fue para Cámara o Senado. Si el dígito es par el voto fue para Cámara, en caso de que el
    dígito sea impar el voto fue para Senado
    Los dos últimos dígitos nos indican el número del candidato
'''

def mostrar():
    candi, case, partido = eleccion(voto)
    cont1 = 0
    num = int(candi)
    while num > 0:
        quita = num % 10
        cont1 = (cont1 * 10) + quita
        num //= 10
    if partido == 1:
        parti = 'Liberal'
    if partido == 2:
        parti = 'Conservador'
    if partido == 3:
        parti = 'Partido de la U'
    if partido > 3 and partido < 10:
        parti = 'Otros Partidos'
    print(f'El partido por que voto es "{parti}" y el de Cámara o Senado es "{case}" y el candidato es "{cont1}"')
def eleccion(x):
    cont1 = 0
    cont2 = 0
    cont3 = 0
    i = 0
    while i <= 1:
        quita = x % 10
        cont1 = (cont1 * 10) + quita
        x //= 10
        i = i + 1
    quita = x % 10
    cont2 = (cont2 * 10) + quita
    x //= 10
    if cont2 % 2 == 0:
        res = 'Camara'
    else:
        res = 'Senado'
    quita = x % 10
    cont3 = (cont3 * 10) + quita
    return cont1, res, cont3
print(f'|------------------------------------------------|\n'
      f'|     [1er] para el partido                      |\n'
      f'|     [2do] para camara o senado                 |\n'
      f'|     [3er y 4to] para el candidato              |\n'
      f'|------------------------------------------------|')
voto = int(input(f'El numero de su eleccion es --> '))
while voto <= 999 or voto >= 10000:
    print(f'¡Error!, intente nuevamente')
    voto = int(input(f'El numero de su eleccion es --> '))
mostrar()