import random
class Cards:

    def __init__(self, number = None , symbol = None , card_values = {} ):

        self.card_values =card_values
        self.number = number
        self.symbol = symbol

    def __str__(self):
        return '{}{}'.format(self.number, self.symbol)

class Deck:

    list_of_cards = []

    def __init__(self):
    
        self.symbols = ['♥', '♠', '♣', '♦']
        self.numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10,10,10,10]
        self.generator_of_cards()

    def generator_of_cards(self):

        for symbol in self.symbols:

            for number in self.numbers:

                carta = Cards(number,symbol)
                self.list_of_cards.append(carta)
                carta.card_values.update({carta : carta.number})

        random.shuffle(self.list_of_cards)    

p = Deck()
e = Cards()
print(p.list_of_cards[0])
print(e.card_values[p.list_of_cards[0]])