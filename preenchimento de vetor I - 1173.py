V=int(input())
N=[]
if (V==1):
    N.append(V)
    X=V+1
    i=0
    print("N[%d] = %d" %(i,V))
    N.append(X)
    i=i+1
    print("N[%d] = %d" %(i,X))    
else:
    N.append(V)
    i=0
    print("N[%d] = %d" %(i,V))
    X=V*2
    N.append(X)
    i=i+1
    print("N[%d] = %d" %(i,X))
for i in range(2,11):
    X=X*2
    N.insert(i,X)
    print("N[%d] = %d" %(i,X))

    
    
