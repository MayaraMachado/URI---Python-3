p=0
s=1
fibo=[p,s]
for i in range(2,46):
    t=s+p
    p=s
    s=t
    fibo.append(t)
a=int(input())
for i in range(0,a):
    print('', end='')
    print(fibo[i])

