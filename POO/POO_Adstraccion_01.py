class Factura:
     __tasa = 19
     def __init__(self, unidad, precio):
         self.unidad = unidad
         self.precio = precio
     def por_pagar(self):
         total = self.unidad * self.precio
         impuesto = total * Factura.__tasa / 100
         return(total + impuesto)

compra1 = Factura(12, 110)
print (compra1.unidad)
print (compra1.precio)

print (compra1.por_pagar(), "bitcoins")

#print (Factura.__tasa)  no se puede xq ese dato esta protegido
print (compra1._Factura__tasa)

###############################################################################
# sobrecarga de metodos

class Persona():
     def __init__(self):
         self.cedula = 13765890
     def mensaje(self):
         print("mensaje desde la clase Persona")

class Obrero(Persona):
     def __init__(self):
         self.__especialista = 1

     def mensaje(self):  # ESTE METODO ES LLAMADO SOLO SI SE ENCUNTRE DE LO CONTRARIO
         print("mensaje desde la clase Obrero") # SE LLAMARA AL DE LA CLASE PERSONA.

obrero_planta = Obrero()
print (obrero_planta.mensaje())


###############################################################################
# sobrecarga de OPERACIONES

class Punto:
     def __init__(self,x = 0,y = 0):
         self.x = x
         self.y = y
     def __add__(self,other):
         x = self.x + other.x
         y = self.y + other.y
         return x, y

punto1 = Punto(4,6)
punto2 = Punto(1,-2)
print (punto1 + punto2)