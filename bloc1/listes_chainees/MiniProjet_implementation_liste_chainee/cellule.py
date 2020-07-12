class Cellule:
    """Constructeur d'une cellule de liste chaînée"""
    def __init__(self, element, celluleSuivante):
        self.valeur = element
        self.suivante = celluleSuivante
    
    def __repr__ (self):
        """
        Renvoie une notation parenthésée d'une cellule""

        >>> c = Cellule(1, (Cellule(2, (Cellule(3, None)))))
        >>> repr(c)
        '(1,(2,(3,())))'
        """
        if self.suivante == None :
            return '('+repr(self.valeur)+',())'
        else :
            return '('+repr(self.valeur)+','+repr(self.suivante)+')'
    
    def concatener(c1, c2):
        """
        Concatène 2 cellules d'une liste chaînée sous la forme d'une nouvelle cellule
        c1, c2 (Cellule)
        Résultat (Cellule)
        
        >>> c = Cellule(1, (Cellule(2, (Cellule(3, None)))))
        >>> c2 = Cellule(4, (Cellule(5, (Cellule(6, None)))))
        >>> c.concatener(c2)
        (1,(2,(3,(4,(5,(6,()))))))
        
        """
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
