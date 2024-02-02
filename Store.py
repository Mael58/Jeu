from Game import Jeu
from Library import Library

class Store:
    librairy= Library()
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
        
        
    def buy_game(self, library):
        if library:
            nom_jeu = input("Entrez le nom du jeu que vous souhaitez acheter : ")
            jeu_a_acheter = next((jeu for jeu in self.liste_jeux if jeu.name == nom_jeu), None)
            if jeu_a_acheter:
                library.add_game(jeu_a_acheter)
                print(f"Le jeu {nom_jeu} a été ajouté à votre bibliothèque avec succès!")
                self.liste_jeux.remove(jeu_a_acheter)
            else:
                print(f"Le jeu {nom_jeu} n'est pas disponible dans ce magasin.")
        else:
            print("Aucune bibliothèque n'a été fournie.")