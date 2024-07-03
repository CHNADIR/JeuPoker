# Poker en Python

Ce projet est une implémentation en Python du jeu de poker. Le jeu est conçu pour être joué contre un croupier contrôlé par l'ordinateur.

## Fonctionnalités

### Jeu de base
- Le jeu utilise un jeu de 52 cartes standard.
- Le joueur et le croupier reçoivent chacun une main de 5 cartes.
- Le joueur peut miser et choisir de changer des cartes.
- Le croupier suit une stratégie prédéfinie pour changer ses cartes.
- Le joueur avec la meilleure main gagne le pot.

### Combinaisons
Le jeu reconnaît toutes les combinaisons de poker standard, y compris :
- Carte haute
- Paire
- Deux paires
- Brelan
- Suite
- Flush
- Full house
- Carré
- Quinte flush
- Quinte flush royale

### Sauvegarde et chargement
- Le joueur peut sauvegarder sa progression en jeu et la recharger à tout moment.
- La sauvegarde enregistre le nom du joueur et son crédit restant.

## Structure du code

Le code est divisé en deux fichiers :
- `fonctions_poker.py` : Ce fichier contient toutes les fonctions et classes nécessaires au fonctionnement du jeu.
- `main.py` : Ce fichier contient le code principal du jeu, y compris le menu principal, la gestion des joueurs et les interactions avec l'utilisateur.

## Démarrage

1. Clonez le référentiel :
    ```sh
    git clone https://github.com/CHNADIR/JeuPoker.git
    ```
2. Exécutez le fichier `main.py` :
    ```sh
    python main.py
    ```

## Remarques

- Ce jeu de poker est une version simplifiée. Il n'inclut pas de fonctionnalités avancées comme le pari, les blinds ou les relances.
- Le croupier utilise une stratégie simple pour changer ses cartes.
- Le jeu est en développement continu et de nouvelles fonctionnalités pourraient être ajoutées à l'avenir.

## Contributions

Les contributions sont les bienvenues ! N'hésitez pas à soumettre des demandes de pull pour améliorer le code, ajouter de nouvelles fonctionnalités ou corriger des bugs.

## License

Ce projet est sous licence MIT.

## À propos

Ce projet est un projet personnel développé pour apprendre et explorer le développement de jeux en Python.
