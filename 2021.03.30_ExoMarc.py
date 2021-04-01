# https://python.developpez.com/cours/apprendre-python-3/?page=exercices-corriges

"""EXO 1
Écrire un programme qui permet de saisir le nom de l'utilisateur
et de renvoyer "Bonjour", suivi de ce nom"""
x=input()
print("Bonjour, "+x+".")


"""EXO 2
Écrire un programme qui demande à l'utilisateur
la saisie de a et b et affiche la somme de a et de b."""
a=float(input())
b=float(input())
print(a+b)


"""EXO 3
Écrire un programme qui, à partir de la saisie d'un rayon et d'une hauteur,
calcule le volume d'un cône droit."""
#from math import *
r=float(input())
h=float(input())
print(3,14 * (r*r) * h / 3)
#print(math.pi * (r*r) * h / 3)


""""EXO 4
 Une boucle while : entrez un prix HT (entrez o pour terminer)
 et affichez sa valeur TTC."""
tax = 1.10
var=1
while var != 0 :
    var = float(input("entrez un prix : "))
    print(round(var*tax))
    if var == 0 :
        print("stop")
        break

# VERSION MARC
prixHT = float(input("Prix HT (0 pour terminer)? "))
while prixHT > 0:
    print("Prix TTC : {:.2f}\n".format(prixHT * 1.196))
    prixHT = float(input("Prix HT (0 pour terminer)? "))
print("Au revoir !")


"""EXO 5
Un permis de chasse à points remplace désormais le permis de chasse traditionnel.
Chaque chasseur possède au départ un capital de 100 points.
S'il tue une poule, il perd 1 point, 3 points pour un chien,
5 points pour une vache et 10 points pour un ami. Le permis coûte 200 euros.
Écrire une fonction amende qui reçoit le nombre de victimes du chasseur et qui renvoie la somme due.
Utilisez cette fonction dans un programme principal qui saisit le nombre de victimes
et qui affiche la somme que le chasseur doit débourser."""

def amende(p1,p2,p3,p4):
    poule=1*p1
    chien=3*p2
    vache=5*p3
    ami=10*p4
    total=(poule+chien+vache+ami)*2
    if total > 200 :
        print ("Permis perdu et amende de " + str(total) + " €.")
    else :
        print("Amende à payer " + str(total) + " €.")

amende(0,0,0,0) #test


"""EXO 6
Créez une fonction qui prend deux nombres comme arguments et retourne leur somme.
somme(1, 2) ➞ 3
somme(4, 4) ➞ 8
somme(-1, -1) ➞ -2"""
def sommetiti(x,y):
    return(x*y)
print(sommetiti(2,7)) #test


"""EXO 7
Créez une fonction qui prend deux nombres comme arguments et faire la soustraction.
Exemple:
soustraction(2, 1) ➞ 1
soustraction(4, 2) ➞ 2
soustraction(-3, -3) ➞ 0"""
def soustiti(x,y):
    return(x-y)
print(soustiti(10,6)) #test


"""EXO 8
Écrivez une fonction qui prend un nombre entier de minutes et le convertit en secondes.
Exemple:
convert(1) ➞ 60
convert(2) ➞ 120
convert(6) ➞ 360"""
def consectiti(x):
   return x*60
print(consectiti(3)) #test


"""EXO 9
Créez une fonction qui prend la hauteur et la largeur et trouve le périmètre d’un rectangle.
Exemple:
getPerimeter(2, 4) ➞ 12
getPerimeter(6, 10) ➞ 32
getPerimeter(3, 6) ➞ 18"""
def halarectiti(x,y) :
    return(x*2)+(y*2)
print(halarectiti(2,4)) #test


"""EXO 10
Write a Python program to convert temperatures to and from celsius, fahrenheit"""
def convertCFtiti(x,y):
    if y == "C":
        conv1 = (x*(9/5)) + 32
        print("Temp in fahrenheit : " + str(conv1))
    elif y == "F":
        conv2 = (x-32)*(5/9)
        print("Temp in celcius : " + str(conv2))
    else :
        print ("Are you sure of the temperature value ?")

x=float(input("Enter a value : "))
y=str(input("C for Celcius or F for Fahrenheit"))
convertCFtiti(x,y)


#fonction avec l'analyse dernière lettre chaine caractère
def convertCFtiti2(x):
    if (x.lower()[-1]) == "c" :
        f=float(x[:-1])
        conv1 = (f*(9/5)) + 32
        print("Temp in Fahrenheit : " + str(conv1)+ "°")
    elif (x.lower()[-1]) == "f" :
        c=float(x[:-1])
        conv2 = (c-32)*(5/9)
        print("Temp in Celcius : " + str(conv2) + "°")
    else :
        print ("Are you sure of the temperature value ?")

x=input("Enter a value : ")
convertCFtiti2(x)

"""
dans notre cas pour insensibiliser à la case
variable1.lower()
"""













