L=1
R=1
while (L!=0)and(R!=0):
    sl=0
    sr=0
    L,R=map(int,input().split())
    if L!=0 and R!=0:
        sl+=L
        sr+=R
        print(sl+sr)
    
