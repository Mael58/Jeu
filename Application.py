from Store import Store
from Library import Library
from Store import Store
from tkinter import *
from tkinter import ttk
import tkinter as tk
root= Tk()

def Quitter():
    root.destroy()
    

    
            
          
    
class Application:
    
    if __name__ == '__main__':
        bibliotheque = Library()
        magasin = Store()
      
        
      
            
            
        content = ttk.Frame(root)
        frame = ttk.Frame(content, borderwidth=100, relief="ridge", width=100, height=100)
   
        bibliothequeLocale = ttk.Label(frame, text="Bibliothèque locale ")
        MagasinJeu= ttk.Label(frame, text="Magasin ")
        quitter= ttk.Label(frame, text="Quitter", )
        frame.grid(column=2, row=0)
        content.grid(column=0, row=0)
        bibliothequeLocale.grid(column=3, row=0)       
        MagasinJeu.grid(column=3, row=1)    
        quitter.grid(column=3, row=2)
     
       
        
       
       

      
      
       

        

      
        root.mainloop()
        
       
        
        # while True:
        #     print("1. Bibliothèque locale")
        #     print("2. Magasin")
        #     print("0. Quitter")

        #     choix_Menu = input("Entrez votre choix:")

        #     if choix_Menu == "1":
        #         while True:
        #             # print("1. Créer un jeu")
        #             # print("2. Supprimer un jeu")
        #             print("1. Afficher la liste de tous les jeux")
        #             print("2. Afficher le détail d'un jeu")
        #             print("3. Sauvegarder la bibliothèque dans un fichier JSON")
        #             print("4. Sauvegarder la bibliothèque dans un fichier SQL")
        #             print("0. Quitter")
                    

        #             choix = input("Entrez votre choix : ")

        #             # if choix == '1':
        #             #     nom = input("Entrez le nom du jeu : ")
        #             #     image = input("Entrez le nom du fichier image du jeu : ")
        #             #     tags = input("Entrez les tags du jeu (séparés par des virgules) : ")

        #             #     result = bibliotheque.creer_jeu(nom, image, tags)
                       

        #             # elif choix == '2':
        #             #     nom_jeu = input("Entrez le nom du jeu à supprimer : ")
        #             #     bibliotheque.supprimer_jeu(nom_jeu)
                        

        #             if choix == '1':
        #                 bibliotheque.afficher_liste_jeux()

        #             elif choix == '2':
        #                 nom_jeu = input("Entrez le nom du jeu dont vous souhaitez voir le détail : ")
        #                 bibliotheque.afficher_detail_jeu(nom_jeu)

        #             elif choix == '3':
        #                 bibliotheque.sauvegarder_bibliotheque()

        #             elif choix == '4':
        #                 bibliotheque.sauvegarder_bibliothequeSQL()

        #             elif choix == '0':
        #                 break
        #         else:
        #             print("Choix invalide. Veuillez entrer un nombre entre 0 et 5.\n")
                    
        #     else:
        #         while True:
        #             print("\n1. Creer un jeu")
        #             print("\n2. Supprimer un jeu")
        #             print("3. Afficher la liste des jeux en vente")
        #             print("4. Afficher les details du jeux")
        #             print("5. Acheter un jeu")
        #             print("6. Sauvegarder le magasin dans le format de stockage sélectionné")
        #             print("0. Quitter")

        #             choice = input("Entrez votre choix : ")

        #             if choice == '1':
        #                 nom = input("Entrez le nom du jeu : ")
        #                 image = input("Entrez le nom du fichier image du jeu : ")
        #                 tags = input("Entrez les tags du jeu (séparés par des virgules) : ")

        #                 result = magasin.creer_jeu(nom, image, tags)

        #             elif choice == '2':
        #                 nom_jeu = input("Entrez le nom du jeu à supprimer : ")
        #                 magasin.supprimer_jeu(nom_jeu)
                        
                    

        #             elif choice == '3':
        #                  magasin.afficher_liste_jeux()
                    

        #             elif choice == '4':
        #                 nom_jeu = input("Entrez le nom du jeu dont vous souhaitez voir le détail : ")
        #                 magasin.afficher_detail_jeu(nom_jeu)
                    
        #             elif choice == '5':
                        
        #                 magasin.buy_game(bibliotheque)
                    
        #             elif choice == '6':
        #                 pass
                    
        #             elif choice == '0':
        #                 break

        #             else:
        #                 print("Choix invalide. Veuillez entrer un nombre entre 0 et 4.\n")

        
                