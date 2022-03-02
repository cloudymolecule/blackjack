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

game_on = True

while game_on:
    bet_placed = False
    while bet_placed == False:
        bet_amount = int(input('How much do you want to bet? '))
        if bet_amount > player.balance:
            print(f"Sorry {player.name}, you don't have enough money")
        else:
            player.bet(bet_amount)
            print(f'{player.name} bets ${bet_amount}. {player.name} has ${player.balance} left')
            bet_placed = True

    for x in range(2):
        player.add_cards(deck.deal_card())
        dealer.add_cards(deck.deal_card())

    player_cards = '| '
    player_cards_value = 0
    cont = True

    while player_cards_value < 21 and cont:
        for ind, card in enumerate(player.hand):
            player_cards = player_cards + f'{card.rank} of {card.suit} ''| '
            player_cards_value += card.value

        print(f"{player.name}'s cards are: \n{player_cards} \nand they add up to {player_cards_value}.")

        if player_cards_value >= 21:
            if player_cards_value == 21:
                print('21!! BLACKJACK!')
                player.get_paid(bet_amount)
            else:
                print("Sorry, that's a bust")
            cont = False
        else:
            inp = int(input('Do you want to hit or stop? 1 to hit, 0 to stop.'))
        
        
        # cont = int(input('Do you want to hit or stop? 1 to hit, 0 to stop.'))
            if inp == 1:
                player_cards = '| '
                player.add_cards(deck.deal_card())
            else:
                inp = False

    game_on = False