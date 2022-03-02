from card import Card
from random import shuffle

class Deck:
    def __init__(self):
        self.all_cards = []

        suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
        ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')

        for suit in suits:
            for rank in ranks:
                # There are 6 decks in a casino Blackjack game, so 6 cards of each are created.
                for num in range(6):
                    self.all_cards.append(Card(suit, rank))
        
        # All 312 cards are shuffled
        shuffle(self.all_cards)

    def deal_card(self):
        return self.all_cards.pop()

    def __str__(self):
        return f'There are {len(self.all_cards)} card/s in this deck'