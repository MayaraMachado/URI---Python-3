soma=0
a=int(input())
b=int(input())
if (b>a):
    for n in range(a,(b+1)):
        if (n%13!=0):
            soma+=n
if (a>b):
    for n in range(b,(a+1)):
        if (n%13!=0):
            soma+=n
print(soma)
