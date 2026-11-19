import random
import math
from itertools import permutations
import matplotlib.pyplot as plt

"""
Fonction qui génère une permutation pour une liste de taille n
n : entier, nombre d'éléments dans la liste
"""
def gen_permutation(n):
    # On génère la liste de taille n [0, 1, ..., n - 1]
    liste_perm = list(range(n))

    for i in range(n):
        indice_alea = random.randint(0, n - 1) 
        liste_perm[i], liste_perm[indice_alea] = liste_perm[indice_alea], liste_perm[i]

    return liste_perm

"""
Fonction pour générer toutes les permutations de taille n
n : entier, nombre d'éléments dans la liste
"""
def gen_all_permutation(n):
    l_res = []
    limite = math.factorial(n)
    cpt = 0

    for i in range(limite):
        # Permutation aléatoire
        l_perm = gen_permutation(n)

        # On prend une permutation tant qu'elle est déjà dans la liste
        while(l_perm in l_res):
            l_perm = gen_permutation(n)

        l_res.append(l_perm)
        cpt += 1

    return l_res, cpt

"""
Fonction qui génère toutes les permutations avec itertools
n : entier, nombre d'éléments dans la liste
"""
def gen_all_permutation_itertools(n):
    l_res = []
    liste_perm = list(range(n))
    liste_perm = permutations(liste_perm)
    cpt = 0

    for p in liste_perm:
        cpt += 1

    return liste_perm, cpt


"""
Fonction qui réalise N mélanges et compte les fréquences
n : entier, nombre d'éléments pour la permutation
N : entier, valeur de la fréquence
"""
def calcul_frequences(n, N):
    toutes_perm = list(permutations(range(n)))
    effectifs = [0] * len(toutes_perm)

    for i in range(N):
        p = tuple(gen_permutation(n))
        rang = toutes_perm.index(p)
        effectifs[rang] += 1

    frequences = [e / N for e in effectifs]

    return frequences

"""
Fonction qui trace le graphe
n : entier, nombre d'éléments dans la liste
"""

def display_fig_perm(n, frequences, N):
    limite = math.factorial(n)

    plt.figure(figsize=(16, 5))

    # Tracé des fréquences
    plt.bar(range(limite), frequences, width=0.8)

    # Fréquence théorique si le mélange est uniforme
    plt.axhline(y=1/limite, color='red', linestyle='--',
                label="Fréquence théorique (1/120)")

    plt.xlim(0, limite)
    plt.ylim(0, max(max(frequences) * 1.1, 1/limite * 1.2))

    plt.xlabel("Rang de la permutation")
    plt.ylabel("Fréquence")
    plt.title(f"Fréquences des permutations pour N = {N}")

    plt.legend()
    plt.grid(axis='y')
    plt.show()

"""
Fonction qui génère toutes les permutations sans biais
n : entier, nombre d'éléments dans la liste
"""
def gen_permutation_uniforme(n):
    liste_perm = list(range(n))
    for i in range(n - 1):
        indice_alea = random.randint(i, n - 1)  
        liste_perm[i], liste_perm[indice_alea] = liste_perm[indice_alea], liste_perm[i]
    return liste_perm


n = 7
l_all_perm1, cpt1 = gen_all_permutation(n)
l_all_perm, cpt = gen_all_permutation_itertools(n)

"""
print("cpt =", cpt1)
print(l_all_perm1)

print("\n")

print("cpt =", cpt)
print(l_all_perm)
"""

"""

for graines in [10, 42, 123, 2026]:
    random.seed(graines)
    for N in [1200, 12000, 120000]:
        frequences = calcul_frequences(5, N)
        display_fig_perm(5, frequences, N)
"""

n = 3
l_perm = gen_permutation_uniforme(3)
print(l_perm)
