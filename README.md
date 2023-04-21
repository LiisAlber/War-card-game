# War-card-game

## Game Description

War is a simple card game that is played between two players using a standard deck of 52 cards. 
The objective of the game is to win all the cards. The deck is divided equally between the two players, and each player places their cards in a face-down pile in front of them. On each turn, both players reveal the top card of their pile, and the player with the higher card takes both cards. 
If the cards are of the same value, then both players place one additional face-up card. The player with the higher face-up card wins all four cards and adds them to the bottom of their deck. The game continues until one player has won all the cards.

## Requirements

The goal of this project is to implement the card game of War using Object-Oriented Programming principles. The following requirements should be met:

* The deck of cards should be randomly shuffled at the beginning of the game using the random library.
* The deck should be divided equally between two players.
* On each turn, both players should reveal the top card of their pile.
* If the cards are of the same value, then both players place one additional face-up card. The player with the higher face-up card wins all four cards and adds them to the bottom of their deck.
* If the additional face-up cards are also of the same value, this process repeats until a player wins.
* When a player wins a turn or a war, they take all the cards that were on the table and add them to the bottom of their deck, maintaining the order of the cards.
* The game continues until one player has won all the cards.
* After every turn the program should present the remaining cards of each player.


## Implementation
The implementation of the game should be done using Python programming language, utilizing Object-Oriented Programming principles. The implementation should be split into multiple classes, such as Card, Deck, Player, and Game.

### Class Table
The Table class represents the table on which the game is played. It is responsible for managing the deck of cards, dealing cards to the players, and overseeing the game rounds. It has methods to play one round of the game, count the rounds, play all the rounds until the game is finished, and show the winner of the game.

### Class Player
The Player class represents a player in the game. Each player has a name and a hand of cards. It has methods to drop a card from their hand into a pot, drop bonus cards into a pot, give cards to a player, and show their hand.

### Class Hand
The Hand class represents the cards held by a player. It has methods to add a card to the hand, take the top card from the hand, add a list of cards to the hand, and check if the hand has any cards left.

### Class Deck
The Deck class represents a standard deck of 52 playing cards. It has methods to create the deck, shuffle the deck, and set up hands for the players.

### Class Card
The Card class represents a single playing card from the deck. Each card has a rank and a suit. It has a method to return the value of the card.

### Class Pot
The Pot class represents the pot of cards in a round. It has methods to add a card to the pot, add bonus cards to the pot, show the cards in the pot, determine the winner of the pot. It also has a method to check for ties in the pot.


After each move, the program should display the number of cards in the pile of each player.

## Output
The output of the game should be a message displayed on the console indicating which player won the game.
