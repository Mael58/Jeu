from Store import Store
from Library import Library

class Application:
    if __name__ == '__main__':
        bibliotheque = Library()
        magasin = Store()
        while True:
            print("1. Bibliothèque locale")
            print("2. Magasin")
            print("0. Quitter")

            choix_Menu = input("Entrez votre choix:")

            if choix_Menu == "1":
                while True:
                    print("1. Créer un jeu")
                    print("2. Supprimer un jeu")
                    print("3. Afficher la liste de tous les jeux")
                    print("4. Afficher le détail d'un jeu")
                    print("5. Sauvegarder la bibliothèque dans un fichier JSON")
                    print("6. Sauvegarder la bibliothèque dans un fichier SQL")
                    print("0. Quitter")
                    

                    choix = input("Entrez votre choix : ")

                    if choix == '1':
                        nom = input("Entrez le nom du jeu : ")
                        image = input("Entrez le nom du fichier image du jeu : ")
                        tags = input("Entrez les tags du jeu (séparés par des virgules) : ")

                        result = bibliotheque.creer_jeu(nom, image, tags)
                       

                    elif choix == '2':
                        nom_jeu = input("Entrez le nom du jeu à supprimer : ")
                        bibliotheque.supprimer_jeu(nom_jeu)
                        

                    elif choix == '3':
                        bibliotheque.afficher_liste_jeux()

                    elif choix == '4':
                        nom_jeu = input("Entrez le nom du jeu dont vous souhaitez voir le détail : ")
                        bibliotheque.afficher_detail_jeu(nom_jeu)

                    elif choix == '5':
                        bibliotheque.sauvegarder_bibliotheque()

                    elif choix == '6':
                        bibliotheque.sauvegarder_bibliothequeSQL()

                    elif choix == '0':
                        break
                else:
                    print("Choix invalide. Veuillez entrer un nombre entre 0 et 5.\n")
            elif choix_Menu == "2":
                