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

    verif(lettre,mot,mot_etoile,liste_lettres_trouvees,liste_alphabet,nombre_essais)
