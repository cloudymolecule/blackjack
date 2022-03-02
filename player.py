class Player:
    def __init__(self, name):
        self.all_cards = []
        self.name = name
        self.balance = 500

    def bet(self, amount):
        if amount > self.balance:
            print(f"Sorry {self.name}, you don't have enough money")
        else:
            self.balance -= amount
            print(f'{self.name} bets ${amount}. {self.name} has ${self.balance} left')
        
    def __str__(self):
        return f'{self.name} has ${self.balance} in the wallet.'
    # The player can stand or hit.
# The player must be able to pick their betting amount.