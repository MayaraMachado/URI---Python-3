from math import sqrt
a,b,c=map(float, input().split())
if a!=0:
    r1=((-(b)+(sqrt((b*b)-(4*a*c))))/2*a)/100
    print("R1 = %.5f" %r1)
    r2=((-(b)-(sqrt((b*b)-(4*a*c))))/2*a)/100
    print("R2 = %.5f" %r2)
elif (a==0):
    print("Impossivel calcular")
