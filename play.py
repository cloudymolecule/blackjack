from asyncio import FastChildWatcher
from curses.ascii import isdigit
from deck import Deck
from player import Player
from dealer import Dealer

print('')
name = input("What is your name? ")
print('')

deck = Deck()
player = Player(name)
dealer = Dealer()

game_on = True
bet_placed = False
cont_round = True
player_final_value = 0
dealer_final_value = 0
dealer_play = True
player_bust = False

while game_on:
    while bet_placed == False:
        print(f'You have ${player.balance} available to bet')
        bet_amount = input('How much do you want to bet? ')
        while not bet_amount.isdigit():
            print('Please enter a number.')
            bet_amount = input('How much do you want to bet? ')
        bet_amount = int(bet_amount)
        if bet_amount > player.balance:
            print(f"Sorry {player.name}, you don't have enough money, you have ${player.balance} available to bet.")
        else:
            player.bet(bet_amount)
            print(f'{player.name} bets ${bet_amount}. {player.name} has ${player.balance} left.')
            print('')
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
            # ace can be 1 or 11
            ace = False
            if card.value == 1:
                ace = True
                player_cards = player_cards + f'{card.rank} of {card.suit} ''| '
            else:
                player_cards = player_cards + f'{card.rank} of {card.suit} ''| '
                player_cards_value += card.value
            
            if player_cards_value < 11 and ace:
                player_cards_value += 11
            elif player_cards_value >= 11 and ace:
                player_cards_value += 1

        print(f"{player.name}'s cards are: \n{player_cards} \nand they add up to {player_cards_value}.")
        print('')

        if player_cards_value >= 21:
            if player_cards_value == 21 and len(player.hand) == 2:
                print('21!! BLACKJACK!')
                print('')

                player.get_paid(bet_amount + (bet_amount / 2))
                cont_round = False
                dealer_play = False
            else:
                print("Sorry, that's a bust")
                print('')
                cont_round = False
                dealer_play = False
                player_bust = True

            
        else:
            bad_input = True
            inp = None
            while bad_input:

                try:
                    inp = int(input('Do you want to hit or stop? 1 to hit, 0 to stand.'))
                    if inp == 1 or inp == 0:
                        bad_input = False
                        break
                except:
                    print('Only 1 or 0 are accepted.')
                    pass
        
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
    print('')
    cont_round = True
    bet_placed = False

    while dealer_play == True:

        dealer_cards_value = 0
        for ind, card in enumerate(dealer.hand):
            dealer_cards = dealer_cards + f'{card.rank} of {card.suit} ''| '
            dealer_cards_value += card.value

        print(f"{dealer.name}'s cards are: \n{dealer_cards} \nand they add up to {dealer_cards_value}.")
        if dealer_cards_value >= 17 and dealer_cards_value < 21:
            dealer_play = False
            
        elif dealer_cards_value >= 21:
            if dealer_cards_value == 21 and len(dealer.hand) == 2:
                print('21!! DEALER BLACKJACK!')
                dealer_play = False
            elif dealer_cards_value == 21:
                dealer_play = False
            else:
                print("Dealer busted!")
                dealer_play = False
        else:
            dealer_cards = '| '
            dealer.add_cards(deck.deal_card())

        dealer_final_value = dealer_cards_value
    
    deck.get_cards(dealer.return_cards())
    
    cont_round = True

    result = ''
    if player_bust == False and dealer_play == False:
        if player_final_value > dealer_final_value:
            result = f'{player.name} won'
            player.get_paid(bet_amount)
        else:
            result = 'Dealer Won'
    elif player_bust == True:
        result = 'Dealer Won'
        print('')
    elif player_bust == False and dealer_play == True:
        result = f'{player.name} Won'
        player.get_paid(bet_amount)

    print(result)
    
    if player.balance == 0:
        print(f"Sorry {player.name}, you're out of money. Goodbye!")
        print('')
        game_on = False