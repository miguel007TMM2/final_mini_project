import random
"""
This class is in charge of general, give value and shuffle the cards.
"""
class Deck_of_cards:

    #Card attributes
    value_cards = []
    Symbol_of_cards = ['♥', '♠', '♣', '♦']
    symbol_of_value_of_the_cards = {1 :'A', 11 : 'J', 12 : 'Q', 13 : 'K'}

    
   
    def __init__(self): #Contains the deck cards
        self.list_of_cards = []
        self.value_and_cards = {}
        self.__Generator_of_cards()
        self.value_of_cards()
        self.__shuffle_the_cards(self.list_of_cards)

    
    def __Generator_of_cards(self):#This function generates the cards and stores them in the list of cards
        get_keys = self.symbol_of_value_of_the_cards.keys()
        for Symbol_of_card in self.Symbol_of_cards:
            for get_key in range(1,14):
                if get_key in get_keys:
                    get_key = self.symbol_of_value_of_the_cards[get_key]
                self.list_of_cards.append(str(get_key) + Symbol_of_card)
                self.value_cards.append(get_key)

    
    def value_of_cards(self):#Gives value to the cards in the card list
        
        for keys_of_cards in range(len(self.list_of_cards)):
            if self.value_cards[keys_of_cards] == "A":
                self.value_cards[keys_of_cards] = 1

            for keys_symbol_of_value_of_the_cards in  self.symbol_of_value_of_the_cards:
                if self.value_cards[keys_of_cards] ==  self.symbol_of_value_of_the_cards[keys_symbol_of_value_of_the_cards]:
                    self.value_cards[keys_of_cards] = 10
                    
            self.value_and_cards.update({self.list_of_cards[keys_of_cards] : self.value_cards[keys_of_cards]})
    
    
    def __shuffle_the_cards(self, list_to_shuffle):#This function shuffle the cards
        random.shuffle(list_to_shuffle)
        