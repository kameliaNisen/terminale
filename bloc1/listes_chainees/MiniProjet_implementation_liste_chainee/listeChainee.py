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
        
        >>> liste = ListeChainee()
        >>> liste.is_empty()
        True
        >>> liste.add_cell(1)
        >>> liste.is_empty()
        False
        '''
        pass
        
    def head(self) :
        '''
        Renvoie l'élément en tête de liste chaînée non vide
        Resultat : premier élément de la liste chaînée
        
        >>> liste = ListeChainee()
        >>> liste.add_cell(1)
        >>> liste.head()
        1
        '''      
        pass
    
    def tail(self):
        '''
        Renvoie la queue d'une liste chaînée non vide
        Resultat (ListeChainee)
        
        >>> liste = ListeChainee()
        >>> liste.add_cell(3)
        >>> liste.tail()
        ()
        >>> liste.add_cell(2)
        >>> liste.tail()
        (3,())
        >>> liste.add_cell(1)
        >>> liste.tail().tail()
        (3,())
        '''
        pass
    
    def longueur(self):
        # avec une fonction récursive
        '''
        Calcule le nombre de cellules d'une liste chaînée
        Résultat(int) : nombre d'élément dans la liste
        
        >>> liste = ListeChainee()
        >>> liste.longueur()
        0
        >>> liste.add_cell('b')
        >>> liste.longueur()
        1
        >>> liste.add_cell('a')
        >>> liste.longueur()
        2
        '''
        pass

    def longueur(self):
        # avec une boucle
        '''
        Calcule le nombre de cellules d'une liste chaînée
        Résultat(int) : nombre d'élément dans la liste
        
        >>> liste = ListeChainee()
        >>> liste.longueur()
        0
        >>> liste.add_cell('b')
        >>> liste.longueur()
        1
        >>> liste.add_cell('a')
        >>> liste.longueur()
        2
        '''
        pass

    def __len__(self):
        '''
        Calcule le nombre de cellules d'une liste chaînée
        Résultat(int) : nombre d'élément dans la liste
        
        >>> liste = ListeChainee()
        >>> len(liste)
        0
        >>> liste.add_cell('b')
        >>> len(liste)
        1
        >>> liste.add_cell('a')
        >>> len(liste)
        2
        '''
        return self.longueur()
    
    def nieme_element(self, n):
        '''
        Détermine le n-ième élément de la liste chaînée,
        les éléments étant numérotés à partir de 0
        n (int) : indice de l'élément demandé
        Résultat : nieme élément de la liste
        
        >>> liste = ListeChainee()
        >>> liste.add_cell('b')
        >>> liste.add_cell('a')
        >>> liste.nieme_element(0)
        'a'
        >>> liste.nieme_element(1)
        'b'
        '''
        pass
    
    def __getitem__(self, n):
        '''
        La notation `liste[i]` renvoie l'élément d'indice i
        
        >>> liste = ListeChainee()
        >>> liste.add_cell('b')
        >>> liste.add_cell('a')
        >>> liste[0]
        'a'
        >>> liste[1]
        'b'
        '''
        return self.nieme_element(n)

    def reverse(self):
        '''
        inverse l'ordre des éléments d'une liste chaînée
        Résultat (listeChainee) : liste chaînée contenant les éléments dans l'ordre inverse
        
        >>> liste = ListeChainee()
        >>> liste.add_cell(3)
        >>> liste.add_cell(2)
        >>> liste.add_cell(1)
        >>> liste
        (1,(2,(3,())))
        >>> liste.reverse()
        (3,(2,(1,())))
        '''
        pass

    def __add__(self, liste):
        '''
        L'opérateur `+` entre listes chaînées renvoie la concaténation de celles-ci
        
        >>> liste = ListeChainee()
        >>> liste.add_cell(3)
        >>> liste.add_cell(2)
        >>> liste.add_cell(1)
        >>> liste
        (1,(2,(3,())))
        >>> liste2 = ListeChainee()
        >>> liste2.add_cell(6)
        >>> liste2.add_cell(5)
        >>> liste2.add_cell(4)
        >>> liste2
        (4,(5,(6,())))
        >>> liste + liste2
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
        
        >>> liste = ListeChainee()
        >>> liste.add_cell(3)
        >>> liste.add_cell(2)
        >>> liste.add_cell(1)
        >>> liste
        (1,(2,(3,())))
        >>> liste.insert(0,'x')
        >>> liste
        ('x',(1,(2,(3,()))))
        >>> liste.insert(2,'y')
        >>> liste
        ('x',(1,('y',(2,(3,())))))
        '''
        pass
    
    def delete(self,n):
        '''
        Supprime l'élément à l'indice n dans la liste chaînée
        n (int) : indice de l'élément supprimé
        Resulat (None)
        Effet de bord : Modification de la liste en place
        
        >>> liste = ListeChainee()
        >>> liste.add_cell('d')
        >>> liste.add_cell('c')
        >>> liste.add_cell('b')
        >>> liste.add_cell('a')
        >>> liste
        ('a',('b',('c',('d',()))))
        >>> liste.delete(0)
        >>> liste
        ('b',('c',('d',())))
        >>> liste.delete(1)
        >>> liste
        ('b',('d',()))
        '''
        pass
            
    def __delitem__(self,n):
        '''
        Supprime l'élément à l'indice n dans la liste chaînée
        n (int) : indice de l'élément supprimé
        Resulat (None)
        Effet de bord : Modification de la liste en place
        
        >>> liste = ListeChainee()
        >>> liste.add_cell('d')
        >>> liste.add_cell('c')
        >>> liste.add_cell('b')
        >>> liste.add_cell('a')
        >>> liste
        ('a',('b',('c',('d',()))))
        >>> del liste[0]
        >>> liste
        ('b',('c',('d',())))
        >>> del liste[1]
        >>> liste
        ('b',('d',()))
        '''
        self.delete(n)

if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
