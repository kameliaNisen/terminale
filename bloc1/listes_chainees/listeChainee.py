from cellule import *

class ListeChainee:

    def __init__(self):
        '''
        Construit une liste chainée vide
        '''
        self.tete = None

    def __repr__ (self):
        """
        Renvoie une notation parenthésée d'une liste chaînée""

        >>> liste = ListeChainee()
        >>> repr(liste)
        '()'
        >>> liste.add_cell(1)
        >>> repr(liste)
        '(1,())'
        """
        if self.is_empty():
            return '()'
        else:
            return repr(self.tete)

    def add_cell(self, element):
        '''
        Crée une cellule contenant element et la rajoute en tête de la liste
        element (type quelconque) : contenu de la cellule de tête
        Résultat : None
        Effet de bord : Modification en place de la liste chaînée
        
        >>> liste = ListeChainee()
        >>> liste.add_cell(1)
        >>> liste
        (1,())
        '''
        self.tete = Cellule(element, self.tete)

    def is_empty(self):
        '''
        Détermine si la liste est vide ou non
        Résultat (bool) : True si la liste ne contient aucune cellule
        
        >>> l = ListeChainee()
        >>> l.is_empty()
        True
        >>> l.add_cell(1)
        >>> l.is_empty()
        False
        '''
        pass
        
    def head(self) :
        '''
        Renvoie l'élément en tête de liste chaînée non vide
        Resultat : premier élément de la liste chaînée
        
        >>> l = ListeChainee()
        >>> l.add_cell(1)
        >>> l.head()
        1
        '''       
        pass
    
    def tail(self):
        '''
        Renvoie la queue d'une liste chaînée non vide
        Resultat (ListeChainee)
        
        >>> l = ListeChainee()
        >>> l.add_cell(3)
        >>> l.tail()
        ()
        >>> l.add_cell(2)
        >>> l.tail()
        (3,())
        >>> l.add_cell(1)
        >>> l.tail().tail()
        (3,())
        '''
        pass
    
    def longueur(self):
        # avec une fonction récursive
        '''
        Calcule le nombre de cellules d'une liste chaînée
        Résultat(int) : nombre d'élément dans la liste
        
        >>> l = ListeChainee()
        >>> l.longueur()
        0
        >>> l.add_cell('b')
        >>> l.longueur()
        1
        >>> l.add_cell('a')
        >>> l.longueur()
        2
        '''
        pass

    def longueur(self):
        # avec une boucle
        '''
        Calcule le nombre de cellules d'une liste chaînée
        Résultat(int) : nombre d'élément dans la liste
        
        >>> l = ListeChainee()
        >>> l.longueur()
        0
        >>> l.add_cell('b')
        >>> l.longueur()
        1
        >>> l.add_cell('a')
        >>> l.longueur()
        2
        '''
        pass

    def __len__(self):
        '''
        Calcule le nombre de cellules d'une liste chaînée
        Résultat(int) : nombre d'élément dans la liste
        
        >>> l = ListeChainee()
        >>> l.longueur()
        0
        >>> l.add_cell('b')
        >>> l.longueur()
        1
        >>> l.add_cell('a')
        >>> l.longueur()
        2
        '''
        return self.longueur()
    
    def nieme_element(self, n):
        '''
        Détermine le n-ième élément de la liste chaînée,
        les éléments étant numérotés à partir de 0
        n (int) : indice de l'élément demandé
        Résultat : nieme élément de la liste
        
        >>> l = ListeChainee()
        >>> l.add_cell('b')
        >>> l.add_cell('a')
        >>> l.nieme_element(0)
        'a'
        >>> l.nieme_element(1)
        'b'
        '''
        pass
    
    def __getitem__(self, n):
        '''
        La notation `liste[i]` renvoie l'élément d'indice i
        
        >>> l = ListeChainee()
        >>> l.add_cell('b')
        >>> l.add_cell('a')
        >>> l[0]
        'a'
        >>> l[1]
        'b'
        '''
        return self.nieme_element(n)

    def reverse(self):
        '''
        inverse l'ordre des éléments d'une liste chaînée
        Résultat (listeChainee) : liste chaînée contenant les éléments dans l'ordre inverse
        
        >>> l = ListeChainee()
        >>> l.add_cell(3)
        >>> l.add_cell(2)
        >>> l.add_cell(1)
        >>> l
        (1,(2,(3,())))
        >>> l.reverse()
        (3,(2,(1,())))
        '''
        pass

    def __add__(self, liste):
        '''
        L'opérateur `+` entre listes chaînées renvoie la concaténation de celles-ci
        
        >>> l = ListeChainee()
        >>> l.add_cell(3)
        >>> l.add_cell(2)
        >>> l.add_cell(1)
        >>> l
        (1,(2,(3,())))
        >>> l2 = ListeChainee()
        >>> l2.add_cell(6)
        >>> l2.add_cell(5)
        >>> l2.add_cell(4)
        >>> l2
        (4,(5,(6,())))
        >>> l + l2
        (1,(2,(3,(4,(5,(6,()))))))
        '''
        resultat = ListeChainee()
        cellule = self.tete.concatener(liste.tete)
        resultat.tete = cellule 
        return resultat
    
    def insert(self,n,element):
        '''
        Insère element à l'indice n dans la liste chaînée
        n (int) : indice où sera effectuée l'insertion
        element (type quelconque) : élément à insérer
        Resulat (None)
        Effet de bord : Modification de la liste en place
        
        >>> l = ListeChainee()
        >>> l.add_cell(3)
        >>> l.add_cell(2)
        >>> l.add_cell(1)
        >>> l
        (1,(2,(3,())))
        >>> l.insert(0,'x')
        >>> l
        ('x',(1,(2,(3,()))))
        >>> l.insert(2,'y')
        >>> l
        ('x',(1,('y',(2,(3,())))))
        '''
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
