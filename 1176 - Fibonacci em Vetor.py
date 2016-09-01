fibo=[0,1]
p=0
s=1
for i in range(60):
    t=s+p
    fibo.append(t)
    p=s
    s=t
T= int(input())
for i in range(T):
    N=int(input())
    print('Fib(%d) = %d' %(N, fibo[N]))
