n = 50
cuantonum = input(f'digite el numero :')
cont= 0
while (cont < cuantonum):
    cont = cont + 1
    factorial = 1
    num = input(f'numero {cont+1}')
    for i in range(1, int(n) + 1):
        factorial = factorial * i
        print("Factorail of ", n, " is : ", factorial)
    if num == factorial:
        print(f'num es resultado ')
    # print("Factorail of ",n , " is : ",factorial)
