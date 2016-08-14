c1=input()
c2=input()
c3=input()
if (c1=="vertebrado"):
    if (c2=="ave"):
        if(c3=="carnivoro"):
            print("aguia")
        elif(c3=="onivoro"):
            print("pomba")
    elif(c2=="mamifero"):
        if(c3=="onivoro"):
            print("homem")
        elif(c3=="herbivoro"):
            print("vaca")
elif(c1=="invertebrado"):
    if(c2=="inseto"):
        if(c3=="hematofago"):
            print("pulga")
        elif(c3=="herbivoro"):
            print("lagarta")
    elif(c2=="anelideo"):
        if(c3=="hematofago"):
            print("sanguessuga")
        elif(c3=="onivoro"):
            print("minhoca")
        
