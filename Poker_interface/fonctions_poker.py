import numpy as np

# Les valeurs et les symboles 'C' (Coeur), 'D' (Carreau), 'H' (Trèfle), 'S' (Pique) de 52 cartes
jeu_de_cartes = np.array([
    (2, 'C'), (3, 'C'), (4, 'C'), (5, 'C'), (6, 'C'), (7, 'C'), (8, 'C'), (9, 'C'), (10, 'C'), (11, 'C'), (12, 'C'), (13, 'C'), (14, 'C'),
    (2, 'D'), (3, 'D'), (4, 'D'), (5, 'D'), (6, 'D'), (7, 'D'), (8, 'D'), (9, 'D'), (10, 'D'), (11, 'D'), (12, 'D'), (13, 'D'), (14, 'D'),
    (2, 'H'), (3, 'H'), (4, 'H'), (5, 'H'), (6, 'H'), (7, 'H'), (8, 'H'), (9, 'H'), (10, 'H'), (11, 'H'), (12, 'H'), (13, 'H'), (14, 'H'),
    (2, 'S'), (3, 'S'), (4, 'S'), (5, 'S'), (6, 'S'), (7, 'S'), (8, 'S'), (9, 'S'), (10, 'S'), (11, 'S'), (12, 'S'), (13, 'S'), (14, 'S')
], dtype=[('valeur', int), ('couleur', 'U1')])

class Joueur: # Classe représentant un joueur avec son nom, sa main de cartes et son crédit
    def __init__(self, nom, main_cartes=None, credit=0):
        self.nom = nom
        self.main_cartes = main_cartes if main_cartes is not None else [None] * 5
        self.credit = credit

    def miser(self, nb): # Méthode permettant au joueur de miser un certain nombre de jetons
        if self.credit >= int(nb):
            self.credit -= int(nb)
            return True
        else:
            print(f"votre crédit est insuffisant pour miser {nb} jetons")
            print(f"Votre crédit est de {self.credit}")
            return False

croupier = Joueur("Croupier", credit=10000000)
# Fonction pour distribuer de nouvelles cartes aux joueurs à partir du jeu de cartes
def nouvelles_cartes(ja, indices_cartes_a_changer=[0, 1, 2, 3, 4]):
    global jeu_de_cartes
    if len(indices_cartes_a_changer)>0:
        for i in indices_cartes_a_changer:
            if i < 5 and len(jeu_de_cartes) > 0:
                ja.main_cartes[i] = jeu_de_cartes[0]
                jeu_de_cartes = np.delete(jeu_de_cartes, 0, axis=0)

def changer_cartes_croupier(croupier):
    eval=evaluer_main(croupier.main_cartes)
    indice_a_changer=[]
    #On change les cartes de valeur inférieure à 7 qui ne sont pas pairées
    if eval[0]==3:
        m_eval=dict(eval[2])
        for i in range(5):
            if croupier.main_cartes[i][0]<7 and m_eval[croupier.main_cartes[i][0]]==1:
                indice_a_changer.append(i)
    elif eval[0]==2:
        m_eval=dict(eval[2])
        for i in range(5):
            if croupier.main_cartes[i][0]<7 and m_eval[croupier.main_cartes[i][0]]==1:
                indice_a_changer.append(i)
    elif eval[0]==1:
        for i in range(5):
            if croupier.main_cartes[i][0]<7:
                indice_a_changer.append(i)
    nouvelles_cartes(croupier,indice_a_changer)

def afficher_main(main):
    return '\n'.join(f"{carte['valeur']}{carte['couleur']}" if carte is not None else "Carte vide" for carte in main)

#Déterminer la force d'une main de cartes
def est_suite(main):
    main=sorted([carte['valeur'] for carte in main],  reverse=True)
    suite = True
    for i in range(4):
        if main[i]-main[i+1]!=1:
            suite=False
    if main[0]==14 and main[4]==2:
        suite=True
        for i in range(1,4):
            if main[i]-main[i+1]!=1:
                suite=False
    return suite
def est_flush(main):
    couleurs = [carte['couleur'] for carte in main]
    couleur=True
    for i in range(4):
        if couleurs[i]!=couleurs[i+1]:
            couleur=False
    return couleur
def est_carre(main):
    valeurs = [carte['valeur'] for carte in main]
    valeur_comptes = {valeur: valeurs.count(valeur) for valeur in valeurs}
    if 4 in valeur_comptes.values():
        carre=[valeur for valeur in valeur_comptes if valeur_comptes[valeur]==4]
        return [True,carre]
    return [False]
def est_full(main):
    valeurs = [carte['valeur'] for carte in main]
    valeur_comptes = {valeur: valeurs.count(valeur) for valeur in valeurs}
    if (2 in valeur_comptes.values()) and (3 in valeur_comptes.values()):
        full=[valeur for valeur in valeur_comptes if valeur_comptes[valeur]==3]
        return [True,full]
    return [False]
def est_brelan(main):
    valeurs = [carte['valeur'] for carte in main]
    valeur_comptes = {valeur: valeurs.count(valeur) for valeur in valeurs}
    if (3 in valeur_comptes.values()):
        brelan=[valeur for valeur in valeur_comptes if valeur_comptes[valeur]==3]
        return [True,brelan]
    return [False]
def est_double_paires(main):
    valeurs = sorted([carte['valeur'] for carte in main], reverse=True)
    valeur_comptes = {valeur: valeurs.count(valeur) for valeur in valeurs}
    if list(valeur_comptes.values()).count(2)==2:
        dpaire= [valeur for valeur in valeur_comptes if valeur_comptes[valeur]==2 ]
        return [True,dpaire]
    return [False]
def est_paire(main):
    valeurs = [carte['valeur'] for carte in main]
    valeur_comptes = {valeur: valeurs.count(valeur) for valeur in valeurs}
    if (2 in valeur_comptes.values()):
        paire= [valeur for valeur in valeur_comptes if valeur_comptes[valeur]==2 ]
        return [True,paire]
    return [False]

#Evaluation d'une main de carte, pour récupérer la combinaison présente
def evaluer_main(main):#=(int mabin 1 o 10,"smiya la main",Akbar karte awla
    """
    Évalue la main du joueur et retourne un tuple (rang, valeurs_importantes).
    Rang: 1 pour carte haute, 2 pour une paire, 3 pour double paires, 4 pour brelan, 5 pour suite, 6 pour flush/couleur,
     7 pour full, 8 pour caréé, 9 pour Quinte Flush et 10 pour une quinte flush royale.
    Chaque comparaison, retourne un tableau (Numéro de combinaison, le nom de la combinaison, les cartes triés)
    """
    valeurs = sorted([carte['valeur'] for carte in main], reverse=True)
    valeur_comptes = {valeur: valeurs.count(valeur) for valeur in valeurs}

    # Quinte flush royale, Quinte flush, Flush, Suite

    if est_flush(main) and est_suite(main):
        if valeurs[0] == 14:  # As est la plus haute carte
            return (10,"Quinte flush royale", valeurs)  # Quinte flush royale
        return (9, "Quinte flush ", valeurs[0])  # Quinte flush
    if est_flush(main):
        return (6,"Flush", valeurs[0])  # Flush
    if est_suite(main):
        return (5,"Suite", valeurs[0])  # Suite

    # Carré, Full House, Brelan, Deux Paires, Paire, Carte Haute
    if est_carre(main)[0]:
        return (8,"Carré",valeur_comptes.items(),est_carre(main)[1])  # Carré
    if est_full(main)[0]:
        return (7,"Full", valeur_comptes.items(),est_full(main)[1])  # Full
    if est_brelan(main)[0]:
        return (4,"Brelan",valeur_comptes.items(),est_brelan(main)[1])  # Brelan
    if est_double_paires(main)[0]:
        return (3,"Double Paires",valeur_comptes.items(),est_double_paires(main)[1])  # Double Paires
    if est_paire(main)[0]:
        return (2,"Paire",valeur_comptes.items(),est_paire(main)[1])  # Paire
    return (1,"Carte Haute", valeurs[0])  # Carte Haute


#Comparaison de deux mains de deux joueurs en comparant l'evalutaion de chaque main  et renvoie le joueur gagnant
def comparer(joueur1, joueur2):
    main_joueur1 = joueur1.main_cartes
    main_joueur2 = joueur2.main_cartes
    eval_joueur1 = evaluer_main(main_joueur1)
    eval_joueur2 = evaluer_main(main_joueur2)
    if eval_joueur1[0] > eval_joueur2[0]:
        print(eval_joueur1[1])
        print("Vous avez gagné")
        return joueur1
    elif eval_joueur1[0] < eval_joueur2[0]:
        print(eval_joueur2[1])
        print("le croupier a gagné")
        return joueur2
    elif eval_joueur1[0] == eval_joueur2[0]:
        if eval_joueur1[0]==1 or eval_joueur1[0]==5 or eval_joueur1[0]==6 or eval_joueur1[0]==9:
            if eval_joueur1[2] < eval_joueur2[2]:
                print(eval_joueur2[1])
                print("Le croupier gagné")
                return joueur2
            else :
                print(eval_joueur1[1])
                print("Vous avez gagné")
                return joueur1
        elif eval_joueur1[0]==2 or eval_joueur1[0]==3 or eval_joueur1[0]==4 or eval_joueur1[0]==7 or eval_joueur1[0]==8:
            if eval_joueur1[3] < eval_joueur2[3]:
                print(eval_joueur2[1])
                print("Le croupier gagné")
                return joueur2
            else :
                print(eval_joueur1[1])
                print("Vous avez gagné")
                return joueur1
        else:
            print(eval_joueur1[1])
            print("Vous avez gagné")
            return joueur1



def lancer_partie(ja):
    global jeu_de_cartes
    global croupier
    np.random.shuffle(jeu_de_cartes)
    ja.main_cartes = [None] * 5
    croupier.main_cartes = [None] * 5
    print(f"Bonjour et bienvenue {ja.nom} sur ma table")
    print("Je m'appelle Nadir et je serai votre croupier aujourd'hui")
    n_round = 1
    while True:
        pot=0
        print(f"On commence notre round No {n_round}")
        print(f"Votre crédit est de {ja.credit} jetons")
        mise=int(input("Pour commencer veuillez miser un nombre de jetons inférieur à votre crédit: "))
        ja.miser(mise)
        pot=2* mise #pour prendre en compte la mise du joueur et du croupier
        print(f"La valeur totale du pot est de {pot} jetons")
        nouvelles_cartes(ja)
        nouvelles_cartes(croupier)
        print("Votre main actuelle est")
        print(afficher_main(ja.main_cartes))
        #Changer des cartes
        choix=input("Est-ce que vous voulez changer des cartes de votre main oui/non:").lower()
        if choix=="oui":
            indices= input("Donnez les indices des cartes à changer (séparés par une virgule): ").split(",")
            indices_chang=[int(ind) for ind in indices]
            nouvelles_cartes(ja,indices_chang)
            print("Votre main actuelle est")
            print(afficher_main(ja.main_cartes))
        changer_cartes_croupier(croupier)
        #Doubler la mise
        choix=input("Est ce que vous voulez doubler la mise oui/non:").lower()
        if choix=="oui":
            ja.miser(mise)
            pot*=2
            print(f"La valeur totale du pot est devenue {pot} jetons")
        #Affichage des mains finales
        print("Votre main finale est:")
        print(afficher_main(ja.main_cartes))
        print("La main croupier est:")
        print(afficher_main(croupier.main_cartes))
        #comparer les mains et annoncer le gagnant
        comparer(ja, croupier).credit += pot
        print(f"Votre crédit est de {ja.credit}")
        pot = 0
        choix=input("vous voulez contunier ou quitter la partie? c/q: ")
        if choix == "q":
            quitter(ja)
            return
        elif choix == "c":
            n_round += 1
            jeu_de_cartes = np.array([
                (2, 'C'), (3, 'C'), (4, 'C'), (5, 'C'), (6, 'C'), (7, 'C'), (8, 'C'), (9, 'C'), (10, 'C'), (11, 'C'), (12, 'C'), (13, 'C'), (14, 'C'),
                (2, 'D'), (3, 'D'), (4, 'D'), (5, 'D'), (6, 'D'), (7, 'D'), (8, 'D'), (9, 'D'), (10, 'D'), (11, 'D'), (12, 'D'), (13, 'D'), (14, 'D'),
                (2, 'H'), (3, 'H'), (4, 'H'), (5, 'H'), (6, 'H'), (7, 'H'), (8, 'H'), (9, 'H'), (10, 'H'), (11, 'H'), (12, 'H'), (13, 'H'), (14, 'H'),
                (2, 'S'), (3, 'S'), (4, 'S'), (5, 'S'), (6, 'S'), (7, 'S'), (8, 'S'), (9, 'S'), (10, 'S'), (11, 'S'), (12, 'S'), (13, 'S'), (14, 'S')
            ], dtype=[('valeur', int), ('couleur', 'U1')])
            np.random.shuffle(jeu_de_cartes)


def lancer_partie_tkinter(ja, mise):
    global jeu_de_cartes
    global croupier
    np.random.shuffle(jeu_de_cartes)
    ja.main_cartes = [None] * 5
    croupier.main_cartes = [None] * 5
    print(f"Bonjour et bienvenue {ja.nom} sur ma table")
    print("Je m'appelle Nadir et je serai votre croupier aujourd'hui")
    n_round = 1
    pot=0
    print(f"On commence notre round No {n_round}")
    print(f"Votre crédit est de {ja.credit} jetons")
    ja.miser(mise)
    pot=2*int(mise) #pour prendre en compte la mise du joueur et du croupier
    print(f"La valeur totale du pot est de {pot} jetons")
    nouvelles_cartes(ja)
    nouvelles_cartes(croupier)
    print("Votre main actuelle est")
    print(afficher_main(ja.main_cartes))
    #Changer des cartes
    
    #Affichage des mains finales
    print("Votre main finale est:")
    print(afficher_main(ja.main_cartes))
    print("La main croupier est:")
    print(afficher_main(croupier.main_cartes))
    #comparer les mains et annoncer le gagnant
    comparer(ja, croupier).credit += int(pot)
    print(f"Votre crédit est de {ja.credit}")
    pot = 0
        

def changer_cartes_croupier(croupier):
    eval=evaluer_main(croupier.main_cartes)
    indice_a_changer=[]
    #On change les cartes de valeur inférieure à 7 qui ne sont pas pairées
    if eval[0]==3:
        m_eval=dict(eval[2])
        for i in range(5):
            if croupier.main_cartes[i][0]<7 and m_eval[croupier.main_cartes[i][0]]==1:
                indice_a_changer.append(i)
    elif eval[0]==2:
        m_eval=dict(eval[2])
        for i in range(5):
            if croupier.main_cartes[i][0]<7 and m_eval[croupier.main_cartes[i][0]]==1:
                indice_a_changer.append(i)
    elif eval[0]==1:
        for i in range(5):
            if croupier.main_cartes[i][0]<7:
                indice_a_changer.append(i)
    nouvelles_cartes(croupier,indice_a_changer)

def quitter(ja,mise):
    j=lancer_partie_tkinter(ja,mise)
    joueur_info = {
        "nom": j.nom,
        "credit_restant": j.credit
    }
    fichier_sauvegarde = f"{j.nom}_info.npy"
    np.save(fichier_sauvegarde, joueur_info)
    print(f"Les informations du joueur {j.nom} ont été sauvegardées dans {fichier_sauvegarde}.")

def quitter_tkinter(ja):
    joueur_info = {
        "nom": ja.nom,
        "credit_restant": ja.credit
    }
    fichier_sauvegarde = f"{ja.nom}_info.npy"
    np.save(fichier_sauvegarde, joueur_info)
    print(f"Les informations du joueur {ja.nom} ont été sauvegardées dans {fichier_sauvegarde}.")


def regles():
    with open('regles.txt', 'r') as file:
    # Read the contents of the file
        content = file.read()
        # Print the contents
        print(content)

'''def charger_partie(ja):
    fichier_charger = f"{ja.nom}_info.npy"
    np.load(fichier_charger)
    print(f"Rebonjour et bienvenue {ja.non} sur ma table")'''

'''def charger_info_joueur(nom_joueur):
    fichier_sauvegarde = f"{nom_joueur}_info.npy"
    
    try:
        joueur_info = np.load(fichier_sauvegarde, allow_pickle=True).item()
        return joueur_info
    except FileNotFoundError:
        print(f"Le fichier de sauvegarde pour {nom_joueur} n'a pas été trouvé.")
        return None'''
def chargerPartie(nom_joueur,mise):
    fichier_sauvegarde = f"{nom_joueur}_info.npy"
    
    try:
        joueur_info = np.load(fichier_sauvegarde, allow_pickle=True).item()
        print (f"le joueur : {joueur_info}")
        joueur_charge=Joueur(joueur_info['nom'],np.empty((5,2)), credit=joueur_info['credit_restant'])
        lancer_partie_tkinter(joueur_charge, mise)
        return joueur_info
    except FileNotFoundError:
        print(f"Le fichier de sauvegarde pour {nom_joueur} n'a pas été trouvé.")
        return None