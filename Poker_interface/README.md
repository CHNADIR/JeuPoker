# CASINO ROYAL - Poker

Welcome to `CASINO ROYAL - Poker`, a graphical poker game implemented in Python using the Tkinter library.

## Game Overview

In this game, you can play a game of poker against the computer. You can choose to play a new game, load a saved game, or view the rules of poker. The game uses a standard deck of 52 cards and follows the basic rules of poker.

## Fichiers

- `main.py` : Contains the main script to run the poker program.
- `fonctions_poker.py` : Contains utility functions for evaluating poker hands and other related features.

## Installation

1. Clone this repository to your local machine:
    ```sh
    git clone https://github.com/your_username/poker-hand-evaluation.git
    ```
2. Navigate to the project directory:
    ```sh
    cd poker-hand-evaluation
    ```
3. Ensure you have Python 3.x installed on your machine.

## Usage

To run the main script, use the following command:
```sh
python main.py
```

## How to Play

1. Run the game by executing the main.py file.
2. Enter your name and the amount of chips you want to bet.
3. Click the "COMMENCER" button to start the game.
4. You will be dealt five cards. You can choose to change any of these cards by entering the numbers of the cards you want to change (e.g. "1,3,5").
5. Click the "Changer les cartes" button to change your cards.
6. Click the "Resultat" button to see the result of the game.
7. You can repeat steps 4-6 until you want to quit the game.

## Technical Details

- The game uses the Tkinter library for the graphical interface.
- The game logic is implemented in Python using the fonctions_poker module.
- The game uses a standard deck of 52 cards, represented as a NumPy array.
- The game uses threading to run the game logic in the background.