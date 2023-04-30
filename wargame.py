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
    def __init__(self):     
        self.cards = []

    def __str__(self):      
        return ', '.join(map(str, self.cards))
    
    def add_card(self, card):       #add card to the hand
        self.cards.append(card)

    def take_top(self):     #removes top card
        return self.cards.pop(0)
    
    
    @property  #needs to be property?
    def has_cards(self):       
        return bool(self.cards)
    



#should represent a standard deck of 52 playing cards
#should have methods to create the deck and shuffle the deck
class Deck:
    def __init__(self):     
        self.cards = # needs to finish

    def shuffle(self):     
        random.shuffle(self.cards)

    def setup_hands(self, players):     #sets up the players' hands by dealing cards from the deck to each hand


# should represent a single playing card from the deck
# each card should have a rank and a suit
class Card:
    SUITE = 'H D S C'.split()
    RANK = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, suite, rank):
        self.suite, self.rank = suite, rank

    def __str__(self):      #returns a string representation of the card, in the format "rank-suit"
        return '{}-{}'.format(self.rank, self.suite)
    
    #@property?
    def value(self):        #returns the value of the card based on its rank
        return self.RANKS.index(self.rank)


#represents a round of the game
#has methods to manage the cards played by the players in the round
#determine the winner of the round, and reward the winner with the cards played in the round
class Round:

    def __init__(self):     #empty lists of cards, players, and bonus cards
        

    def add_card(self, card, player):       #adds a card to the list of cards played in the current round
                                            #the player who played it to the list of players in the round
        

    def add_bonus(self, cards):         #adds a list of bonus cards to the list of bonus cards played in the current round
        

    @property                           #winner of the round
    def winner(self): 


    def show_round(self):               #message: cards played by each player in the round


    def reward(self, player):           #gives the cards and bonus cards played in the round to the winning player

    def tied(self):                     #generator that yields the tied players