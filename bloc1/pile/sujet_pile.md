# TD PILE

## utilisation de la pile (facile)

dans les exercices suivant, une pile sera reprtesenté sous la forme d'une liste, les éléments s'ajoutent par la droite. on part d'une pile 'stack1' qui a pour comme éléments : 
| |
|-|
|0|
|2|
|6|
|9|

, le but des exercices suivants et de suivre les états successifs de la pile.
### exercice 1:
dessinez l'etat de la pile après le code suivant:
```python
stack1.push(9)
```
### exercice 2:
dessinez l'etat de la pile après le code suivant:
```python
stack1.pop()
```
### exercice 3:
dessinez l'etat de la pile après le code suivant:
```python
stack1.push(8)
stack1.push(10)
stack1.pop()
stack1.push(11)
stack1.top()
stack1.push(12)
```
---
dans la suite, on ajoute une pile 'stack2' vide

### exercice 4:
dessinez l'etat des piles après le code suivant:
```python
stack1.pop()
stack2.push(3)
stack2.push(3)
```
### exercice 5:
dessinez l'etat des piles après le code suivant:
```python
stack1.push(stack2.pop())
stack2.push(4)
```
### exercice 6:
dessinez l'etat des piles après le code suivant:
```python
stack1.push(stack2.top())
```

## implémentation (moyen)

le but de cette section est d'implémenter une des implémentations d'une pile, pas forcement la plus efficace en terme de temps ou espace.

vous devrez stocker les élèments de la pile dans une liste.

dans un premier créez une classe pile et ses méthodes dans l'ordre:
- push(a)

<details> 
  <summary>indice 1</summary>
   pensez à la concatenation
</details>

- pop()

<details> 
  <summary>indice 1</summary>
   où se trouve le dernier élèment ajouté dans la liste?
</details>
<details> 
  <summary>indice 2</summary>
   comment copier les tous élèments de la pile sauf le dernier élèment?
</details>

- top()

- isempty()

- size()

- sort() (à implémenter après l'exercice "tri d'un tas")

<details> 
  <summary>indice 1</summary>
   transformer la fonction sort_stack en méthode de pile
</details>

## utilisation 

### le bon parenthésage (facile)

ecrivez une fonction "bien_parenthese(str)" qui prend en parametre une chaine de charactere et qui retourne true si la chaine est bien parenthese

exemples:
|parametre|retour|
|:-:|:-:|
|"" | true|
|"(qsdf)" | true|
|")(" | false|
|"qfe)" | false|

### notation polonaise (moyen)

La notation polonaise inverse (NPI) (en anglais RPN pour Reverse Polish Notation), également connue sous le nom de notation post-fixée, permet d'écrire de façon non ambiguë les formules arithmétiques sans utiliser de parenthèses. Dérivée de la notation polonaise présentée en 1924 par le mathématicien polonais Jan Łukasiewicz, elle s’en différencie par l’ordre des termes, les opérandes y étant présentés avant les opérateurs et non l’inverse.

Par exemple, l’expression « 3 × (4 + 7) » s'écrie en NPI sous la forme « 4 7 + 3 × »

on lit '4' 

puis on lit '7' 

puis on lit '+', donc on fait 4+7 et on stock le resulat (11)

puis on lit '3'

puis on lit '\*', donc on fait 11\*3 et on stock le resultat (33)

puis il n'y a plus rien à lire donc on a finie

le but de l'exercice est de réaliser la fonction eval(formule) qui permet, dans un premier temps, de réaliser l'évaluation d'une formule en notation polonaise inverse uniquement sur des *chiffres* (de 0 à 9) et en retourne le resultat.

formule étant une chaine de caracteres valide (pas de besoin de tester si la formule est valide) sans espaces entre les chiffres.

il vous faudra peut être utiliser la fonction: eval(chaine) qui permet d'evaluer une chaine de caracteres (eval('3+4') retourne 7)

exemples:
|parametre|retour|
|:-:|:-:|
|"47+3*" | 33 |
|"34+6*" | 42 |

créez une fonction eval2(formule) qui fait la même chose mais qui peut prendre des nombres cette fois ci, et donc avec des espaces

exemples: 
|parametre|retour|
|:-:|:-:|
|"3 4 + 6 \*" | 42 |
|"101 - 1 * 10" | 1000 |

### tri d'un tas (difficile)

ecrivez une fonction 'sort_stack(stack)' qui tri la pile passé en parametre
pour cela vous vous aiderais d'une autre pile

exemple :
sur 'stack1' : 

| |
|-|
|0|
|9|
|6|
|2|

la fonction devra retourner : 

| |
|-|
|0|
|2|
|6|
|9|

<details> 
  <summary>indice 1</summary>
   pensez à utiliser ce qui à été vue dans l'exercice 5
</details>
<details> 
  <summary>indice 2</summary>
   où faut-il stocker l'élèment le plus grand une fois trouvé
</details>
<details> 
  <summary>indice 3</summary>
   comment trouver le plus grand élément
</details>
