import random
class Cards:

    def __init__(self, number, symbol):

        self.number = number
        self.symbol = symbol

    def __str__(self):
        return '{}{}'.format(self.number, self.symbol)

class Deck:

    list_of_cards = []

    def __init__(self):
    
        self.symbols = ['♥', '♠', '♣', '♦']
        self.numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10,10,10,10]
        self.card_values = {}
        self.generator_of_cards()

    def generator_of_cards(self):

        for symbol in self.symbols:

            for number in self.numbers:

                carta = Cards(number,symbol)
                self.list_of_cards.append(carta)
                self.card_values.update({carta : carta.number})

        random.shuffle(self.list_of_cards)    

# baraja =  Deck()

# print('suma de las cartas {} y {} es igual {}'.format( baraja.list_of_cards[1], baraja.list_of_cards[2], baraja.card_values[baraja.list_of_cards[1]] + baraja.card_values[baraja.list_of_cards[2]] ))
