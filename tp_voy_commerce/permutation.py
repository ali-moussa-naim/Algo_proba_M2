import random
import math
from itertools import permutations
import matplotlib as plt

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

    for i in range(limite):
        # Permutation aléatoire
        l_perm = gen_permutation(n)

        # On vérifie si la permutation est déjà dans la liste ou non
        while(l_perm in l_res):
            l_perm = gen_permutation(n)
        
        l_res.append(l_perm)
    
    return l_res

"""
Fonction qui génère toutes les permutations avec itertools
n : entier, nombre d'éléments dans la liste
"""
def gen_all_permutation_itertools(n):
    l_res = []
    liste_perm = list(range(n))
    

    for p in liste_perm:
        print(p)

    return permutations(liste_perm)

"""
Fonction qui compare les résultats entre les 2 méthodes de générations de permutation
n : entier, nombre d'éléments dans une liste
"""
def comp_l_perm(n):
    l_perm = gen_all_permutation(n)
    l_perm_itertools = gen_all_permutation_itertools(n)

    # On vérifie si on a les mêmes tailles
    if(len(l_perm) != len(l_perm_itertools)):
        print("Les 2 listes n'ont pas le même nombre de permutation")
        return False

    comp = False
    for i in range(len(l_perm)):
        for j in range(len(l_perm)):
            pass
    
    return None

"""
Fonction qui trace le graphe
n : entier, nombre d'éléments dans la liste
"""
def display_fig_perm(n):
    pass



n = 8
l_all_perm = gen_all_permutation(n)

print(l_all_perm)
print("Nombre de permutation =", len(l_all_perm))

print("\n")
#l_all_perm_itertools = gen_all_permutation_itertools(n)
#print("Permutations naïve = Permutations itertools:", sorted(l_all_perm) == sorted(l_all_perm_itertools))