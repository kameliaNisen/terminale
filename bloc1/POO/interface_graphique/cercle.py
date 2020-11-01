from tkinter import *
import random

#-------------------------
# DEFINITION DES FONCTIONS
#-------------------------

def dessinerCercle():
    x = random.randint(0,Largeur)
    y = random.randint(0,Hauteur)
    r = 20
    zoneDessin.create_oval(x-r, y-r, x+r, y+r, outline = 'blue', fill = 'blue')
    print("création d'un cercle de coordonnée (", x, y, ")" )

def effacer():
    zoneDessin.delete(ALL)
    
#----------------------------------
# DEFINITION DES VARIABLES GLOBALES
#----------------------------------
Largeur = 480
Hauteur = 320

#-------------------------------------
# CREATION DE LA FENETRE ET DES WIDGETS
#-------------------------------------

# Création de la fenêtre principale (main window)
maFenetre = Tk()
maFenetre.title('Cercle')

# Création d'un widget Canvas (zone graphique)
zoneDessin = Canvas(maFenetre, width = Largeur, height = Hauteur, bg = 'white')
zoneDessin.pack(padx = 5, pady = 5)

# Création d'un widget Button (bouton Go)
boutonGo = Button(maFenetre, text ='Go', command = dessinerCercle)
boutonGo.pack(side = LEFT, padx = 10, pady = 10)

# Création d'un widget Button (bouton Effacer)
boutonEffacer = Button(maFenetre, text ='Effacer', command = effacer)
boutonEffacer.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Button (bouton Quitter)
boutonQuitter = Button(maFenetre, text ='Quitter', command = maFenetre.destroy)
boutonQuitter.pack(side = LEFT, padx = 5, pady = 5)

#-----------------------
# GESTION DES EVENEMENTS
#-----------------------

#Lancement du gestionnaire d'événements
maFenetre.mainloop() 