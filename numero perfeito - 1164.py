a=int(input())
for i in range(a):
    soma=0
    X=int(input())
    for t in range(1,X):
        if(X%t==0):
            soma=soma+t
            print(t)
    if (soma==X):
        print(X,"eh perfeito")
    else:
        print(X,"nao eh perfeito")
