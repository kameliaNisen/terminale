class Carte:
    # Attributs de classes
    couleurs = ('Coeur', 'Carreau', 'Trèfle', 'Pique')
    noms = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
    valeurs = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, \
                         '9': 9, '10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14}
    
            
    def __init__(self, nom, coul):
        self.nom = nom
        self.couleur = coul
        self.valeur = # A compléter     
    
    def __repr__(self):
        # A compléter 
    
    def __eq__(self, carte2):
        #A compléter
    
    def __lt__(self, carte2):
        #A compléter
    
    def __gt__(self, carte2):
        #A compléter

if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)