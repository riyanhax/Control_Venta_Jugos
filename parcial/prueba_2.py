def bonifica(m,s):
    if m == 'junio':
        boni = (s * 50) / 100
    else:
        boni = (s * 2.5) / 100
    return boni
def salpen(s):
    salu = (s * 4) / 100
    penc = (s * 4) / 100
    totalsalpen = salu + penc
    return salu, penc, totalsalpen
def diurna(s, d):
    salhora = (s / 240)
    incre = (salhora * 35) / 100
    salt = (d * salhora) * incre
    return salt
def noct(s, n):
    salhora = (s / 240)
    incre = (salhora * 70) / 100
    salt = (n * salhora) * incre
    return salt
def pres(pretamo):
    resul = (pretamo * 7)/ 100
def mostrar():
    a = bonifica(mes, saldo)
    b, x, y = salpen(saldo)
    c = diurna(saldo, diurnas)
    d = noct(saldo, nocturnas)
    e = pres(prestamo)
    print(f'la bonificacion es de {a}')
    print(f'la salud es {b} y la pension es de {x} total de {y}')
    print(f'las diurnas son {c}')
    print(f'las nocturnas son {d}')
    print(f'el total saldo es de {a+c+d}')
    print(f'el decuento es de {y}')
    print(f'total es de {(a+c+d)}')

saldo = int(input(f'salario del empleado'))
dias = int(input(f'dias :'))
diurnas = int(input(f'diurnas :'))
nocturnas = int(input(f'nocturnas :'))
prestamo = int(input(f'prestamo :'))
mes = input(f'mes :')
saldo_mes = (saldo / 30) * dias
pagopres = (saldo / 7) * 100
print(f'el saldo es de {saldo} \n'
      f'los dias trabajados {dias}\n'
      f'dias diurnas {diurnas}\n'
      f'dias nocyurnas {nocturnas}\n'
      f'el prestamo es de {prestamo}\n'
      f'')
mostrar()
