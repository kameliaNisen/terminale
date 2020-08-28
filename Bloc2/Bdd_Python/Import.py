import sqlite3
baseDeDonnees = sqlite3.connect('livres.db')
curseur = baseDeDonnees.cursor()
livres= [
	{"titre":"Dune", "auteur":"Herbert", "ann_publi":1965, "note":8},
	{"titre":"Fondation", "auteur":"Asimov", "ann_publi":1951, "note":9},
	{"titre":"Le meilleur des mondes", "auteur":"Huxley", "ann_publi":1931, "note":7},
	{"titre":"Fahrenheit 451", "auteur":"Bradbury", "ann_publi":1953, "note":7},
	{"titre":"Ubik", "auteur":"K.Dick", "ann_publi":1969, "note":9},
	{"titre":"Chroniques martiennes", "auteur":"Bradbury", "ann_publi":1950, "note":8},
	{"titre":"La nuit des temps", "auteur":"Barjavel", "ann_publi":1968, "note":7},
	{"titre":"Blade Runner", "auteur":"K.Dick", "ann_publi":1968, "note":8},
	{"titre":"Les Robots", "auteur":"Asimov","ann_publi":1950, "note":9},
	{"titre":"La Planète des singes", "auteur":"Boulle", "ann_publi":1963, "note":8},
	{"titre":"Ravage", "auteur":"Barjavel", "ann_publi":1943, "note":8},
	{"titre":"Le Maître du Haut Château", "auteur":"K.Dick", "ann_publi":1962, "note":8},
	{"titre":"Le Monde des non-A", "auteur":"Van Vogt", "ann_publi":1945, "note":7},
	{"titre":"La Fin de l’éternité", "auteur":"Asimov", "ann_publi":1955, "note":8},
	{"titre":"De la Terre à la Lune", "auteur":"Verne", "ann_publi":1865, "note":10},
    {"titre":"Hypèrion", "auteur":"Simmons", "ann_publi":1989, "note":8}
]
for livre in livres:
	curseur.execute("INSERT INTO livres (titre, auteur, ann_publi, note) VALUES (:titre, :auteur, :ann_publi, :note)", livre) # On ajoute un enregistrement depuis un dictionnaire
baseDeDonnees.commit()
idDernierEnregistrement = curseur.lastrowid # Récupère l'ID de la dernière ligne insérée.
baseDeDonnees.close()