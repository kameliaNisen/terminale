# Projet Morpion à deux joueurs (Textuel) : 

Pour jouer une partie de morpion, il suffit de tracer sur une feuille blanche une grille de 3 cases sur 3 (selon les variantes, il est possible d’augmenter le nombre de cases). Le but du jeu est d’aligner avant son adversaire 3 symboles identiques horizontalement, verticalement ou en diagonale.
Chaque joueur a donc son propre symbole, généralement une croix pour l’un et un rond pour l’autre. La partie se termine quand l’un des joueurs à aligner 3 symboles ou quand la grille est complétée sans vainqueur. Il y a alors égalité.

## Partie 1 : Morpion en textuel 

N'oubliez pas de : 

- Documentez vos fonctions
- Découpez le code en plusieurs fonctions.

### Exemple de déroulement du code :

```
>>> c= Grille()
>>> c.jeu()
        0    1    2
A     ['.', '.', '.']
B     ['.', '.', '.']
C     ['.', '.', '.']
Joueur x choisissez une case sous la forme : A0, B1, C0, etc .. 
A1
Placé!
        0    1    2
A     ['.', 'x', '.']
B     ['.', '.', '.']
C     ['.', '.', '.']
Joueur o choisissez une case sous la forme : A0, B1, C0, etc .. 
A0
Placé!
        0    1    2
A     ['o', 'x', '.']
B     ['.', '.', '.']
C     ['.', '.', '.']
Joueur x choisissez une case sous la forme : A0, B1, C0, etc .. 
A1
Placement impossible
        0    1    2
A     ['o', 'x', '.']
B     ['.', '.', '.']
C     ['.', '.', '.']
Joueur x choisissez une case sous la forme : A0, B1, C0, etc .. 
B1
Placé!
        0    1    2
A     ['o', 'x', '.']
B     ['.', 'x', '.']
C     ['.', '.', '.']
Joueur o choisissez une case sous la forme : A0, B1, C0, etc .. 
A2
Placé!
        0    1    2
A     ['o', 'x', 'o']
B     ['.', 'x', '.']
C     ['.', '.', '.']
Joueur x choisissez une case sous la forme : A0, B1, C0, etc .. 
C1
Placé!
        0    1    2
A     ['o', 'x', 'o']
B     ['.', 'x', '.']
C     ['.', 'x', '.']
Victoire du joueur  x
```

## Bonus :

Créer la fonction du jeu de manière recursive (ou itérative si vous avez déjà opter pour la récursivité)

