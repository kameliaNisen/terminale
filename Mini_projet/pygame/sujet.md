# projet ballon

## objectifs

l'objectif du projet est de réaliser un mini jeu de basket-ball comprenant:

-   une balle
-   un panier

le but du jeu étant de lancer la balle dans le panier.

## contraintes

la balle suivra une trajectoire de projectile balistique standard (équations donné dans [ce chapitre](#les-équations)).
le panier est mobile. (libre a vous de lui donner le trajectoire souhaité, du moment qu'il est mobile)
le lancer de la balle se fera au moment du clique du joueur.
le jeu est à réaliser en python avec la bibliothéque [pyagme](https://www.pygame.org/docs/).
le joueur marque un point quand il lance la balle dans le panier, les points sont réinitialisé quand le joueur manque le panier

## les equations

la trajectoire d'un projectile est déterminer par une fonction : 

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Ferde_hajitas2.svg/250px-Ferde_hajitas2.svg.png)

cette fonction est détérminé par:

- une *puissance* correspond à la puissance du tire, libre à vous de determiner quelle puissance vous voullez donner au projectile du moment qu'elle n'est pas fixe

- un *temps* correspond au temps actuel de parcour

- l'angle correspond à l'angle de la trajectoire au debut du lancé, exprimé en radiants

la trajectoire d'un projectile est donné par les équations suivantes:
- la vélocité peut être divisé en deux, celle sur les abscisses (vX) et celle sur les ordonnées (vY):
- - vX = cos(angle)* *puissance*
- - vY = cos(angle)* *puissance*

- la distance parcourue par le projectile en abscisse est:
- vX * *temps*
- la distance parcourue par le projectile en ordonnée est plus compliqué car il faut appliqué la gravité:
- vY* *temps* + (sqrt(9.8)* *time*² )/2

pour trouver l'angle de départ:

l'angle se mesure entre le sol et la droite définie par la balle et l'emplacement du curseur

![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Unit_circle_angles_color.svg/1024px-Unit_circle_angles_color.svg.png)

- arctan((ballY - curseurY)/(ballX - curseurX))
- faire attention à la division par 0

on obtient une valeur entre -pi/2 et pi/2 qu'il faut modifier pour obtenir une valeur entre pi et 2*pi

- si ballY > mouseY et ballX < mouseX
- - angle = |angle|
- si ballY > mouseY et ballX > mouseX
- - angle = pi - angle
- si ballY < mouseY et ballX > mouseX
- - angle = pi+ |angle|
- si ballY > mouseY et ballX > mouseX
- - angle = pi*2 + angle

## améliorations

- implémentez une resistance à l'air
- faire en sorte que la balle ne sorte pas de l'ecran
- augmentez la difficulté du jeu quand le joueur marque un point
- affichez le meilleur score
- faire un menu
- ajoutez une musique
- ...
