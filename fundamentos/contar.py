'''
lista = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
totaldiascuentavieja = 0

for dia in lista:
    totaldiascuentavieja += 1

print("El número de elementos de la lista, por la cuenta de la vieja es",
 totaldiascuentavieja)
print("El número de elementos de la lista según la función len es", len(lista))

primos = [2]
nmax = 10
for x in range(3, nmax):
    for i in range(2, x):
        if x%i != 0:
            #i no es divisor de x, x puede ser primo
            continue
        else:
            #i es divisor de x, x no es primo
            break #No es necesario buscar más divisores
    else:
        #El bucle for ha terminado con normalidad
        #El número que estábamos comprobando es primo
        print('%d es primo'%x)
        primos.append(x)
F = open('numerosprimos.txt', 'w')
for data in primos:
    F.write('%d\n'%data)
'''

def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def app():
    num = int(input('Write a number: '))
    result = isPrime(num)

    if result is True:
        print('The number is prime!!')
    else:
        print('The number is not prime!!')

if __name__ == '__main__':
    app()