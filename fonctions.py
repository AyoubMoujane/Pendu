

def lister_mot (mot): #Transforme le mot choisi en une liste
    mot_en_liste = []
    for i in range (0,len(mot)):
        mot_en_liste.append(mot[i])
    return mot_en_liste

def mot_etoile (mot_en_liste):              #["t","o","i","t"] -> ["*","*","*","*"]
    for i in range (0,len(mot_en_liste)):
        mot_en_liste[i]="*"
    return mot_en_liste

def verifAlphabet(lettre,liste_alphabet): #return true ou false si la lettre entrée est contenue ou non dans l'alphabet
    return lettre in liste_alphabet

def verifLettreTrouvees(lettre,liste_lettres_trouvees): #return true ou false si la lettre entrée a déjà été trouvée ou non
    return lettre in liste_lettres_trouvees

def verifMot(lettre,mot,mot_en_etoile,liste_lettres_trouvees): #return true ou false si la lettre entrée était dans le mot
    bool=0
    for i in range (0,len(mot)):
        if lettre == mot[i]:
            bool+=1
            liste_lettres_trouvees.append(mot[i])
            juste(lettre,mot_en_etoile,i)


    if bool==0:
        print("Vous n'avez trouvé aucune lettre")
        return False
    else:
        print("Bravo, vous avez trouvé",bool,"lettres")
        return True


def juste(lettre,mot_en_etoile,i):
    mot_en_etoile[i]=lettre

def faux(nombre_essais):
    return nombre_essais-1
