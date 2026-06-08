tableau = []
max_val = None
min_val = None
print("remplissage du tableau")
for i in range(1 ,11) :
    N = int(input(f"input(entrer N n°{i} : "))
    tableau.append(N)
    #print(f"taille tableau: {len(tableau)}")
    if max_val is None or N > max_val :
        max_val = N 
    if min_val is None or N < min_val :
       min_val = N
print(f"le plus petit : {min_val}")
print(f"le plus grand : {max_val}")
print(f"tableau complet : {tableau}")