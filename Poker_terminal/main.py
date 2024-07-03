import numpy as np
import fonctions_poker as fpkr


def main():
     
    print("Bienvenue dans notre CASINO ROYAL")
    print("Bienvenue au jeu du Poker")

    while True:

            print("--------MENU PRINCIPAL-------")
            print("1 - Lancer une nouvelle partie")
            print("2 - Charger une partie")
            print("3 - Voir les règles du jeu")
            print("4 - Quitter le jeu")
            choix=int(input("Faites votre choix: "))


            if choix==1:
                joueur_actuel=input("Donnez votre nom de joueur: ")
                joueur_actuel=fpkr.Joueur(joueur_actuel,np.empty((5,2)), credit=10)
                fpkr.lancer_partie(joueur_actuel)
            elif choix==2:
                joueur_actuel=input("Donnez votre nom de joueur: ")
                fpkr.charger_partie(joueur_actuel)
            elif choix==3:
                fpkr.regles()
            elif choix==4:
                print("\nAu revoir")
                break
            else:
                print("Faites un choix à partir du menu de 1 à 4")
if __name__=="__main__":
    main()