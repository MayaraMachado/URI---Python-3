resp=1
soma=0
somaE=0
somaI=0
somaG=0
while resp==1:
    a,b=map(int, input().split())
    soma+=1
    if (a>b):
        somaI+=1
    elif(b>a):
        somaG+=1
    elif(a==b):
        somaE+=1
    resp=int(input("Novo grenal (1-sim 2-nao)"))
print("%d grenais"%soma)
print("Inter:%d" %somaI)
print("Gremio:%d"%somaG)
print("Empates:%d"%somaE)
if (somaI>somaG):
    print("Inter venceu mais")
elif (somaG>somaI):
    print("Gremio venceu mais")
elif (somaI==somaG):
    print("Nao houve vencedor")

    
