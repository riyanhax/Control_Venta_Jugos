
class Jugo(object):
    """Esta es la clase de los Jugos"""

    __jNatu = 0
    __jno_Natu = 0
    __jbod_Natu = 0
    __jbod_no_Natu = 0

    def __init__(self, natu, no_natu, bod_natu, bod_no_natu):
        Jugo.__jNatu = natu
        Jugo.__jno_Natu = no_natu
        Jugo.__jbod_Natu = bod_natu
        Jugo.__jbod_no_Natu = bod_no_natu

    def getjNatu(self):
        return Jugo.__jNatu

    def getjno_Natu(self):
        return Jugo.__jno_Natu

    def getjbod_Natu(self):
        return Jugo.__jbod_Natu

    def getjbod_no_Natu(self):
        return Jugo.__jbod_no_Natu

    def venjNatu(self, natu):
        Jugo.__jNatu -= natu

    def venjno_Natu(self, no_natu):
        Jugo.__jno_Natu -= no_natu

    def verifica(self, can, tip):
        if tip == 1:
            if can != 5 and can < 20 or can > 30:
                if Jugo.__jNatu >= can:
                    return 1
                else:
                    return 0
            else:
                if Jugo.__jNatu > can:
                    return 1
                else:
                    return -1
        elif tip == 2:
            if can != 5 and can < 20 or can > 30:
                if Jugo.__jno_Natu >= can:
                    return 1
                else:
                    return 0
            else:
                if Jugo.__jno_Natu > can:
                    return 1
                else:
                    return -1

    def reabastecer(self, can, tip):
        print(end="\nProcesando.")
        for i in range(0, 4):
            time.sleep(0.5)
            print(".", end="")
        print('')
        time.sleep(1)
        if tip == 1:
            if Jugo.__jbod_Natu > 0 and can <= Jugo.__jbod_Natu:
                Jugo.__jNatu += can
                Jugo.__jbod_Natu -= can
                print(f"Reabastecimiento de jugos naturales Exitoso...")
                return 1
            else:
                print(f"Error! Cantidades no validas o insuficientes...")
                return 0
        elif tip == 2:
            if Jugo.__jbod_no_Natu > 0 and can <= Jugo.__jbod_no_Natu:
                Jugo.__jno_Natu += can
                Jugo.__jbod_no_Natu -= can
                print(f"Reabastecimiento de jugos no naturales Exitoso...")
                return 1
            else:
                print(f"Error! Cantidades no validas o insuficientes...")
                return 0

    def __str__(self):
        return (f"|******************************************************|\n"
                f"|{self.__doc__[24:29]}: Naturales -->{self.__jNatu}    \n"
                f"|       No naturales -->{self.__jno_Natu}              \n"
                f"|       Bodega Naturales -->{self.__jbod_Natu}         \n"
                f"|       Bodega No Naturales -->{self.__jbod_no_Natu}   \n"
                f"|******************************************************|")

class Venta(object):
    """Esta es la clase Ventas"""
    
    def __init__(self, can, tip, met):
        self.__Can = can
        self.__Tip = tip
        self.__Met = met

    def getCan(self):
        return self.__Can

    def getTip(self):
        return self.__Tip

    def getMet(self):
        return self.__Met

    def opcion(self, acc):
        valor = 0
        v = ""
        print("Calculando....")
        time.sleep(1)
        if self.__Tip == 1:
            valor = self.__Can * 1000
        elif self.__Tip == 2:
            valor = self.__Can * 2000
        if acc == 0:
            v = str(input(f"El valor a pagar es de --> ${valor}. desea realizar la compra? [s/n] -->"))
        elif acc == 1:
            v = str(input(f"El valor a pagar es de --> ${valor} + $10000 del envio ${valor+10000}. desea realizar la compra? [s/n] -->"))
        if v == "S" or  v == "s":
            time.sleep(1)
            return 1
        else: return 0

class vent_Ventana(Venta, Jugo):
    """Esta es la clase Venta por Ventana"""

    def __init__(self, can, tip, met):
        Venta.__init__(self, can, tip, met)
        self.__Can = can
        self.__Tip = tip
        self.__Met = met

    def Promo(self, can):
        if can == 5:
            return True
        else:
            return False

    def realizarVenta(self, acc):
        if self.__Tip == 1:
            Jugo.venjNatu(self, self.__Can + acc)
        elif self.__Tip == 2:
            Jugo.venjno_Natu(self, self.__Can + acc)

    def compra(self):
        v = Venta.opcion(self, 0)
        if v == 1:
            print(f"\nRealizando venta...\n")
            time.sleep(1)
            if vent_Ventana.Promo(self, self.__Can) == True:
                vent_Ventana.realizarVenta(self, 1)
                print(f"Venta Exitosa...")
                return ([self.__Can, 1, self.__Tip, self.__Met,
                                     '***', '***'])
            elif vent_Ventana.Promo(self, self.__Can) == False:
                vent_Ventana.realizarVenta(self, 0)
                print(f"Venta Exitosa...")
                return ([self.__Can, 0, self.__Tip, self.__Met,
                         '***', '***'])
        elif v == 0:
            time.sleep(1)
            print(f"\nCompra cancelada!\n")

class vent_distacia(Venta, Jugo):
    """Esta es la clase venta por Distacia"""

    def __init__(self, can, tip, met, dir, fec):
        Venta.__init__(self, can, tip, met)
        self.__Can = can
        self.__Tip = tip
        self.__Met = met
        self.__Dir = dir
        self.__Fec = fec

    def Promo(self):
        if self.__Can >= 20 and self.__Can <= 30:
            return True
        else:
            return False

    def realizarVenta(self, acc):
        if self.__Tip == 1:
            Jugo.venjNatu(self, self.__Can + acc)
        elif self.__Tip == 2:
            Jugo.venjno_Natu(self, self.__Can + acc)

    def compra(self):
        v = Venta.opcion(self, 1)
        if v == 1:
            print(f"\nRealizando venta...\n")
            time.sleep(1)
            if vent_distacia.Promo(self) == True:
                vent_distacia.realizarVenta(self, 1)
                print(f"Venta Exitosa...")
                return ([self.__Can, 1, self.__Tip, self.__Met, self.__Dir,
                                     self.__Fec])# Cantidad, Promo, Tipo, Metodo, Direccion, fecha
            elif vent_distacia.Promo(self) == False:
                vent_distacia.realizarVenta(self, 0)
                print(f"Venta Exitosa...")
                return ([self.__Can, 0, self.__Tip, self.__Met, self.__Dir,
                         self.__Fec])  # Cantidad, Promo, Tipo, Metodo, Direccion, fecha
        elif v == 0:
            time.sleep(1)
            print(f"\nCompra cancelada!\n")
            return 0

#***********************************************************************************************************

from datetime import datetime
import time

def menu():
    time.sleep(1)
    op = int(input((f"\n|================|\n"
                    f"|    --menu--    |\n"
                    f"|================|\n"
                    f"| [1] Venta V    |\n"
                    f"| [2] Venta D    |\n"
                    f"| [3] Reabastecer|\n"
                    f"| [4] Historial  |\n"
                    f"| [5] resultados |\n"
                    f"| [0] Salir      |\n"
                    f"|================|\n"
                    f"    Opción --> ")))
    return op

def mostrar(hist, hist_reab):
    m = hist
    r = hist_reab
    print(f'\n                      HISTORIAL \n'
          f'|-------------------------------------------------------------------|\n'
          f'| Cantidad | Promo | Tipo |   Metodo    |  Dirección   |    Hora    |\n'
          f'|----------|-------|------|-------------|--------------|------------|')
    for i in range(0, len(hist)):
        print(f'|{"%9s" % m[i][0]} | {"%5s" % m[i][1]} | {"%4s" % m[i][2]} | {"%9s" % m[i][3]} | {"%12s" % m[i][4]} | '
              f'{"%10s" % m[i][5]} ')
        print(f'|----------|-------|------|-------------|--------------|------------|\n')

    print(f'\n     REABASTECIMIENTO \n'
          f'|-------------------------------|\n'
          f'| Cantidad |  Tipo |    Hora    |\n'
          f'|----------|-------|------------|')
    for i in range(0, len(hist_reab)):
        print(f'|{"%9s" % r[i][0]} |  {"%4s" % r[i][1]} | {"%10s" % r[i][2]} ')
        print(f'|----------|-------|------------|')

def resultado(hist, hist_reab):
    m = hist
    mostrar(hist, hist_reab)
    ventana = 0
    distancia = 0
    cont = 0
    talNatu = 0
    talno_Natu = 0
    prom = 0
    met = 0
    time.sleep(1)
    for i in range(0, len(hist)):
        if m[i][4] == '***':
            ventana += m[i][0]
        elif m[i][4] != '***':
            distancia += m[i][0]
            cont += 1
        if m[i][2] == 1:
            talNatu += m[i][0]
        elif m[i][2] == 2:
            talno_Natu += m[i][0]
        if m[i][1] == 1:
            prom += 1
        if m[i][3] == 'Electronico':
            if m[i][2] == 1:
                met += m[i][0] * 1000
            elif m[i][2] == 2:
                met += m[i][0] * 2000
    total = (talNatu * 1000) + (talno_Natu * 2000) + (cont * 10000)
    print(f'\n                     RESULTADOS \n'
          f'|------------------------------------------------------|\n'
          f'| Ventana | Distancia | Ven Natu | Ven No_Natu | Total |\n'
          f'|---------|-----------|----------|-------------|-------|')
    print(f'|{"%8s" % ventana} | {"%9s" % distancia} | {"%8s" % talNatu} | {"%11s" % talno_Natu} | {"%10s" % total} ')
    print(f'|---------|-----------|----------|-------------|-------|\n')
    print('')
    print(f'\n  RESULTADOS X TIPO \n'
          f'|-----------------------------|\n'
          f'|  Ven Natural  |  Ven No_Natu  |\n'
          f'|---------------|---------------|')
    print(f'| {"%15s" % talNatu * 1000}| {"%11s" % talno_Natu * 2000} |')
    print(f'|---------------|---------------|\n')
    print('')
    time.sleep(1)
    print(f'\n  RESULTADOS X METODO \n'
          f'|-------------------------------|\n'
          f'|    Efectivo   |  Electronico  |\n'
          f'|---------------|---------------|')
    print(f'| {"%15s" % (total - met)}| {"%11s" % met} |')
    print(f'|---------------|---------------|\n')
    print('')
    time.sleep(1)
    print(f"La cantidad de ventas con promocion fueron --> {prom}\n")
    time.sleep(1)
    print("\nEl inventario quedo de la siguiente manera:\n")
    print(str(juice))

def venta(acc, tip, qui, v):
    if acc == 1:
        while True:
            print(f"La cantidad de jugos {qui} es --> {v}")
            can = int(input(f"Cuantos jugos desea llevar --> "))
            if can <= 0:
                print(f"Error la cantidad debe ser mayor a '0'.")
            else: break
        if juice.verifica(can, tip) == 1:
            comp = vent_Ventana(can, tip, 'Efectivo')
            info = comp.compra()
            return info
        elif juice.verifica(can, tip) == 0:
            print(f"Error cantidades insuficientes verifique disponibilidad o reabasteca desde la bodega...")
        elif juice.verifica(can, tip) == -1:
            print(f"La cantidad de la venta aplica para una promoción pero las cantidades son insuficientes "
                  f"verifique disponibilidad o reabasteca desde la bodega...")
    elif acc == 2:
        while True:
            print(f"La cantidad de jugos {qui} es --> {v}")
            can = int(input(f"Cuantos jugos desea llevar --> "))
            if can <= 0:
                print(f"Error! La cantidad debe ser mayor a '0'.")
            else:
                break
        met = int(input(f"Cual es el metodo de pago? [1] Efectivo [2] Electronico --> "))
        if met == 1:
            met = 'Efectivo'
        elif met == 2:
            met = 'Electronico'
        while True:
            dir = str(input(f"Cual es la direccion? --> "))
            if dir == '':
                print(f"Error! Debe a ver una dirección.")
            else: break
        now = datetime.now()
        fec = now.time()
        if juice.verifica(can, tip) == 1:
            comp = vent_distacia(can, tip, met, dir, fec)
            info = comp.compra()
            return info
        elif juice.verifica(can, tip) == 0:
            print(f"Error cantidades insuficientes verifique disponibilidad o reabasteca desde la bodega...")
        elif juice.verifica(can, tip) == -1:
            print(f"La cantidad de la venta aplica para una promoción pero las cantidades son insuficientes "
                  f"verifique disponibilidad o reabasteca desde la bodega...")

print("Bienvenido\n")
jnatu = int(input(f" Jugos naturales listos?        --> "))
jno_natu = int(input(f" Jugos No naturales listos?     --> "))
bodnatu = int(input(f" Jugos naturales en bodega?     --> "))
bodno_natu =int(input(f" Jugos No naturales en bodega?  --> "))
juice = Jugo(jnatu, jno_natu, bodnatu, bodno_natu)
print(end="\nRegistrando.")
for i in range(0,4):
    time.sleep(0.5)
    print(".", end="")
print('')
time.sleep(1)
print(f"\nRegistro exito...")

hist = []
hist_reab = []
while True:
    op = menu()
    v1 = juice.getjNatu()
    v2 = juice.getjno_Natu()
    if op == 1:
        tip = int(input(f"Que tipo desea [1] natural \n"
                        f"               [2] No Naturales\n"
                        f"                        Opción --> "))
        if tip == 1:
            info = venta(1, tip, 'Naturales', v1)
            hist.append(info)
        elif tip == 2:
            info = venta(1, tip, 'No Naturales', v2)
            hist.append(info)
    elif op == 2:
        tip = int(input(f"Que tipo desea [1] natural \n"
                        f"               [2] No Naturales\n"
                        f"                        Opción --> "))
        if tip == 1:
            info = venta(2, tip, 'Naturales', v1)
            hist.append(info)
        elif tip == 2:
            info = venta(2, tip, 'No Naturales', v2)
            hist.append(info)
    elif op == 3:
        while True:
            op1 = int(input(f"|==============================================|\n"
                            f"| [1] Mostrar cantidades en local y bodega     |\n"
                            f"| [2] Reabastecer                              |\n"
                            f"| [0] Salir                                    |\n"
                            f"|==============================================|\n"
                            f"          Opción --> "))
            if op1 == 1:
                print(str(juice))
            elif op1 == 2:
                tip = int(input(f"Que tipo desea reabastecer  [1] natural \n"
                                f"                            [2] No Naturales\n"
                                f"                               Opción --> "))
                can = int(input(f"Cuantos jugos desea reabastecer --> "))
                #juice.verifica(2, can, tip)
                rta = juice.reabastecer(can, tip)
                if rta == 1:
                    now = datetime.now()
                    fec = now.time()
                    hist_reab.append([can, tip, fec])
            elif op1 < 0 or op1 > 2:
                print(f"Error opción no validad!")
            elif op1 == 0:
                break
    elif op == 4:
        print(end="\nProcesando.")
        for i in range(0, 4):
            time.sleep(0.5)
            print(".", end="")
        print('')
        time.sleep(1)
        mostrar(hist, hist_reab)
    elif op == 5:
        print(end="\nProcesando.")
        for i in range(0, 4):
            time.sleep(0.5)
            print(".", end="")
        print('')
        time.sleep(1)
        resultado(hist, hist_reab)
    elif op == 0:
        time.sleep(1)
        print(f"Ten buen resto de dia 😊👍👋")
        break
    elif op != (1,2,3,4,5,0):
        time.sleep(1)
        print(f"Error! Opcion no validad...")