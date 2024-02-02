import jsonpickle
import sqlite3
from Game import Jeu


class Library:
    def __init__(self):
        self.liste_jeux = []

    def creer_jeu(self, name, image, tags):
        nouveau_jeu = Jeu(name, image)
        nouveau_jeu.addTags(tags)
        self.liste_jeux.append(nouveau_jeu)
        print("Le jeu a été créé avec succès.")
        print()

    def afficher_liste_jeux(self):
        print("Liste de tous les jeux :")
        for jeu in self.liste_jeux:
            print(f"- {jeu.name}")
        print()

    def supprimer_jeu(self, nom_jeu):
        jeux_restants = [jeu for jeu in self.liste_jeux if jeu.name != nom_jeu]
        if len(jeux_restants) < len(self.liste_jeux):
            print(f"Le jeu {nom_jeu} a été supprimé avec succès.")
        else:
            print(f"Le jeu {nom_jeu} n'a pas été trouvé.")
        self.liste_jeux = jeux_restants
        print()

    def afficher_detail_jeu(self, nom_jeu):
        jeu_trouve= [jeu for jeu in self.liste_jeux if jeu.name == nom_jeu][:1]
        if jeu_trouve:
            print(f"Détails du jeu {jeu_trouve}:")
            # print(f"Nom: {jeu_trouve.name}")
            # print(f"Image: {jeu_trouve.image}")
            # print(f"Tags: {jeu_trouve.tags}")
        else:
            print(f"Le jeu {nom_jeu} n'a pas été trouvé.")
        print()



    def sauvegarder_bibliotheque(self):
        nom_fichier ="Jeux.json"
        data_jeu = {
            "jeux": [
                {"nom": jeu.name, "image": jeu.image, "tags": jeu.tags}
                for jeu in self.liste_jeux
            ]
        }
        json_data = jsonpickle.encode(data_jeu)
        with open(nom_fichier, 'w') as f:
            f.write(json_data)
        print(f"La bibliothèque a été sauvegardée dans {json_data}.")
        
    def sauvegarder_bibliothequeSQL(self):
        con = sqlite3.connect("jeux.db")
        cur = con.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS jeu(idJeu INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, image TEXT)")
        cur.execute("CREATE TABLE IF NOT EXISTS Tags(idTags INTEGER PRIMARY KEY AUTOINCREMENT, tagsNom TEXT)")

        for jeu in self.liste_jeux:
            cur.execute("INSERT INTO jeu (name, image) VALUES (?, ?)", (jeu.name, jeu.image))
            

            for tag in jeu.tags:
               cur.execute("INSERT INTO Tags (tagsNom) VALUES (?)", (tag,))


        cur.execute("SELECT * FROM jeu")
        jeux = cur.fetchall()
        print("Fetched rows from 'jeu':", jeux)

        cur.execute("SELECT * FROM Tags")
        tags = cur.fetchall()
        print("Fetched rows from 'Tags':", tags)

        con.commit()
        con.close()

        print("La bibliothèque a été sauvegardée dans la base de données SQLite.")
        
        
    def add_game(self, liste_jeux):
        self.liste_jeux.append(liste_jeux)
       
        


    
