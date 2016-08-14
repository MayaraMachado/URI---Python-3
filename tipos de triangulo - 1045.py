a,b,c = map(float, input().split())
if(a>b>c)or(a==b>c)or(a==b>c) or(a==b==c):
    A=a
    B=b
    C=c
elif(a>c>b)or(a==c>b)or(a>c==b):
    A=a
    B=c
    C=b
elif(b>a>c)or(b==a>c)or(b>a==c):
    A=b
    B=a
    C=c
elif(b>c>a)or(b==c>a)or(b>c==a):
    A=b
    B=c
    C=a
elif(c>a>b)or(c==a>b)or(c>a==b):
    A=c
    B=a
    C=b
elif(c>b>a)or(c==b>a)or(c>b==a):
    A=c
    B=b
    C=a

if(A>=B+C):
    print("NAO FORMA TRIANGULO")
else:
    if(A**2 == B**2+C**2):
        print("TRIANGULO RETANGULO")
    if(A**2>B**2+C**2):
        print("TRIANGULO OBTUSANGULO")
    if(A**2<B**2+C**2):
        print("TRIANGULO ACUTANGULO")
    if(A==B==C):
        print("TRIANGULO EQUILATERO")
    elif(A==B):
        print("TRIANGULO ISOSCELES")
    elif(A==C):
        print("TRIANGULO ISOSCELES")
    elif(B==C):
        print("TRIANGULO ISOSCELES")
