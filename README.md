# War-card-game

## Game Description

War is a simple card game that is played between two players using a standard deck of 52 cards. 
The objective of the game is to win all the cards. The deck is divided equally between the two players, and each player places their cards in a face-down pile in front of them. On each turn, both players reveal the top card of their pile, and the player with the higher card takes both cards. 
If the cards are of the same value, then both players place one additional face-down card followed by a face-up card. The player with the higher face-up card wins all six cards and adds them to the bottom of their deck. The game continues until one player has won all the cards.

## Requirements

The goal of this project is to implement the card game of War using Object-Oriented Programming principles. The following requirements should be met:

* The deck of cards should be randomly shuffled at the beginning of the game using the random library.
* The deck should be divided equally between two players.
* On each turn, both players should reveal the top card of their pile.
* If the cards are of the same value, then both players place one additional face-down card followed by a face-up card. The player with the higher face-up card wins all six cards and adds them to the bottom of their deck.
* If the additional face-up cards are also of the same value, this process repeats until a player wins.
* When a player wins a turn or a war, they take all the cards that were on the table and add them to the bottom of their deck, maintaining the order of the cards.
* The game continues until one player has won all the cards.


## Implementation
The implementation of the game should be done using Python programming language, utilizing Object-Oriented Programming principles. The implementation should be split into multiple classes, such as Card, Deck, Player, and Game.

### Card Class
The Card class should represent a single card from the deck and should have attributes such as rank and suit.

### Deck Class
The Deck class should represent the deck of cards and should have methods such as shuffle and deal.

### Player Class
The Player class should represent a player in the game and should have attributes such as the name and the pile of cards.

### Game Class
The Game class should represent the game and should have methods such as play and determine_winner.

After each move, the program should display the number of cards in the pile of each player.

## Output
The output of the game should be a message displayed on the console indicating which player won the game.
