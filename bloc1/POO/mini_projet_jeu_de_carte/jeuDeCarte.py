class JeuDeCarte:
    def creerPaquet(self):
        #A compléter
        #permet de créer le paquet de cartes (voir constructeur)
    
    def __init__(self,nb):
        # nb : attribut contenant le nombre de cartes composant le jeu de carte
        # paquet : attribut contenant la liste des cartes de jeu (agrégation de classe)
        self.nb = nb;
        self.paquet = self.creerPaquet()
    
    def __repr__(self):
        # A compléter
    
    def melangerPaquet(self):
        # A compléter
    
    def distribuerCarte(self):
        # A compléter
    
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
        # A compléter

                
if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
        