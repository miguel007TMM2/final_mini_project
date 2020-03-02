from deck_of_cards import Deck_of_cards
shuffle_dice = Deck_of_cards()

#This class is the dealer's dice and which will indicate the minimum bet for the player
class Dice():
    def __init__(self):
        self.color = True
        self.figure = '🎲'
        self.condition = {'⚀' : 1, '⚁' : 2, '⚂' : 3, '⚃' : 4}
        
    def throw_dice(self):
        self.get_keys_status = list(self.condition.keys())
        shuffle_dice.shuffle_the_cards(self.get_keys_status)
        self.get_key_status = 0
        self.status = self.condition[self.get_keys_status[self.get_key_status]]
        