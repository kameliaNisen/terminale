import File
import random
   
VAL_CARTE = ['1','2','3','4','5','6','7','8','9','10','V','D','R','AS']
COL_CARTE = ['P','T','C','H']

def in_file(x,f):
    """
    Fonction qui revoie True si x est dans la file f
    param x (): element present ou non dans f
    param f (File1/File2) : File contenant ou non x
    return (bool) : Renvoie True si x est dans f, False sinon
    """
    if type(f) == File1 :
        if x in f.file :
            return True
        else :
            return False
    elif type(f) == File2 :
        if f.tete == x :
            return True
        elif f.queue != None :
            return in_file(x,f.queue)
        else :
            return False
    else :
        return False
        
def comp(c1,c2) :
    """
    Fonction de comparaison entre deux cartes
    param c1 : (tuple) Carte 1
    param c2 : (tuple) Carte 2
    return : Renvoie
                    -1 si => c1 < c2
                    1  si => c1 > <2
                    0  si => c1 == c2
    
    """
    if VAL_CARTE.index(c1[0]) < VAL_CARTE.index(c2[0]) :
        return -1
    elif VAL_CARTE.index(c1[0]) > VAL_CARTE.index(c2[0]) :
        return 1
    else :
        return 0
                    
def creer_jeu():
    """
    Fonction qui crée un jeu aléatoire
    return a,b (File) Deux files contenant 26 cartes chacunes
    """
    i = 0
    val_carte = ['1','2','3','4','5','6','7','8','9','10','V','D','R','AS']
    col_carte = ['P','T','C','H']
    f1 = File1()
    f2 = File1()
    while i < 52 :
        val = random.randint(0,len(val_carte)-1)
        col = random.randint(0,len(col_carte)-1)
        carte = (val_carte[val],col_carte[col])
        if in_file(carte,f1) == False or in_file(carte,f2) == False  :
            if i%2 == 0 :
                f1.enfile(carte)
            else :
                f2.enfile(carte)
            i+=1
    return f1,f2
            


def game(f1,f2):
    """
    Fonction simulant le jeu de la bataille
    param f1: (File) File contenant le jeu n°1
    param f2: (File) File contenant le jeu n°2
    """
    while not est_fini(f1,f2) :
        tour(f1,f2)