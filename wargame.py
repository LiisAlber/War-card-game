import random


def main():
    table = Table(['Player 1', 'Player 2'])
    table.deal_cards()
    table.play_all()




#should represent the table on which the game is played 
# should be responsible for managing the deck of cards, dealing cards to the players, and overseeing the game rounds
# should have methods to play one round of the game, count the rounds, play all the rounds until the game is finished
# show the winner of the game
class Table:
    def __init__(self, players):
        self.players = [Player(name, Hand()) for name in players]
        self.deck = Deck()
        self.rounds = 0

    def deal_cards(self):
        self.deck.shuffle()
        self.deck.setup_hands(self.players)

    def play_once(self, tied=None):
        if tied is None:
            self.count_round()
        collection = Round()
        for player in (self.players if tied is None else tied):
            player.drop_card(collection)
            if tied:
                player.drop_bonus(collection, 3)
        winner = collection.winner
        if winner is not None:
            collection.reward(winner)
        else:
            winner = self.play_once(collection.tied)
            collection.reward(winner)
        return winner


    def count_round(self):
        self.rounds += 1
        print_underline('Starting round {}'.format(self.rounds), '=')
        for player in self.players:
            print(player.name, 'has', len(player.hand.cards), 'cards')

    def play_all(self):
        while not self.finished:
            self.play_once()
        self.show_winner()


    def show_winner(self):
        print('\nGAME OVER')
        print('==============')
        winner = None
        for player in self.players:
            if player.hand.has_cards:
                winner = player
        print(f'{winner.name} wins with {len(winner.hand.cards)} cards remaining!')



    @property
    def finished(self):
        return sum(bool(player.hand.cards) for player in self.players) == 1


#should represent a player in the game
#each player should have a name and a hand of cards
#should have methods to drop a card from their hand into a pot, drop bonus cards into a pot, give cards to a player, and show their hand
class Player:
    def __init__ (self, hand, name):
        self.hand, self.name = hand, name

    def drop_card(self, collection):
        if self.hand.has_cards:
            collection.add_card(self.hand.take_top())

    def drop_bonus(self, collection, count):
        collection.add_bonus(self.hand.cards[:count])
        self.hand.cards = self.hand.cards[count:]

    def show_hand(self):
        print(self.name, 'has', self.hand)

    def give_cards(self, cards):
        self.hand.add_all(cards)




#represent the cards held by a player, 
# should have methods to add a card to the hand, 
# take the top card from the hand, 
# add a list of cards to the hand, 
# check if the hand has any cards left
class Hand:


#should represent a standard deck of 52 playing cards
#should have methods to create the deck and shuffle the deck
class Deck:


# should represent a single playing card from the deck
# each card should have a rank and a suit
class Card:
    SUITE = 'H D S C'.split()
    RANK = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, suite, rank):
        self.suite, self.rank = suite, rank


#represents a round of the game
#has methods to manage the cards played by the players in the round
#determine the winner of the round, and reward the winner with the cards played in the round
class Round:


