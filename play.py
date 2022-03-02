# You need to create a simple text-based BlackJack game
# The game needs to have one player versus an automated dealer.
# The player can stand or hit.
# The player must be able to pick their betting amount.
# You need to keep track of the player's total money.
# You need to alert the player of wins, losses, or busts, etc...

# Classes

# Player
# Dealer
# Deck
# Card

from deck import Deck
from player import Player
from dealer import Dealer

deck = Deck()
player = Player('Jack')
dealer = Dealer()

print(deck)
print(player)
print(dealer)