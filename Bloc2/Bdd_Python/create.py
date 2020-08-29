import sqlite3
baseDeDonnees = sqlite3.connect('Livres.db')
curseur = baseDeDonnees.cursor()
curseur.execute("CREATE TABLE livres (id INTEGER PRIMARY KEY AUTOINCREMENT, titre TEXT NOT NULL, auteur TEXT NOT NULL, ann_publi INTEGER, note INTEGER)") # Création de la base de données
baseDeDonnees.commit() # On envoie la requête SQL
curseur.execute("INSERT INTO livres (titre,auteur,ann_publi,note) VALUES (?, ?, ?, ?)", ("1984","Orwell",1949,10)) # On ajoute un enregistrement
baseDeDonnees.commit()
baseDeDonnees.close()
