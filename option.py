A = int(input("entrer la valeur A :"))
B = int(input("entrer la valeur B :"))
option = int(input("entrer option : (1_4)"))
if option < 1 or option > 4 :
    print("invalide")
    elif option == 1 :
        print(A+B)
    elif option == 2 :
        print(A-B)
    elif option == 3 :
        print(A*B)
    elif option == 4 :
        print(A/B)    
