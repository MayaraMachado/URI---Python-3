from math import sqrt
a=int(input())
p = 1
primos = [2]
for numero in range(3,a+1):
    ehprimo = 1
    for i in primos:
        if numero % i == 0:
            ehprimo = 0
            print("nao primo")
            break
        if i > sqrt(numero):
            break
    if (ehprimo):
        primos.append(numero)
        print ("primo")
        p += 1
