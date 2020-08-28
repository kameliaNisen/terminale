import sqlite3
baseDeDonnees = sqlite3.connect('livres.db')
curseur = baseDeDonnees.cursor()
curseur.execute("SELECT * FROM livres WHERE auteur = ?", ("Asimov",))
for contact in curseur.fetchall():
    print(contact)