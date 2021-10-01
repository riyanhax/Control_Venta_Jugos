import time
import numpy as np
import sys
# imprimir con retraso
def icr(s):
    # imprimir letra por letra
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
# crear la clase
class pokemon:
    def __int__(self, nombre, tipos, movimientos, EVs, vida='==================='):
        # guardar los valores como atributos
        self.nombre = nombre
        self.tipos = tipos
        self.movimientos = movimientos
        self.ataque = EVs['Ataque']
        self.defensa = EVs['Defensa']
        self.vida = vida
        self.barras = 20
    def impresa(self, pokemon2):
        print('---------BATALLA DE POKEMON----------')
        print(f'\n{self.nombre}')
        print('tipo/', self.tipos)
        print('ataque', self.ataque)
        print('defensa', self.defensa)
        print('Nv./', 3*(1+np.mean([self.ataque,self.defensa])))
        print('\nVS')
        print('tipo/', pokemon2.tipos)
        print('ataque', pokemon2.ataque)
        print('defensa', pokemon2.defensa)
        print('Nv./', 3 * (1 + np.mean([pokemon2.ataque, pokemon2.defensa])))
        time.sleep(2)
    def ventajas(self,pokemon2):
        version =  ['fuego', 'agua', 'planta']
        for i,k in enumerate(version):
            if self.tipo == k:
                if pokemon2.tipos == k:
                    ataque_1 = '\n no es muy efectivo'
                    ataque_2 = '\n no es muy efectivo'
                if pokemon2.tipos == version[(i+1)%3]:
                    pokemon2.ataque *= 2
                    pokemon2.defensa *= 2
                    self.ataque /= 2
                    self.defensa /= 2
                    ataque_1 = '\n no es muy efectivo'
                    ataque_2 = '\n es muy efectivo'
                if pokemon2.tipos == version[(i+2)%3]:
                    self.ataque *= 2
                    self.defensa *= 2
                    pokemon2.ataque /= 2
                    pokemon2.defensa /= 2
                    ataque_1 = '\n no es muy efectivo'
                    ataque_2 = '\n es muy efectivo'
            return ataque_1, ataque_2
    def turno(self, pokemon2, ataque_1, ataque_2):
        while (self.barras > 0) and (pokemon2.barras > 0):
            print(f'\n{self.nombre}\t\tPS\t{self.vida}')
            print(f'\n{pokemon2.nombre}\t\tPS\t{pokemon2.vida}')
            print(f'Adelante {self.nombre}')
            for i, x in enumerate(self.movimientos):
                print(f'{i+1}.',x)
            index = int(input(f'elige un movimiento :'))
            icr(f'\n{self.nombre} uso {self.movimientos[index-1]}')
            time.sleep(1)
            icr(ataque_1)