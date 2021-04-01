"""
http://sosoftware.free.fr/ExosC.php

L'exercice consiste à créer une fonction searchC qui a pour paramètres un mot et une chaine de caractères
et qui renvoie False si l'élément n'est pas dans la chaîne de caractères, ou la position du mot dans le cas contraire.
(ici False est un booléen, pas une chaîne de caractères)
"""
#EXO 1 avec FIND
textest = "Salut Raoul, je suis là !"
mot = "je"

print(textest.find("je")) #renvoie 13, la position du 1er caractère
print(textest.find("tu")) #renvoie -1, non présent dans la chaine de caractères


#EXO 2 avec la fonction
def searchC(b,a):
    x= a.find(b)
    if x == -1:
        print(False)
    else :
        print("Position de mot, première lettre est le caractère n°" + str(a.find(b)))


a = "Salut Raoul, je suis là !"
b = "je"
c = "tu"
print(searchC(b,a))



################################################################################
"""
Voici une chaîne de caractères : "La v13 3st un myst3r3 qu'1l faut v1vr3, et non un probl3m3 a r3soudr3.Gandh1".
L'exercice consiste à afficher cette chaîne de caractères en remplaçant les 1 par des i et les 3 par des e.
(Cette fois-ci je ne demande pas la définition d'une fonction.)
"""
#EXO 2 V1
chaineTeste = "La v13 3st un myst3r3 qu'1l faut v1vr3, et non un probl3m3 à r3soudr3.Gandh1"
print(chaineTeste)
ichaine = chaineTeste.replace("1","i")
echaine = ichaine.replace("3","e")
print(echaine)

#EXO 2 V2 avec fonction
chaineTeste = "La v13 3st un myst3r3 qu'1l faut v1vr3, et non un probl3m3 à r3soudr3.Gandh1"
def ReplanceIE(x):
    i=x.replace("1","i")
    e=i.replace("3","e")
    print(e)
ReplanceIE(chaineTeste)

#EXO 2 Correction en ligne
chaineTeste = "La v13 3st un myst3r3 qu'1l faut v1vr3, et non un probl3m3 à r3soudr3.Gandh1"
newtext=""
for letter in chaineTeste:
    if letter=="1":
        newtext+="i"
    elif letter=="3":
        newtext+="e"
    else:
        newtext+=letter
print(newtext)
################################################################################

"""
L'exercice consiste à créer une fonction compteur qui a pour paramètres une lettre et une chaine de caractères,
et qui renvoie le nombre d'apparitions de la lettre dans la chaîne de caractères.
"""
def compteur (a,b):
    #a = la lettre à chercher ; b = la chaine de caractère
    compt=0
    for i in b:
        if i==a:
            compt+=1
    return(compt)

a="z"
b="comment vous appelez-vous ?"
print(compteur(a,b))

################################################################################
"""
Créez une fonction inverse qui prend une chaine de caractères en paramètre et qui renvoie son inverse.
"""
a = "ceci est un anagramme"
print(a)
def reversed_string(a_string):
    return a_string[::-1]
print(reversed_string(a))


################################################################################
"""
L'exercice consiste à créer une fonction NbrLigne qui a pour paramètre
le nom d'un fichier (texte) et qui renvoie le nombre de lignes de ce fichier
Avant de commencer l'exercice,
veuillez enregistrer le fichier suivant dans le répertoire où vous travaillez
=>Demi.txt
"""







"""
Voici une chaîne de caractères : " La mesure de l'homme. \n \n Ce n est pas celui qui critique qui est important,
ni celui qui montre du doigt comment l homme fort trébuche ou comment l homme d action aurait pu faire mieux. \n
L hommage est dû à celui ou à celle qui se bat dans l arène, dont le visage est couvert de poussière et de sueur,
 qui va de l avant vaillamment, qui commet des erreurs et en commettra encore, car il n y a pas d efforts humains
 sans erreurs et imperfections.  C est à lui ou à elle qu appartient l hommage, à celui ou à celle dont l enthousiasme
 et la dévotion sont grands, à celui ou à celle qui se consume pour une cause importante, à celui ou à celle qui,
 au mieux, connaîtra le triomphe du succès, et au pis, s il échoue, saura qu il a échoué alors qu il risquait courageusement."
L'exercice consiste à : (Cette fois-ci je ne demande pas la définition d'une fonction.)
a. Créez un autre fichier texte nommé La_mesure_de_lhomme.txt et écrire la chaîne de caractères dedans.
b. Écrivez le contenu du fichier Demi.txt à la suite du fichier La_mesure_de_lhomme.txt.
c. Affichez le contenu du fichier La_mesure_de_lhomme.txt.
"""





################################################################################










