import random


def main():
    table = Table(['Player 1', 'Player 2'])
    table.deal_cards()
    table.play_all()


def print_underline(string, line):
    print('\n{}\n{}'.format(string, line * len(string)))

# represent the table on which the game is played 
# be responsible for managing the deck of cards, dealing cards to the players, and overseeing the game rounds
# have methods to play one round of the game, count the rounds, play all the rounds until the game is finished
# show the winner of the game
class Table:

    def __init__(self, players):
        self.players = [Player(name, Hand()) for name in players]
        self.deck = Deck()
        self.rounds = 0

    def deal_cards(self):
        self.deck.shuffle()
        self.deck.setup_hands(self.players)

    def play_once(self, tied=None): #one round
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

    def count_round(self):  #counts the number of rounds played
        self.rounds += 1
        print_underline('Starting round {}'.format(self.rounds), '=')
        for player in self.players:
            print(player.name, 'has', len(player.hand.cards), 'cards')

    def play_all(self):     #plays all the rounds of the game until a winner is found
        while not self.finished:
            self.play_once()
        self.show_winner()

    def show_winner(self):      #prints a message displaying the winner
        print('\nGAME OVER')
        print('==============')
        winner = None
        for player in self.players:
            if player.hand.has_cards:
                winner = player
        print(f'{winner.name} wins with {len(winner.hand.cards)} cards remaining!')

    @property
    def finished(self):     #returns True if the game is finished, and False otherwise
        return sum(bool(player.hand.cards) for player in self.players) == 1


#should represent a player in the game
#each player should have a name and a hand of cards
#should have methods to drop a card from their hand into a pot, drop bonus cards into a pot, give cards to a player, and show their hand
class Player:

    def __init__(self, name, hand):
        self.name, self.hand = name, hand

    def drop_card(self, collection):  #drops a card from the player's hand, adds it to the collection of cards played in the current round
        if self.hand.has_cards:
            collection.add_card(self.hand.take_top(), self)

    def drop_bonus(self, collection, count):        #drops a specified number of bonus cards 
        collection.add_bonus(self.hand.cards[:count])
        self.hand.cards = self.hand.cards[count:]

    def give_cards(self, cards):        #adds a list of cards to the player's hand
        self.hand.add_all(cards)

    def show_hand(self):        #prints a message displaying the player's hand
        print(self.name, 'has', self.hand)


#represent the cards held by a player, 
# should have methods to add a card to the hand, 
# take the top card from the hand, 
# add a list of cards to the hand, 
# check if the hand has any cards left
class Hand:

    def __init__(self):     # initializes the Hand object with an empty list of cards
        self.cards = []

    def __str__(self):      #converts each card object to a string representation of the card, join the string
        return ', '.join(map(str, self.cards))

    def add_card(self, card):       #adds a card to the hand
        self.cards.append(card)

    def take_top(self):     #removes the top card from the hand
        return self.cards.pop(0)

    def add_all(self, cards):       #adds a list of cards to the hand
        self.cards.extend(cards)

    @property
    def has_cards(self):        #returns True if the hand has cards, and False if otherwise
        return bool(self.cards)
    
#should represent a standard deck of 52 playing cards
#should have methods to create the deck and shuffle the deck
class Deck:

    def __init__(self):     #initializes the Deck object with a list of Card objects representing the cards in the deck
        self.cards = [Card(s, r) for s in Card.SUITE for r in Card.RANKS]

    def shuffle(self):     
        random.shuffle(self.cards)

    def setup_hands(self, players):     #sets up the players' hands by dealing cards from the deck to each hand
        hands = [player.hand for player in players]
        while len(self.cards) >= len(players):
            for hand in hands:
                hand.add_card(self.cards.pop())
        return hands

# should represent a single playing card from the deck
# each card should have a rank and a suit
class Card:

    SUITE = 'H D S C'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, suite, rank):        #initializes the Card object with a suit and a rank
        self.suite, self.rank = suite, rank

    def __str__(self):      #returns a string representation of the card, in the format "rank-suit"
        return '{}-{}'.format(self.rank, self.suite)

    @property
    def value(self):        #returns the value of the card based on its rank
        return self.RANKS.index(self.rank)


#represents a round of the game
#has methods to manage the cards played by the players in the round
#determine the winner of the round, and reward the winner with the cards played in the round
class Round:

    def __init__(self):     #initializes the Round object with empty lists of cards, players, and bonus cards
        self.cards = []
        self.players = []
        self.bonus = []

    def add_card(self, card, player):       #adds a card to the list of cards played in the current round
        self.cards.append(card)             #and the player who played it to the list of players in the round
        self.players.append(player)

    def add_bonus(self, cards):         #adds a list of bonus cards to the list of bonus cards played in the current round
        self.bonus.extend(cards)

    @property
    def winner(self):       #determines the winner of the round, returns the player who played the winning card
        self.show_round()
        values = [card.value for card in self.cards]
        self.best = max(values)
        if values.count(self.best) == 1:
            return self.players[values.index(self.best)]

    def show_round(self):       #prints a message displaying the cards played by each player in the round
        for player, card in zip(self.players, self.cards):
            print('{} laid down a {}.'.format(player.name, card))

    def reward(self, player):       #gives the cards and bonus cards played in the round to the winning player
        player.give_cards(self.cards)
        player.give_cards(self.bonus)

    @property
    def tied(self):     #returns a generator that yields the tied players based on the cards played in the round
        for card, player in zip(self.cards, self.players):      #zip() combines together 2 iterables and creates a tuple
            if card.value == self.best:
                yield player

if __name__ == '__main__':
    main()