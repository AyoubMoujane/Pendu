

def lister_mot (mot): #Transforme le mot choisi en une liste
    mot_en_liste = []
    for i in range (0,len(mot)):
        mot_en_liste.append(mot[i])
    return mot_en_liste

def mot_etoile (mot_en_liste):              #["t","o","i","t"] -> ["*","*","*","*"]
    for i in range (0,len(mot_en_liste)):
        mot_en_liste[i]="*"
    return mot_en_liste

def verif(lettre,mot,mot_en_etoile,liste_lettres_trouvees,liste_alphabet,nombre_essais):
    bool=0
    if lettre in liste_alphabet:
        if lettre not in liste_lettres_trouvees:
            for i in range (0,len(mot)):
                if lettre == mot[i]:
                    bool+=1
                    liste_lettres_trouvees.append(mot[i])
                    juste(lettre,mot_en_etoile,i)
        else:
            x= input("La lettre que vous venez d'entrer a déjà été entrée veuillez en saisir une autre")
            verif(x,mot,mot_en_etoile,liste_lettres_trouvees,liste_alphabet,nombre_essais)
    else:
        x=input("Veuillez entrer une lettre de l'alphabet !")
        verif(x,mot,mot_en_etoile,liste_lettres_trouvees,liste_alphabet,nombre_essais)
    if bool==0:
        print("raté !")
        nombre_essais=faux(nombre_essais)
    else:
        print("Bravo, vous avez trouvé",bool,"lettres")

    print(mot_en_etoile)
    print("Il vous reste",nombre_essais,"essais")

def juste(lettre,mot_en_etoile,i):

    mot_en_etoile[i]=lettre

def faux(nombre_essais):
    return nombre_essais-1
