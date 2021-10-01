from random import randint
#================================================
def llenar(v,n):
    for i in range (0,n):
        v[i]=randint(0,100)

#================================================
def burbuja(v,n):
    i = 0
    while (i<n):
      j = i + 1
      while(j<n):
         if(v[i]>v[j]):
            temp = v[i]
            v[i] = v[j]
            v[j] = temp
         j = j + 1
      i=i+1
#================================================
def busecuencial(v,n,dato):
    i=0
    pos = -1
    while(i<n and pos<0):  # Termina cuando NO existan valores por revisar (inf<=sup da FALSE) o se encuentre el dato ya que el valor
                           # de pos pasa de -1 (menor a 0)  por eso pos<0 da FALSE
        if(v[i]==dato): # Si se encuentra el dato pos almacena la posicion almacenada en i
           pos = i
        else:
            i = i + 1
    return pos
#================================================
n=int(input(" Ingrese la longitud del vector"))
#n=20
v=[0]*n
llenar(v,n)
print("Valores del vector: ",v)
burbuja(v,n)
print("Vector ordenado: ",v)

d = int(input("Que valor desea buscar(0 para terminar)? "))
while(d>0):
  x = busecuencial(v,n,d)
  if(x<0):
     print("El dato no esta en el vector")
  else:
     print("El dato esta en la posicion ",x)
  d = int(input("Que valor desea buscar(0 para terminar)? "))