N=1
while (N!=0):
    N=int(input())
    if (N!=0):
        s1=0
        s2=0
        for i in range(N):
            A,B=map(int, input().split())
            if A>B:
                s1=s1+1
            elif A<B:
                s2+=1
        print(s1,s2)
