# projet casino

from random import *

pari = 0
wallet = int(500)


while wallet > 0 :
    print("Bonjour, voici la roulette. Votre portefeuille est de " + str(wallet) + ". Bonne chance au jeu !")
    pari = int(input("Sur quel chiffre mise-vous (Entre 0 et 49 ?) "))

    if pari < 0 or pari > 49:
        print("Entre 0 et 49, recommencez !!!\n")
    else:
        mise = int(input("Combien misez-vous ? Vous disposez de " + str(wallet) + ". " ))
        if mise > wallet :
            print("Vous ne pouvez pas miser autant.\n")
        else:
            roulette = randrange(50)
            print("Et c'est le " + str(roulette))

            if pari == roulette:
               wallet = wallet + mise*3
               print("Votre mise est triplée. Votre wallet est de " + str(round(wallet)) + " !\n")
            elif pari != roulette and (roulette%2==0) and (pari%2==0) :
               wallet = int((wallet-mise) + (mise/2))
               print("Même couleur, on vous rend la moitiée de votre mise. Votre wallet est de " + str(round(wallet)) + " !\n")
            elif pari != roulette and (roulette%2==1) and (pari%2==1) :
                wallet = int((wallet-mise) + (mise/2))
                print("Même couleur, on vous rend la moitiée de votre mise. Votre wallet est de " + str(round(wallet)) + " !\n")
            else:
               wallet = wallet - mise
               print("Vous perdez votre mise. Votre wallet est de " + str(round(wallet)) + " !\n")

else :
    print("Vous avez perdu!\nRentrez chez vous")
