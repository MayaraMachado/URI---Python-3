n1,n2,n3,n4 = map(float, input().split())
media=((n1*2+n2*3+n3*4+n4)/10)
if (media>=7):
    print("Media: %.1f" %media)
    print("Aluno aprovado.")
elif(6.9>=media>=5):
    print("Media: %.1f" %media)
    print("Aluno em exame.")
    n5= float(input())
    mediaf= (media+n5)/2
    if (mediaf>=5):
        print("Nota do exame: %.1f" %n5)
        print("Aluno aprovado.")
        print("Media final: %.1f" %mediaf)
    else:
        print("Nota do exame: %.1f" %n5)
        print("Aluno reprovado.")
        print("Media final: %.1f" %mediaf)
else:
    print("Media: %.1f" %media)
    print("Aluno reprovado.")
