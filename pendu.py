from donnees import *
from fonctions import *
from random import randrange


mot = liste_mots[randrange(0,len(liste_mots))]
print(mot)
mot_liste=lister_mot(mot)
print(mot_liste)
mot_etoile = mot_etoile(mot_liste)

global nombre_essais

print(mot_etoile)


liste_lettres_trouvees=[]

while "*" in mot_etoile and nombre_essais!=0:
    lettre = input("Entrez une lettre")

    if verifAlphabet(lettre,liste_alphabet):
        if verifLettreTrouvees(lettre,liste_lettres_trouvees):
            print("La lettre a déjà été trouvée !")
        else:
            if verifMot(lettre,mot,mot_etoile,liste_lettres_trouvees):
                print(" ")
            else:
                nombre_essais=faux(nombre_essais)
    else:
        print("La lettre entrée n'est pas contenue dans l'alphabet")

    print("Il vous reste",nombre_essais,"essais")

    print(mot_etoile)

if "*" not in mot_etoile:
    print("Vous avez gagné, le mot était",mot)
else:
    print("Perdu le mot était",mot)
