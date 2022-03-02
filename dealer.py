class Dealer:
    def __init__(self):
        self.name = 'Dealer'
        self.hand = []
    
    def __str__(self):
        return 'This is the Dealer.'

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.hand.extend(new_cards)
        else:
            self.hand.append(new_cards)

                

