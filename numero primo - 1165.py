N=int(input())
for i in range(N): 
    X=int(input())
    soma=0
    for t in range(1,X):
        if(X%t==0):
            soma=soma+i
            print(t)
    if (soma>2):
        print(X,"nao eh primo")
    else:
        print(X,"eh primo")
