T=int(input())
anos=0
for n in range(1, T+1):
    PA,PB,G1,G2=(input().split())
    while (PA<PB):
        anos= anos + 1
        PA=int(PA)+(int(PA)*(round(float(G1))/100))
        PB=int(PB)+(int(PB)*(round(float(G2))/100))
    print(anos+1)
