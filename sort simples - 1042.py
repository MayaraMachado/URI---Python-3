a,b,c= map(int,input().split())
if(a>b>c):
    print("%d\n%d\n%d\n\n%d\n%d\n%d" %(c,b,a,a,b,c))
elif(a>c>b):
    print("%d\n%d\n%d\n\n%d\n%d\n%d" %(b,c,a,a,b,c))
elif(b>a>c):
    print("%d\n%d\n%d\n\n%d\n%d\n%d" %(c,a,b,a,b,c))
elif(b>c>a):
    print("%d\n%d\n%d\n\n%d\n%d\n%d" %(a,c,b,a,b,c))
elif(c>a>b):
    print("%d\n%d\n%d\n\n%d\n%d\n%d" %(b,a,c,a,b,c))
elif(c>b>a):
    print("%d\n%d\n%d\n\n%d\n%d\n%d" %(a,b,c,a,b,c))
