from itertools import permutations

"""
Génère les permutations sans contraintes
liste_couple: liste entiers, représente les hommes & femmes
"""
def gen_no_restrictions(liste_couple):
    l_res = list(permutations(liste_couple))
    
    return l_res

"""
Génère les permutations où les hommes doivent rester ensemble et les femmes aussi
liste_couple: liste entiers, représente les hommes & femmes
"""
def gen_men_and_women(liste_couple):
    l_gen = gen_no_restrictions(liste_couple)
    l_res = []

    for i in range(len(l_gen)):
        condition_homme1 = (l_gen[i][0] < 4 and l_gen[i][1] < 4 and l_gen[i][2] < 4 and l_gen[i][3] < 4)
        condition_femme1 = (l_gen[i][4] >= 4 and l_gen[i][5] >= 4 and l_gen[i][6] >= 4 and l_gen[i][7] >= 4)
        condition_homme2 = (l_gen[i][4] < 4 and l_gen[i][5] < 4 and l_gen[i][6] < 4 and l_gen[i][7] < 4)
        condition_femme2 = (l_gen[i][0] >= 4 and l_gen[i][1] >= 4 and l_gen[i][2] >= 4 and l_gen[i][3] >= 4)

        if((condition_homme1 and condition_femme1) or (condition_femme2 and condition_homme2)):
            l_res.append(l_gen[i])
    
    return l_res

"""
Génère les permutations où les hommes doivent rester ensemble
liste_couple: liste entiers, représente les hommes & femmes
"""
def gen_men(liste_couple):
    l_gen = gen_no_restrictions(liste_couple)
    l_res = []
    limite = len(l_gen[0]) // 2

    for i in range(len(l_gen)):
        verif = False
        for j in range(0, limite + 1):
            condition_verif = (l_gen[i][j] < 4 and l_gen[i][j + 1] < 4 and l_gen[i][j + 2] < 4 and l_gen[i][j + 3] < 4)
            if(condition_verif):
                verif = True

        if(verif):
            l_res.append(l_gen[i])
    
    return l_res

"""
Génère les permutations où les couples sont ensemble
liste_couple: liste entiers, représente les hommes & femmes
"""
def gen_couple(liste_couple):
    l_gen = gen_no_restrictions(liste_couple)
    l_res = []

    for i in range(len(l_gen)):
        verif = True
        for j in range(0, len(l_gen[0]) - 1, 2):
            if(abs(l_gen[i][j] - l_gen[i][j + 1]) != 4):
                verif = False
                break
        
        if(verif):
            l_res.append(l_gen[i])
    
    return l_res

#-----------------------------------------------MAIN----------------------------------------------------#
liste_couple = list(range(8))
l_perm_no_restrictions = gen_no_restrictions(liste_couple)
print("Nombre de permutations sans contraintes:", len(l_perm_no_restrictions))

l_men_and_women = gen_men_and_women(liste_couple)
print("Nombre de permutations avec les hommes ensembles et les femmes ensemble:", len(l_men_and_women))

l_men = gen_men(liste_couple)
print("Nombre de permutations avec les hommes ensembles:", len(l_men))

l_couple = gen_couple(liste_couple)
print("Nombre de permutations avec les couples qui restent ensembles:", len(l_couple))

