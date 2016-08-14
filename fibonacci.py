p=0
s=1
fibo=[p,s]
a=int(input())
for i in range(2,60):
    t=s+p
    p=s
    s=t
    fibo.append(t)
a,b,c,d,e=fibo[0:a]
print(a,b,c,d,e)
    
