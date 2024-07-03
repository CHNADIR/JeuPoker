from tkinter import *
import sys
import fonctions_poker as fpkr
import numpy as np
import threading
from PIL import Image, ImageTk
import os



class Redirector(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert(END, string)
        self.text_widget.see(END)

# Get the current working directory (where your main script is located)
current_directory = os.getcwd()

# Specify the name of the folder you want to access
folder_name = "poker-projet-tkinter\\Cards\\"

# Construct the full path to the folder
chemin_images = os.path.join(current_directory, folder_name)
images_cartes = {}

# Créer la fenêtre principale
root = Tk()
root.geometry('1000x800')
root.title("CASINO ROYAL - Poker")
root.after(0, lambda: load_card_images())
# Ajouter des widgets
label_bienvenue = Label(root, text="Bienvenue dans notre CASINO ROYAL - Poker")
label_bienvenue.pack()

label_nom_joueur = Label(root, text="Entrez votre nom de joueur :")
entry_nom_joueur = Entry(root)
label_mise = Label(root, text="Entrez le nombre de jetons que vous voulez miser :")
entry_mise = Entry(root)
label_changer_cartes = Label(root, text="Souhaitez-vous changer de cartes, si oui mentionnez lequelles en séparant par point virgule :")
entry_changer_cartes = Entry(root)
label_doubler_mise = Label(root, text="Souhaitez-vous doubler la mise :")
entry_doubler_mise = Entry(root)
frame_joueur = Frame(root)
frame_joueur.pack()
frame_croupier = Frame(root)
frame_croupier.pack()

nom_joueur = entry_nom_joueur.get()
mise = 0


jeu_de_cartes = np.array([
    (2, 'C'), (3, 'C'), (4, 'C'), (5, 'C'), (6, 'C'), (7, 'C'), (8, 'C'), (9, 'C'), (10, 'C'), (11, 'C'), (12, 'C'), (13, 'C'), (14, 'C'),
    (2, 'D'), (3, 'D'), (4, 'D'), (5, 'D'), (6, 'D'), (7, 'D'), (8, 'D'), (9, 'D'), (10, 'D'), (11, 'D'), (12, 'D'), (13, 'D'), (14, 'D'),
    (2, 'H'), (3, 'H'), (4, 'H'), (5, 'H'), (6, 'H'), (7, 'H'), (8, 'H'), (9, 'H'), (10, 'H'), (11, 'H'), (12, 'H'), (13, 'H'), (14, 'H'),
    (2, 'S'), (3, 'S'), (4, 'S'), (5, 'S'), (6, 'S'), (7, 'S'), (8, 'S'), (9, 'S'), (10, 'S'), (11, 'S'), (12, 'S'), (13, 'S'), (14, 'S')
], dtype=[('valeur', int), ('couleur', 'U1')])

# Shuffle and distribute cards
np.random.shuffle(jeu_de_cartes)

main_cartes = [None] * 5
mise_double=0

cartes_joueur = jeu_de_cartes[:5]  # Take the first 5 cards

def afficher_cartes_joueur(cartes, frame, images_cartes):
    for i, carte in enumerate(cartes):
        # Convert the carte to a hashable key (tuple) for the dictionary
        carte_key = (carte['valeur'], carte['couleur'])
        label = Label(frame, image=images_cartes[carte_key])
        label.image = images_cartes[carte_key]  # Keep a reference
        label.grid(row=0, column=i)


def load_card_images():
    images_cartes = {}
    for valeur in range(2, 15):
        for couleur in ['C', 'D', 'H', 'S']:
            nom_carte = f"{valeur}{couleur}.png"  # Example: "2C.png"
            chemin_complet = chemin_images + nom_carte
            image = Image.open(chemin_complet)
            photo = ImageTk.PhotoImage(image)
            images_cartes[(valeur, couleur)] = photo
    return images_cartes

# Call load_card_images and store the returned dictionary
images_cartes = load_card_images()


def chargement() :
    label_nom_joueur.pack()
    entry_nom_joueur.pack()
    label_mise.pack()
    entry_mise.pack()
    bouton_jouer_partie.pack_forget()
    bouton_regles.pack_forget()
    bouton_start.pack()
    bouton_charger_partie.pack_forget()
    bouron_start_partie_charge.pack()

joueur_charge = ""

def charger_partie():
    nom_joueur = entry_nom_joueur.get()
    '''mise = entry_mise.get()
    game_thread = threading.Thread(target=lambda: fpkr.chargerPartie(nom_joueur, mise))
    game_thread.start()'''
    fichier_sauvegarde = f"{nom_joueur}_info.npy"
    
    
    try:
        joueur_info = np.load(fichier_sauvegarde, allow_pickle=True).item()
        print (f"le joueur : {joueur_info}")
        cartes_joueur_charge = jeu_de_cartes[:5]  # Take the first 5 cards
        joueur_charge=fpkr.Joueur(joueur_info['nom'],cartes_joueur_charge, credit=joueur_info['credit_restant'])
        afficher_cartes_joueur(cartes_joueur_charge, frame_joueur, images_cartes)
        
        return joueur_charge
    except FileNotFoundError:
        print(f"Le fichier de sauvegarde pour {nom_joueur} n'a pas été trouvé.")
        return None

def regles_partie():
    fpkr.regles()

def quitter_partie():
    root.destroy()
    '''nom_joueur = entry_nom_joueur.get()
    mise = entry_mise.get()
    game_thread = threading.Thread(target=lambda: fpkr.quitter_tkinter(nom_joueur,mise ))
    game_thread.start()'''
    

def jouer_partie_thread():
    
    label_nom_joueur.pack()
    entry_nom_joueur.pack()
    label_mise.pack()
    entry_mise.pack()
    bouton_jouer_partie.pack_forget()
    bouton_charger_partie.pack_forget()
    bouton_regles.pack_forget()
    bouton_start.pack()



def lancer_nouvelle_partie_thread():
    
    afficher_cartes_joueur(cartes_joueur, frame_joueur, images_cartes)
    
    # Démarre un nouveau thread pour exécuter la partie
    label_nom_joueur.pack_forget()
    entry_nom_joueur.pack_forget()
    label_mise.pack()
    entry_mise.pack()
    bouton_start.pack_forget()
    label_changer_cartes.pack()
    entry_changer_cartes.pack()
    bouton_changer_carte.pack()
    label_doubler_mise.pack()
    entry_doubler_mise.pack()
    bouton_resultat.pack()
    

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def initialiser_main():
    global main_cartes, jeu_de_cartes
    np.random.shuffle(jeu_de_cartes)
    main_cartes = jeu_de_cartes[:5]
    jeu_de_cartes = jeu_de_cartes[5:]

def nouvelles_cartes(indices_cartes_a_changer):
    global main_cartes, jeu_de_cartes
    for i in indices_cartes_a_changer:
        if 0 <= i < 5 and len(jeu_de_cartes) > 0:
            main_cartes[i] = jeu_de_cartes[0]
            jeu_de_cartes = np.delete(jeu_de_cartes, 0, axis=0)

def changer_carte():
    indices_nouvelles_cartes = entry_changer_cartes.get().split(",")
    indices_chang = [int(ind) - 1 for ind in indices_nouvelles_cartes]
    nouvelles_cartes(indices_chang)
    clear_frame(frame_joueur)
    afficher_cartes_joueur(main_cartes, frame_joueur, images_cartes)

def resultat_partie():
    cartes_croupier = jeu_de_cartes[:5]
    afficher_cartes_joueur(cartes_croupier, frame_croupier, images_cartes)  
    joueur_actuel = fpkr.Joueur(nom_joueur, cartes_joueur, credit=10)
    croupier = fpkr.Joueur('croupier', cartes_croupier, credit=10)
    doubler_mise = entry_doubler_mise.get()
    mise = int(entry_mise.get())
    resultat = fpkr.comparer(joueur_actuel,croupier)
    if doubler_mise == 'oui':
        mise = 2*mise
        if resultat == joueur_actuel :
            credit_ja += pot
        elif resultat == croupier:
            credit_ja -= mise
    pot=2*mise
    credit_ja = joueur_actuel.credit-mise
    if resultat == joueur_actuel :
        credit_ja += pot
    label_resultat = Label(root, text=f'votre crédit est de : {credit_ja}')
    affichage.pack()
    label_resultat.pack()
    mise = 0


#bouton_lancer_partie = Button(root, text="Lancer une nouvelle partie", command=lancer_nouvelle_partie_thread)
bouton_jouer_partie = Button(root, text="Jouer une partie", command=jouer_partie_thread)
bouton_start = Button(root, text="COMMENCER", command=lancer_nouvelle_partie_thread)
bouton_charger_partie = Button(root, text="Charger une partie", command=chargement)
bouton_regles = Button(root, text="Règles de poker", command=regles_partie)
bouton_quitter = Button(root, text="Quitter la partie", command=quitter_partie)
bouton_changer_carte= Button(root, text="Changer les cartes", command=changer_carte)
bouton_resultat= Button(root, text="Resultat", command=resultat_partie)
bouron_start_partie_charge = Button(root, text="Resultat de la partie", command=charger_partie)


#bouton_lancer_partie.pack()
bouton_jouer_partie.pack()
bouton_charger_partie.pack()
bouton_regles.pack()
bouton_quitter.pack()

initialiser_main()

# Widget Text pour l'affichage
affichage = Text(root, height=10, width=60)

# Rediriger stdout vers le widget Text
redirector = Redirector(affichage)
sys.stdout = redirector

# Boucle principale
root.mainloop()
