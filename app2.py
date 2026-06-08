tableau_A = []
tableau_B = []
intersection = []
print("remplissage du tableau A")
for i in range (1 , 10) :
    N = int(input(f"entrer N n°{i} : "))
    tableau_A.append(N)
print("remplissage du tableau B")    
for i in range (1 , 10) :
    N = int(input(f"entrer N n°{i} : "))
    tableau_B.append(N)
for element in tableau_A:
 if element in tableau_B:
    intersection.append(element)
print(f"tableau_A : {tableau_A} ")
print(f"tableau_B : {tableau_B} ")
print(f"tableau_intersection : {intersection}")