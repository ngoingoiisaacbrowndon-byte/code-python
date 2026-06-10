tableau_complet = []
tableau_pairs = []
print("Remplissage du tableau :")

for i in range(1, 15):
    N = int(input(f"Entrez le nombre n°{i} : "))
    if N < 0:
        print("Invalide")
    else:
        tableau_complet.append(N)
        if N % 2 == 0:
            tableau_pairs.append(N)
print(" RÉSULTATS ")
print(f"tableau_complet : {tableau_complet}")
print(f"tableau_pairs   : {tableau_pairs}")