"""
2. Realice un programa que dados 3 números retorne el mayor el mayor,  el menor y el del medio
"""
print("digite los valores :")
v1 = int(input())
v2 = int(input())
v3 = int(input())

if v1>v2 and v1>v3:
    if v2>v3:
        print("el numero mayor es el : ", v1,", el menor es el : ",v3," y el medio es : ",v2)
    else:
        print("el numero mayor es el : ", v1, ", el menor es el : ", v2, " y el medio es : ", v3)
elif v2>v1 and v2>v3:
    if v1 > v3:
         print("el numero mayor es el : ", v2,", el menor es el : ",v3," y el medio es : ",v1)
    else:
        print("el numero mayor es el : ", v2, ", el menor es el : ", v1, " y el medio es : ", v3)
elif v3>v1 and v3>v2:
    if v1>v2:
        print("el numero mayor es el : ", v3, ", el menor es el : ", v2, " y el medio es : ", v1)
    else:
        print("el numero mayor es el : ", v3, ", el menor es el : ", v1, " y el medio es : ", v2)

