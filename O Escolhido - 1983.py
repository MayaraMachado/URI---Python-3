n= int(input())
a= {}
if (3<=n<=100):
    loop=1
    while loop!= n+1:
        x,y= map(int, input().split())
        a= dict([x])
        a[x]=y
        loop+=1
    for a in range(0,n):
        print(a)
        
