S,T,F = map(int,input().split())
if S==0:
    S=24
chegada= S+T+F
if chegada>24:
    chegada=chegada-24
    print(chegada)
elif chegada==24:
    chegada=0
    print(chegada)
else:
    print(chegada)
