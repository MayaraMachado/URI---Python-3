n=int(input())
for i in range (n):
    tm=0
    tv=0
    sld1=0
    sld2=0
    m1,c,v1=map(str,input().split())
    v2,c,m2=map(str, input().split())
    if (m1>v1):
        tm+=3
    elif(v1>m1):
        tv+=3
    elif (m1==v1):
        tm+=1
        tv+=1
    if (m2>v2):
        tm+=3
    elif(v2>m2):
        tv+=3
    elif (m2==v2):
        tm+=1
        tv+=1
    if tv>tm:
        print("Time 2")
    elif tm>tv:
        print("Time 1")
    elif (tm==tv):
        if (v1>m1)and(v2>m2):
            print("Time 2")
        elif (m1>v1)and(m2>v2):
            print("Time 1")
        elif (m1>v1)and(m2<v2):
            sld1=(int(m1)-int(v1))+(int(m2)-int(v2))
            sld2=(int(v1)-int(m1))+(int(v2)-int(m2))
            if sld1>sld2:
                print("Time 1")
            elif (sld1<sld2):
                print("Time2")
            elif(sld1==sld2):
                print("Penaltis")
        elif (m1<v1)and(m2>v2):
            sld1=(int(m1)-int(v1))+(int(m2)-int(v2))
            sld2=(int(v1)-int(m1))+(int(v2)-int(m2))
            if sld1>sld2:
                print("Time 1")
            elif (sld1<sld2):
                print("Time2")
            elif(sld1==sld2):
                print("Penaltis")
        elif (m1==v1)and(v2==m2):
            if v1>m2:
                print("Time 2")
            elif (m2>v1):
                print("Time 1")
            elif (m2==v1):
                print("Penaltis")
    

    
