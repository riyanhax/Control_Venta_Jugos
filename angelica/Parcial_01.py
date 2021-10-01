def CalValor(vec1, vec2, vec3):
    tal = 0
    for i in range(0, len(vec1)):
        tal += (vec1[i] * vec3[i])
        if vec2[i] == "Pesado":
            tal += ((vec1[i] * vec3[i]) * 15) / 100
    return tal
vect1 = [1,2,3,4,5,6,7,8,9]
vect2 = [100000,22000,310000,10000,60000,300000,200000,500000,53000]
vect3 = ["liviano","Pesado","Pesando","liviano","Pesado","liviano","Pesado","Pesado","Pesado"]
vect4 = [10,3,6,12,4,7,3,4,2]
valor = CalValor(vect2,vect3,vect4)
print(f"El inventario tienen un valor de : ${valor}")