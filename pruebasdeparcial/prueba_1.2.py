n=int(input('en numero : '))
if n>99 and n<999:
    if n%2==0:
        d1=n%10
        n=n/10
        d2=n%10
        n=n/10
        d3=n%10
        print(f'el numero {n} corresponden {d1} {d2} {d3} / en 2')
    elif n%3==0:
        d1 = n % 10
        n = n / 10
        d2 = n % 10
        n = n / 10
        d3 = n % 10
        print(f'el numero {n} corresponden {d1} {d2} {d3} / en 3')
    elif n%5==0:
        d1 = n % 10
        n = n / 10
        d2 = n % 10
        n = n / 10
        d3 = n % 10
        print(f'el numero {n} corresponden {d1} {d2} {d3} / en 3')