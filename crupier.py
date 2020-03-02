from deck_of_cards import Deck_of_cards
from dice import Dice
#This class is responsible for managing the dealer process in the game.
class Crupier(Deck_of_cards, Dice):
    def __init__(self):
        super(Crupier, self).__init__()
        self.list_cards_of_crupier = []
        self.crupier_cards_value = 0
        self.card_of_crupier = 0
        self.symbols_as = ['A♥', 'A♠', 'A♣', 'A♦']
        self.Player_curret_hand = [[]]

    def initial_bet(self):
        self.throw_dice()
        if self.status == 1:
            self.bet = input('Your initial bet must be equal to or greater than ' + str(self.status) + '00')

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
        for self.card_of_crupier in range(0, 2):
            self.call_crupier_card(self.list_cards_of_crupier, self.card_of_crupier)

    def mutation_of_as(self, index):
        mutation = self.dic_value_of_the_cards[self.list_cards_of_crupier[index]] = 11
        self.crupier_cards_value += mutation
        self.crupier_cards_value -= 1

    def call_mutation_of_as(self):
        for list_card_of_crupier in range(len(self.list_cards_of_crupier)):
            if self.list_cards_of_crupier[list_card_of_crupier]  in self.symbols_as:
                if self.crupier_cards_value <= 11:
                    self.mutation_of_as(list_card_of_crupier)
    
    def Keep_holding_cards(self):
        if self.crupier_cards_value < 16:
            self.call_mutation_of_as()
            while self.crupier_cards_value < 16:
                self.card_of_crupier += 1
                self.call_crupier_card(self.list_cards_of_crupier, self.card_of_crupier)

f = Crupier()
# f.initial_bet()
f.get_two_cards_for_player()
f.get_two_cards_for_crupier()
f.call_mutation_of_as()
f.Keep_holding_cards()
print(f.crupier_cards_value)
print(f.Player_curret_hand)
print(f.list_cards_of_crupier)
