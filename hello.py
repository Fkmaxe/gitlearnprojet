stop = False
while stop != True :
    var = int(input("Entrez un nombre ? :"))
    print(var)
    for i in range(1,11):
        temp = var*i
        print(temp)
    a = input("voulez vous continuez ? oui ou non ? :")
    if a == "non" :
        stop = True
