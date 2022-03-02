class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name
        self.balance = 500

    def bet(self, amount):
        self.balance -= amount

    def get_paid(self, amount):
        self.balance += amount

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.hand.extend(new_cards)
        else:
            self.hand.append(new_cards)
    
    def return_cards(self):
        hand = self.hand
        self.hand = []
        return hand

    def __str__(self):
        return f'{self.name} has ${self.balance} in the wallet.'
    # The player can stand or hit.
# The player must be able to pick their betting amount.