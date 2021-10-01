def llenar(nombre):
    v=[]
    arch = open(nombre,"r")
    lineas = arch.readlines()  # lee todo el archivo
    arch.close()  # cierra el archivo

    t = lineas[0].split(',')  # crea el vector temporal con los string de los numeros=> '33'
    x = len(t)
    for i in range(0,x):
        v.append(int(t[i]))
    return v,x    # retorna el vector y la cantidad de valores
#============================================================

def imprimir(v,n):
    for i in range(0,n):
        print("|",v[i],end=" ")
    print("|")
def factorial(n):
    fac = 1
    for i in range(1,(n+1)):
        fac = fac * i
    return fac
#==========================================
def vfactoriales(v,n):
    f=[]
    i=0
    while(i<n):
        f.append(factorial(v[i]))
        i = i + 1
    return f
#(v,n)=llenar('D:\\Users\\ASUS\\Documentos\\ISER_2\\FUNDAMENTO DE PROGRAMACIÓN\\SOLUCIONES\\Vnumeros2.txt')
(v,n)=llenar(r'D:\Users\ASUS\Documentos\ISER_2\FUNDAMENTO DE PROGRAMACIÓN\SOLUCIONES\Vnumeros2.txt')
print(" valores iniciales del vector:")
imprimir(v,n)
vFacto = vfactoriales(v,n)
print("El vector con sus factoriales es: "+str(vFacto))
