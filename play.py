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
bet_placed = False
cont_round = True
player_final_value = 0
dealer_final_value = 0
dealer_play = True
player_bust = False
dealer_bust = False

while game_on:
    while bet_placed == False:
        bet_amount = int(input('How much do you want to bet? '))
        if bet_amount > player.balance:
            print(f"Sorry {player.name}, you don't have enough money, you have ${player.balance} available to bet.")
        else:
            player.bet(bet_amount)
            print(f'{player.name} bets ${bet_amount}. {player.name} has ${player.balance} left')
            bet_placed = True

    for x in range(2):
        player.add_cards(deck.deal_card())
        dealer.add_cards(deck.deal_card())

    player_cards = '| '
    player_cards_value = 0

    dealer_cards = '| '
    dealer_cards_value = 0
    

    while player_cards_value < 21 and cont_round:
        player_cards_value = 0
        for ind, card in enumerate(player.hand):
            player_cards = player_cards + f'{card.rank} of {card.suit} ''| '
            player_cards_value += card.value

        print(f"{player.name}'s cards are: \n{player_cards} \nand they add up to {player_cards_value}.")

        if player_cards_value >= 21:
            if player_cards_value == 21:
                print('21!! BLACKJACK!')
                player.get_paid(bet_amount)
                cont_round = False
                dealer_play = False
            else:
                print("Sorry, that's a bust")
                cont_round = False
                dealer_play = False
                player_bust = True

            
        else:
            inp = int(input('Do you want to hit or stop? 1 to hit, 0 to stand.'))
        
            if inp == 1:
                player_cards = '| '
                player.add_cards(deck.deal_card())
            else:
                inp = False
                cont_round = False
    player_final_value = player_cards_value
    player_cards_value = 0
    deck.get_cards(player.return_cards())
    print('now it be the dealers turn')
    cont_round = True
    bet_placed = False
    # dealer has to stop at 17
    while dealer_cards_value <= 17 and cont_round and dealer_play:
        dealer_cards_value = 0
        for ind, card in enumerate(dealer.hand):
            dealer_cards = dealer_cards + f'{card.rank} of {card.suit} ''| '
            dealer_cards_value += card.value

        print(f"{dealer.name}'s cards are: \n{dealer_cards} \nand they add up to {dealer_cards_value}.")
        if dealer_cards_value >= 21:
            if dealer_cards_value == 21:
                print('21!! BLACKJACK!')
            else:
                print("Sorry, that's a bust")
                dealer_bust = True
        else:
            dealer_cards = '| '
            dealer.add_cards(deck.deal_card())

        dealer_final_value = dealer_cards_value
        dealer_cards_value = 0
        deck.get_cards(dealer.return_cards())
        cont_round = False
    
    cont_round = True

    result = ''
    if player_bust == False and dealer_bust == False:
        if player_final_value > dealer_final_value:
            result = 'Player won'
            player.get_paid(bet_amount)
        else:
            result = 'Dealer Won'
    elif player_bust == True:
        result = 'Dealer Won'
    elif player_bust == False and dealer_bust == True:
        result = 'Player Won'
        player.get_paid(bet_amount)

    print(result)
    
    if player.balance == 0:
        print(f"Sorry {player.name}, you're out of money. Goodbye!")
        game_on = False