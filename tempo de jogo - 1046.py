i,f=map(int, input().split())
if i>f:
    a=24-i
    h=a+f
    print("O JOGO DUROU %d HORA(S)" %h)
elif f>i:
    h=f-i
    print("O JOGO DUROU %d HORA(S)" %h)
elif i==f:
    h=24
    print("O JOGO DUROU %d HORA(S)" %h)
