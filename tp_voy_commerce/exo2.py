from itertools import permutations
import math

"""
Fonction qui génère des permutations selon l'algo dans le livre de Knuth
"""
def gen_knuth(L, directions):
    n = len(L)
    max_actif = -1
    idx_max = -1

    # Chercher le plus grand élément actif M
    for i in range(n):
        voisin = i + directions[i]
        if 0 <= voisin < n and L[i] > L[voisin]:
            if L[i] > max_actif:
                max_actif = L[i]
                idx_max = i

    # Plus aucun élément actif 
    if idx_max == -1:
        return None

    # Transposer M et sa direction avec son voisin
    cible = idx_max + directions[idx_max]
    L[idx_max], L[cible] = L[cible], L[idx_max]
    directions[idx_max], directions[cible] = directions[cible], directions[idx_max]

    # Inverser les directions des éléments > M
    for i in range(n):
        if L[i] > max_actif:
            directions[i] = -directions[i]

    return (idx_max, cible)

"""
Fonction qui génère toutes les permutations avec itertools
n : entier, nombre d'éléments dans la liste
"""
def gen_all_permutation_itertools(n):
    l_res = []
    liste_perm = list(range(n))
    liste_perm = permutations(liste_perm)
    l_res = [list(p) for p in liste_perm]
    return l_res, len(l_res)

#---------------------Test----------------------------------
"""
for n in range(1, 6):
    print("Itération numéro", n)
    print("\n")

    L = list(range(n))
    directions = [-1] * n

    l_perm_iter = gen_all_permutation_itertools(n)
    print("Permutations avec itertools:")
    print(l_perm_iter)

    cpt = 1
    limite = math.factorial(n)

    print("\n")

    print("Permutations avec algo:")
    print(L)
    # Affichage de toutes les permutations sans les stocker
    while gen_knuth(L, directions):
        cpt += 1
        print(L)

    if(cpt != limite):
        print("Les permutations ne sont pas toutes générées.")
    else:
        print("Toutes les permutations ont été générées.")

    print("\n")


# Exemple minimal du bug (sans copie)
L = [0, 1, 2]
directions = [-1, -1, -1]
resultats = []

resultats.append(L)

while gen_knuth(L, directions):
    resultats.append(L)  

print("Résultat :", resultats)

print("\n")

L = [0, 1, 2]
directions = [-1, -1, -1]
resultats = []

resultats.append(L.copy())

while gen_knuth(L, directions):
    resultats.append(L.copy())

print("Résultat :", resultats)
"""

n = 3
L = list(range(n))
directions = [-1] * n

print("Initial :", L)
echange = gen_knuth(L, directions)
while echange is not None:
    print(f"Échange indices {echange} -> {L}")
    echange = gen_knuth(L, directions)