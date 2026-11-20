#!/usr/bin/env python
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# --------------------------------------
# Pb du voyageur de commerce à Manhattan
# --------------------------------------
# UTILISATION :
# import NYcity
#     puis on initialise les positions (intersections) et les distances (de Manhattan) :
# p, posx, posy, dist = NYcity.init(n)
#     et après avoir trouvé la bonne permutation, on affiche sa longueur :
# print('Distance = ',NYcity.calc(p, dist))
#     et on trace le résultat graphiquement :
# NYcity.plot(p, posx, posy)

scale = 10
mySeed = 2024

def init(n):
    # En entrée :
    #     n = nombre de sites
    # En sortie :
    #     perm = liste (ordonnée) des sites de 0 à n-1
    #     posx, posy = liste des positions x et y des sites
    #     dist = tableau (python : liste de liste) des distances, 
    #            dist[i][j] est la distance du site i au site j.
    rng = random.Random(mySeed)  # Générateur local : préserve le hasard du programme appelant.
    perm = [i for i in range(n)]
    # Tirage par site : à graine et échelle identiques, les instances sont emboîtées.
    posx, posy = [], []
    for i in range(n):
        posx.append(rng.randint(0,scale))
        posy.append(rng.randint(0,scale))
    # Calcul des distances de Manhattan
    dist = [[0 for k in range(n)] for j in range(n)] 
    for k in range(1,n):
        for j in range(k):
            dist[k][j] = abs(posx[k]-posx[j])+abs(posy[k]-posy[j])
            dist[j][k] = abs(posx[k]-posx[j])+abs(posy[k]-posy[j])
    return perm, posx, posy, dist

def calc(perm, dist):
    # En entrée :
    #     perm = liste (ordonnée) des sites de 0 à n-1
    #     dist = tableau (python : liste de liste) des distances, 
    # En sortie :
    #     d = longueur de la solution basée sur perm
    n = len(perm)
    d = dist[perm[n-1]][perm[0]]
    for i in range(n-1):
        d += dist[perm[i]][perm[i+1]]
    return(d)

def plot(perm, posx, posy):
    # En entrée :
    #     perm = permutation des sites correspondant au trajet proposé
    #     posx, posy = liste des positions x et y des sites
    # Attention, la fonction est bloquante (pyplot.show()) !

    # Tracé des points et de la ville de NY
    plt.figure()
    currentAxis = plt.gca()
    for i in range(scale):
        for j in range(scale):
            currentAxis.add_patch(Rectangle((i+0.1,j+0.1), 0.8, 0.8,color='orange', alpha=1))
    plt.plot(posx, posy, 'o', color='black')
    n = len(posx)
    for i in range(n):
        plt.text(posx[i]+0.1, posy[i]+0.1, f'{i}')
    # Tracé final de la solution
    n = len(perm)
    perm = list(perm) + [perm[0]]  # Ferme le circuit sur une copie locale.
    for i in range(n):
        coinx1, coiny1 = posx[perm[i]], posy[perm[i+1]]
        dist1 = abs(2*coinx1-scale) + abs(2*coiny1-scale)
        coinx2, coiny2 = posx[perm[i+1]], posy[perm[i]]
        dist2 = abs(2*coinx2-scale) + abs(2*coiny2-scale)
        if dist1>dist2:
            plt.plot( [posx[perm[i]],coinx1,posx[perm[i+1]]], [posy[perm[i]],coiny1,posy[perm[i+1]]], color='blue')
        else:
            plt.plot( [posx[perm[i]],coinx2,posx[perm[i+1]]], [posy[perm[i]],coiny2,posy[perm[i+1]]], color='blue')
    plt.show()

if __name__ == "__main__":
    n = 10
    p, posx, posy, dist = init(n)
    # bla bla
    print('Distance = ',calc(p, dist))
    plot(p, posx, posy)
