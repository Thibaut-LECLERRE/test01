"""
L'exercice consiste à créer une fonction NbrLigne qui a pour paramètre
le nom d'un fichier (texte) et qui renvoie le nombre de lignes de ce fichier
Avant de commencer l'exercice,
veuillez enregistrer le fichier suivant dans le répertoire où vous travaillez
=>Demi.txt
"""
def NbrLigne (fichier):

    # ouverture du fichier
    fic = open(fichier, "r", encoding = "utf-8")
    compteur = 0

    #parcours du fichier
    for ligne in fic:
        l = ligne.strip("\n") #séparation ligne par ligne
        compteur += 1
    print(compteur)

NbrLigne("C:\Users\Thibaut\Desktop\12_PROGRAMMATION PYTHON\Exercices\Exo3_chaineCaract\Demi.txt")
