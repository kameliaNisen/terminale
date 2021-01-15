# Les Piles

## Présentation de la structure de données

une pile est une structure de données abstraites qui se définit par les méthodes qui lui sont associées.

c'est une structure dite LIFO (last in first out), c'est a dire que le premier element qui rentre dans la structure est le dernier qui en va en sortir et le dernier element qui y rentre sera la première à en sortir.

## Exemple 

Similaire à une pile de livres, on ajoute les livres les uns sur les autres et quand on veut prendre un livre, on prend celui du dessus.

![](https://upload.wikimedia.org/wikipedia/commons/9/93/PrimitivesPile.png)

## les méthodes associé aux piles:

### les méthodes essentiels:
de cet exemple, on peut en déduire que les méthodes associées aux piles sont: 
- **empiler**: ajoute un element a la pile
- **depiler**: retire un element a la pile

### les méthodes secondaires:
on peut aussi y associer d'autres méthodes par mesure de commodité mais ce sont celles-ci dessus qui définissent qu'est une pile 

ces autres méthodes sont (pour le cas du python):
- **top**: retourne l'element du dessus de la pile mais ne modifie pas la pile

### les méthodes "hérité" des structures de données:
et on y ajoute des méthodes communes à toutes les structures de données:
- **estVide**: return vrai si la pile est vide
- **recevoir**: retourne la taille de la pile 

## les implémentation d'une pile:

l'implementation des piles peut se faire de beaucoup de façon, plus ou moins efficace en temps ou espace, mais l'implementation est à dissocier de la structure abstraite.
