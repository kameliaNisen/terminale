import carte
import random

class JeuDeCarte:
    def creerPaquet(self,nb):
        paquet = []
        for couleur in carte.Carte.couleurs:
            for nom in carte.Carte.noms :
                if self.nb == 52:
                    paquet.append(carte.Carte(nom,couleur))
                if self.nb == 32 and carte.Carte.noms not in ['2','3','4','5','6']:
                    paquet.append(carte.Carte(nom,couleur))
        return paquet
    
    def __init__(self,nb):
        # nb : attribut contenant le nombre de cartes composant le jeu de carte
        # paquet : attribut contenant la liste des cartes de jeu (agrégation de classe)
        self.nb = nb;
        self.paquet = self.creerPaquet(nb)
    
    def __repr__(self):
        '''
        >>> monJeu = JeuDeCarte(52)
        >>> monJeu
        2 de Coeur, 3 de Coeur, 4 de Coeur, 5 de Coeur, 6 de Coeur, 7 de Coeur, 8 de Coeur, 9 de Coeur, 10 de Coeur, Valet de Coeur, Dame de Coeur,
        Roi de Coeur, As de Coeur, 2 de Carreau, 3 de Carreau, 4 de Carreau, 5 de Carreau, 6 de Carreau, 7 de Carreau, 8 de Carreau, 9 de Carreau, 10 de Carreau, 
        Valet de Carreau, Dame de Carreau, Roi de Carreau, As de Carreau, 2 de Trèfle, 3 de Trèfle, 4 de Trèfle, 5 de Trèfle, 6 de Trèfle, 7 de Trèfle, 8 de Trèfle, 
        9 de Trèfle, 10 de Trèfle, Valet de Trèfle, Dame de Trèfle, Roi de Trèfle, As de Trèfle, 2 de Pique, 3 de Pique, 4 de Pique, 5 de Pique, 6 de Pique, 7 de Pique, 
        8 de Pique, 9 de Pique, 10 de Pique, Valet de Pique, Dame de Pique, Roi de Pique, As de Pique,
        '''
        afficher = ""
        for i in range(len(self.paquet)):
            afficher += str(self.paquet[i])
            afficher +=', '
        return afficher
        #return str(self.paquet)
            
    
    def melangerPaquet(self):
        return random.shuffle(self.paquet)
  
    def distribuerCarte(self):
        x = self.paquet.pop()
        return self.paquet
       
    def distribuerCartes(self,nbCartes,nbJoueurs):
        """
        descritption de la méthode : distribuer des cartes du paquet à des joueurs
        nbCartes (int) : nombre de cartes à distribuer à chaque joueur
        nbJoueurs (int) : nombre de joueurs à qui distribuer les cartes
        return(liste de listes de cartes(Carte)) : une liste contenant autant de listes que de joueurs
                                                chacune de ces listes contient la liste des cartes
                                                distribuées au joueur
        effet de bord : le paquet de carte est modifié : il ne contient plus les cartes distribuées
        """
##       >>> monJeu = JeuDeCarte(52)
##      >>> distribuerCartes(4,2)
        
        if (nbJoueurs * nbCartes <= self.nb):
            c=[]
            for i in range(nbJoueurs):
                c.append([])
                for j in range(nbCartes):
                    c[i].append(self.distribuerCarte())
                return c
            else:
                print('Pas assez de carte dans le jeu')
        
    def __len__(self):
        return len(self.paquet)
                
if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
