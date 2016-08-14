X=[]
for i in range(10):
    a=int(input())
    if(a<=0):
        a=1
        X.append(a)
    else:
        X.append(a)
    print("X[%d] = %d" %(i,a))
