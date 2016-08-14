a,b,c= map(float, input().split())
if (a>0) and (b>0) and (c>0):
    if ((c-b)<a<(c+b))and((b-a)<c<(b+a))and((c-a)<b<(c+a)):
        per= a+b+c
        print("Perimetro = %.1f" %per)
    else:
        area=((a+b)*c)/2
        print("Area = %.1f" %area)      
else:
    area=((a+b)*c)/2
    print("Area = %.1f" %area)
