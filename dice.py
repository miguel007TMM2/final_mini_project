import random


#This class is the dealer's dice and which will indicate the minimum bet for the player
class Dice():
    def __init__(self):
        self.index = 0;
        self.dices  = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅']

    #This function is to call the dice state when it is rolled.
    def status(self):
        self.index = random.randrange(0, 6)
        return self.dices[self.index]
