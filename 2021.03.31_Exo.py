# EXO 1
list_animaux = ["lapin", "chat", "chien", "chiot", "dragon", "ornithorynque"]
print(list_animaux)
list_animaux.reverse()
print(list_animaux)
list_animaux.sort()
print(list_animaux)

list_animaux = ["lapin", "chat", "chien", "chiot", "dragon", "ornithorynque"]
list_animaux.append("troll")
#list_animaux.delete("chat"; "chien"; "chiot"; "lapin")
list_dom = list_animaux[0:4]
del list_animaux[0:4]
print(list_animaux)
print(list_dom)

# OU
list_animaux = ["lapin", "chat", "chien", "chiot", "dragon", "ornithorynque"]
domestiques = ["lapin","chat","chien","chiot"]
for i in domestiques :
    list_animaux.remove(i)
    print(list_animaux)


# EXO 2-3
import random
tableau_jeu=[]
# Initialisation d'une liste de 10 éléments
for i in range (0,10) :tableau_jeu.append (random.randint (1,10))
print(tableau_jeu)
tableau_jeu.sort()

#V1
ut=(int(input("Quel chiffre (1-10) ? ")))
if ut in tableau_jeu :
    print("gagné")
else :
    print ("perdu")

#V2
while ut in tableau_jeu:
    print("gagné")
    break
else :
    print("perdu")
