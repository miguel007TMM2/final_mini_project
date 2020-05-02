import random

class Card:

    def __init__(self, number = None , symbol = None , value = None ):

        self.value = value
        self.number = number 
        self.symbol = symbol

    def __str__(self):
        return '{}{}'.format(self.number, self.symbol)

class Deck:

    list_of_cards = []

    def __init__(self):

        self.symbols = ['♥', '♠', '♣', '♦']
        self.numbers = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10,'J','Q','K']
        self.generator_of_cards()

    def generator_of_cards(self):

        for symbol in self.symbols:

            for number in self.numbers:
                value = number

                if value == 'A':
                    value = 11

                elif value == 'J' or value == 'Q'or value == 'K':
                    value = 10

                carta = Card(number,symbol, value)
                self.list_of_cards.append(carta)

        random.shuffle(self.list_of_cards)
