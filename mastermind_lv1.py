# Degrange Sara TS1
# Projet ISN Mastermind

import random, sys

# Liste des couleurs à choix
couleurs = ["rouge", "bleu", "vert", "jaune", "orange", "gris"]

# Initialisation des couleur à choix (construit à partir de la liste de couleurs
# où couleur[i][0] = 0ième caractère du ième nom de couleur)
initiales_couleurs = []
for couleur in couleurs:
    initiales_couleurs.append(couleur[0])

# Longueur pour les combinaison de couleurs
longueur_combinaison = 4

# nombre maximal de tentatives pour trouver la combinaison
nb_max_tentatives = 10

def afficher_les_couleurs_a_choix():
    print ("les couleurs à choix sont:")
    for couleur in couleurs :
        print("-",couleur)

def creer_combinaison_secrete():
    combinaison_secrete=""

    for i in range(0,longueur_combinaison):
        index=random.randint(0,len(initiales_couleurs)-1)
        combinaison_secrete=combinaison_secrete+initiales_couleurs[index]

    return combinaison_secrete

def comparer_combinaisons(combinaison_entree, combinaison_secrete):
    nb_couleurs_bien_placees = 0
    nb_couleurs_mal_placees = 0
    initiales_couleurs_entrees = list(combinaison_entree)
    initiales_couleurs_secretes = list(combinaison_secrete)

    for i in range(0,len(initiales_couleurs_entrees)):
        if initiales_couleurs_entrees[i] == initiales_couleurs_secretes[i]:
#nb_couleurs_bien_placees=nb_couleurs_bien_placees+1
            nb_couleurs_bien_placees+=1
            initiales_couleurs_entrees[i]='x'
            initiales_couleurs_secretes[i]='x'

    for i in range(0,len(initiales_couleurs_entrees)):
        if initiales_couleurs_entrees[i] in initiales_couleurs_secretes:
            if initiales_couleurs_entrees[i] != 'x':
                nb_couleurs_mal_placees+=1
                couleur_actuelle = initiales_couleurs_entrees[i]
                j=initiales_couleurs_secretes.index(couleur_actuelle)
                initiales_couleurs_secretes[j]='x'

    return [nb_couleurs_bien_placees, nb_couleurs_mal_placees]

def demander_combinaison_au_joueur():
    invalide=False
    combinaison_joueur=input("Entrez votre combinaison:")
    if len(combinaison_joueur) != longueur_combinaison:
        print("longueur incorrecte")
        invalide= True
    for lettre in combinaison_joueur:
        if lettre not in initiales_couleurs:
            print("La couleur",lettre, "n'existe pas")
            invalide= True

    if invalide == True :
        return "Erreur"
    else :
        return combinaison_joueur
    
#programme
afficher_les_couleurs_a_choix ()
combinaison_ordi=creer_combinaison_secrete()

for i in range(0, nb_max_tentatives):
    combinaison_user="Erreur"
    while combinaison_user=="Erreur":
        combinaison_user=demander_combinaison_au_joueur()
    valeurs_comparees=comparer_combinaisons(combinaison_user,combinaison_ordi)
    if valeurs_comparees[0]== longueur_combinaison:
        print("Félicitation, vous avez gagné")
        break
    else :
        print ("Vous avez",valeurs_comparees[0],"éléments bien placées et",valeurs_comparees[1],"éléments mal placées")
        













