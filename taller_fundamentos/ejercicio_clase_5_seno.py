def factoril(num):
    fac1 = 1
    i = 1
    while i <= num:
        fac1 = fac1 * i
        i = i +1
    return fac1
def poten(x, y):
    i = 1
    pot = 1
    while i <= y:
        pot = pot * x
        i += 1
    return pot
def seno(angu):
    sum = 0
    i = 0
    w = (angu * 3.1416) / 180
    










def factorion(num):
    aux = num
    sum = 0
    while num > 0:
        quita = num % 10
        num //= 10
        sum = sum + factoril(quita)
    if sum == aux:
        return 'Si'
    else:
        return 'No'
v1 = int(input(f'Digite el numero --> '))
a = factorion(v1)
print(f'El numero "{a}" es factorion.')