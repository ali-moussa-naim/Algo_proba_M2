import NYcity
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


def recherche_exhaustive(dist):
    n = len(dist)
    L = list(range(n))
    directions = [-1] * n

    pmin = None
    dmin = float('inf')
    nb_perms = 0
    nb_evalues = 0

    while True:
        nb_perms += 1

        # Filtrage des symétries 
        if n < 3 or (L[0] == 0 and L[1] < L[-1]):
            nb_evalues += 1
            longueur = NYcity.calc(L, dist)

            if longueur < dmin:
                dmin = longueur
                pmin = L.copy()  

        if gen_knuth(L, directions) is None:
            break

    return pmin, dmin, nb_perms, nb_evalues


def matrice_manhattan(posx, posy):
    n = len(posx)
    return [
        [abs(posx[i] - posx[j]) + abs(posy[i] - posy[j]) for j in range(n)]
        for i in range(n)
    ]

def verifier_circuit_valide(p, n):
    return (
        isinstance(p, list)
        and len(p) == n
        and set(p) == set(range(n))
    )

def gen_knuth(L, directions):
    n = len(L)
    max_actif, idx_max = -1, -1

    for i in range(n):
        voisin = i + directions[i]
        if 0 <= voisin < n and L[i] > L[voisin]:
            if L[i] > max_actif:
                max_actif, idx_max = L[i], i

    if idx_max == -1:
        return None

    cible = idx_max + directions[idx_max]
    L[idx_max], L[cible] = L[cible], L[idx_max]
    directions[idx_max], directions[cible] = directions[cible], directions[idx_max]

    for i in range(n):
        if L[i] > max_actif:
            directions[i] = -directions[i]

    return (idx_max, cible)


def maj_distance_locale(L, echange, d_precedente, dist):
    n = len(L)
    if n < 3:
        return d_precedente

    # k est l'indice de gauche parmi les deux positions adjacentes échangées
    k = min(echange)

    # Dans L déjà échangé : L[k] = y (nouveau à gauche), L[k+1] = x (nouveau à droite)
    a = L[(k - 1) % n]
    y = L[k]
    x = L[k + 1]
    b = L[(k + 2) % n]

    # Nouvelles arêtes : (a, y) et (x, b) | Anciennes arêtes : (a, x) et (y, b)
    delta = (dist[a][y] + dist[x][b]) - (dist[a][x] + dist[y][b])
    return d_precedente + delta


def verifier_maj_locale(n, afficher_details=True):
    _, _, _, dist = NYcity.init(n)
    L = list(range(n))
    directions = [-1] * n

    d_locale = NYcity.calc(L, dist)
    assert d_locale == NYcity.calc(L, dist)

    nb_transitions = 0
    nb_bords = 0

    while True:
        echange = gen_knuth(L, directions)
        if echange is None:
            break

        nb_transitions += 1
        d_locale = maj_distance_locale(L, echange, d_locale, dist)
        d_exacte = NYcity.calc(L, dist)

        # Contrôle d'égalité stricte à chaque étape
        assert d_locale == d_exacte, (
            f"Écart détecté à l'étape {nb_transitions} sur {L} : "
            f"locale={d_locale} vs calc={d_exacte}"
        )

        # Vérification des échanges touchant le premier (0) ou le dernier (n-1) élément
        touche_bord = (0 in echange) or (n - 1 in echange)
        if touche_bord:
            nb_bords += 1

        if afficher_details:
            tag = " [BORD]" if touche_bord else ""
            print(f"Étape {nb_transitions:3d} | échange {echange}{tag:7s} -> L={L} | d_locale={d_locale} == calc={d_exacte}")

    print(f"\n[OK] n = {n} : {nb_transitions} transitions vérifiées (dont {nb_bords} touchant le 1er ou le dernier élément).")


#------------------------------------------------TEST---------------------------------
n = 6
p, posx, posy, dist = NYcity.init(n)

pmin, dmin, nb_perms, nb_evalues = recherche_exhaustive(dist)

"""
print(f"Meilleur circuit: {pmin}")
print(f"Distance minimale: {dmin}")
print(f"Permutations générées: {nb_perms} (attendu : {n}! = {1 if n==0 else math.factorial(n)})")
print(f"Circuits uniques évalués: {nb_evalues} (attendu : (n-1)!/2 = {math.factorial(n-1)//2})")


# Définition des 3 instances de test : (nom, posx, posy, longueur_attendue)
instances_test = [
    ("Triangle", [0, 3, 0], [0, 0, 4], 14),
    ("Rectangle 4x2", [0, 4, 4, 0], [0, 0, 2, 2], 12),
    ("Coordonnées répétées", [0, 0, 5, 5], [0, 0, 3, 3], 16),
]

for nom, posx, posy, attendu in instances_test:
    n = len(posx)
    dist = matrice_manhattan(posx, posy)
    pmin, dmin, nb_perms, nb_evalues = recherche_exhaustive(dist)

    # Contrôle que chaque site est visité exactement une fois
    assert verifier_circuit_valide(pmin, n), f"Circuit invalide pour {nom} : {pmin}"

    # Contrôle de la longueur optimale et du retour au départ (arête pmin[-1] -> pmin[0])
    somme_sans_retour = sum(dist[pmin[i]][pmin[i + 1]] for i in range(n - 1))
    arete_retour = dist[pmin[-1]][pmin[0]]
    assert somme_sans_retour + arete_retour == dmin, "Erreur : le retour au départ n'est pas inclus !"
    assert dmin == attendu, f"Optimum incorrect pour {nom} : obtenu {dmin}, attendu {attendu}"

    print(f"[OK] {nom:22s} | pmin = {pmin} | dmin = {dmin} (attendu = {attendu}) | retour = +{arete_retour}")

print("\n")

n = 5
p, posx, posy, dist = NYcity.init(n)
longueur_ref = NYcity.calc(p, dist)
print(f"Permutation initiale : {p} -> longueur = {longueur_ref}")

# 1. Vérification des n rotations (décalages circulaires)
for k in range(1, n):
    p_rot = p[k:] + p[:k]
    d_rot = NYcity.calc(p_rot, dist)
    assert d_rot == longueur_ref, f"Erreur sur la rotation {k}"
print(f"[OK] Les {n} rotations ont toutes la même longueur ({longueur_ref}).")

# 2. Vérification de l'inversion (parcours en sens inverse) et de ses rotations
p_inv = p[::-1]
for k in range(n):
    p_inv_rot = p_inv[k:] + p_inv[:k]
    d_inv = NYcity.calc(p_inv_rot, dist)
    assert d_inv == longueur_ref, f"Erreur sur l'inversion tournée {k}"
print(f"[OK] L'inversion {p_inv} et toutes ses rotations ont la même longueur ({longueur_ref}).")
"""

# Tests sur de petites instances : n = 3 (cas limite) et n = 4 (avec détail des bords)
verifier_maj_locale(3, afficher_details=True)
print("-" * 75)
verifier_maj_locale(4, afficher_details=True)
print("-" * 75)
verifier_maj_locale(5, afficher_details=False)
