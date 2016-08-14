a= float(input())
if (0<a<=400):
    rea=(((a*15)/100)+a)
    perc= 15
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea-a))
    print("Em percentual: " + str(perc) + " %")
elif(400<a<=800):
    rea=(((a*12)/100)+a)
    perc= 12
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea-a))
    print("Em percentual: " + str(perc) + " %")
elif(800<a<=1200):
    rea=(((a*10)/100)+a)
    perc= 10
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea-a))
    print("Em percentual: " + str(perc) + " %")
elif(1200<a<=2000):
    rea=(((a*7)/100)+a)
    perc= 7
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea-a))
    print("Em percentual: " + str(perc) + " %")
else:
    rea=(((a*4)/100)+a)
    perc= 4
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea-a))
    print("Em percentual: " + str(perc) + " %")
