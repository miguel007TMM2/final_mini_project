from random import shuffle

"""
This class is in charge of general, give value and shuffle the cards.
"""
class Deck_of_cards:

    def __init__(self):
        self.list_of_cards = []
        self.new_list_of_cards = self.list_of_cards
        self.value_cards = []
        self.Symbol_of_cards = ['♥', '♠', '♣', '♦']
        self.symbol_of_value_of_the_cards = {1 :'A', 11 : 'J', 12 : 'Q', 13 : 'K'}
        self.dic_value_of_the_cards = {}
        self.Generator_of_cards()
        self.value_of_cards()
        self.shuffle_the_cards()
    
  
    #This function generates the cards and stores them in the list of cards
    def Generator_of_cards(self):
        
        #the values ​​of symbol_of_value_of_the_cards are taken to be placed in list_of_cards and substitute their number value within the string with letters
        get_keys = self.symbol_of_value_of_the_cards.keys()
        get_values = list(self.symbol_of_value_of_the_cards.values())

        for Symbol_of_card in self.Symbol_of_cards:
            for get_key in range(1,14):
                if get_key in get_keys:
                    get_key = self.symbol_of_value_of_the_cards[get_key]
                self.list_of_cards.append(str(get_key) + Symbol_of_card)
                self.value_cards.append(get_key)

    #Gives value to the cards in the card list
    def value_of_cards(self):
        
        for keys_of_cards in range(len(self.list_of_cards)):
            if self.value_cards[keys_of_cards] == "A":
                self.value_cards[keys_of_cards] = 1

            for keys_symbol_of_value_of_the_cards in  self.symbol_of_value_of_the_cards:
                if self.value_cards[keys_of_cards] ==  self.symbol_of_value_of_the_cards[keys_symbol_of_value_of_the_cards]:
                    self.value_cards[keys_of_cards] = 10
                    
            self.dic_value_of_the_cards.update({self.list_of_cards[keys_of_cards] : self.value_cards[keys_of_cards]})
    
    #This function shuffle the cards
    def shuffle_the_cards(self):
        shuffle(self.new_list_of_cards)

