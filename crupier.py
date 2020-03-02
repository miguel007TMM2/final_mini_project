from deck_of_cards import Deck_of_cards

class Crupier(Deck_of_cards):
    def __init__(self):
        super(Crupier, self).__init__()
        self.list_cards_of_crupier = []
        self.crupier_cards_value = 0
        self.symbols_as = ['A♥', 'A♠', 'A♣', 'A♦']
        self.Player_curret_hand = [[]]

    def call_player_card(self, list_for_put_cards):
        list_for_put_cards.append(self.new_list_of_cards.pop())

    def call_crupier_card(self, list_for_put_cards, index):
        list_for_put_cards.append(self.new_list_of_cards.pop())
        if list_for_put_cards == self.list_cards_of_crupier:
            self.crupier_cards_value +=  self.dic_value_of_the_cards[list_for_put_cards[index]]

    def get_two_cards_for_player(self):
        for index_for_player in range(0,2):
            self.call_player_card(self.Player_curret_hand[0])
    
    def get_two_cards_for_crupier(self):
        for card_of_crupier in range(0, 2):
            self.call_crupier_card(self.list_cards_of_crupier, card_of_crupier)

    def mutation_of_as(self, index):
        mutation = self.dic_value_of_the_cards[self.list_cards_of_crupier[index]] = 10
        self.crupier_cards_value += mutation

    def call_mutation_of_as(self):
        for list_card_of_crupier in range(len(self.list_cards_of_crupier)):
            if self.list_cards_of_crupier[list_card_of_crupier]  in self.symbols_as:
                if self.crupier_cards_value <= 11:
                    self.mutation_of_as(list_card_of_crupier)
    


f = Crupier()
f.get_two_cards_for_player()
f.get_two_cards_for_crupier()
f.call_mutation_of_as()
print(f.crupier_cards_value)
print(f.Player_curret_hand)
print(f.list_cards_of_crupier)
