l=[]
for i in range(5):
    l.append(float(input()))

for i in range(5):
    if l[i]<=10:
        print("l[%d] = %.1f" %(i,l[i]))
