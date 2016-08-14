l=[]
somas=0
soman=0
a=int(input())
for n in range (1,(a+1)):
    l.append(input())
for n in l:
    if (10<=int(n)<=20):
        somas+=1
    elif (int(n)>20) or(int(n)<10):
        soman+=1
print(somas,"in")
print(soman,"out")
