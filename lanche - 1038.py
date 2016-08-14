a,b = map(int, input().split())
if (a==1):
    total= b*4
    print("Total: R$ %.2f" %total)
elif(a==2):
    total = b*4.50
    print("Total: R$ %.2f" %total)
elif(a==3):
    total= b*5
    print("Total: R$ %.2f" %total)
elif(a==4):
    total=b*2
    print("Total: R$ %.2f" %total)
elif(a==5):
    total=b*1.5
    print("Total: R$ %.2f" %total)
    
