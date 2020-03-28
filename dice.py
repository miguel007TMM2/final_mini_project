import random

class Dice():

    def __init__(self):
        
        self.index = 0
        self.dices  = ['⚀', '⚁', '⚂', '⚃', '⚄', '⚅'] 

    #This function is to call the dice state when it is rolled.
    def status(self):

        self.index = random.randrange(1, 7)
        return self.dices[self.index -1]
