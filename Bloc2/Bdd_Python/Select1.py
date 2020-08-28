import sqlite3
baseDeDonnees = sqlite3.connect('livres.db')
curseur = baseDeDonnees.cursor()
curseur.execute("SELECT * FROM livres WHERE auteur = ?", ("Asimov",))
contact = curseur.fetchone()
print(contact)