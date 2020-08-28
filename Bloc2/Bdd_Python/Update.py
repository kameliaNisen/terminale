import sqlite3
baseDeDonnees = sqlite3.connect('livres.db')
curseur = baseDeDonnees.cursor()
curseur.execute("UPDATE livres SET note = ? WHERE titre = ?", (10, "Blade Runner"))
baseDeDonnees.commit()
baseDeDonnees.close()