def identificar(sig, nums):
    r = []
    aux = 0
    for i in range(len(nums)):
        if sig == nums[i]:
            aux += 1
            r.append(i)
    if aux > 0:
        return [True] + r
    else:
        return [False]

def calculadora(numeros):
    aux = 0
    res = 0
    while True:
        i = 1
        r = identificar('*', numeros)
        while True:
            if r[0] == True:
                res = numeros[r[i] - 1] * numeros[r[i] + 1]
                numeros[r[i] - 1] = res
                print(res)
                print(numeros)
                i += 1
            if r[0] == False:
                break
            print(r)
        print(res)
        print(numeros)
        break
numeros = [1,'*',2,'*',2]
calculadora(numeros)
