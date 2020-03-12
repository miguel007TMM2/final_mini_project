from deck_of_cards import Deck_of_cards
cards = Deck_of_cards()
import os

#This class is responsible for managing the dealer process in the game.
class Crupier():

    crupier_cards_value = 0
    card_of_crupier = 0
    index_for_player = 0
    value_cards_player = 0
    dic_bets = {}
    cards_cemetery = []

    def __init__(self):
        super(Crupier, self).__init__()
        self.croupier_hand = []
        self.Player_curret_hand = []
        
    def set_card(self, list_for_put_cards, index, sum_value):

        list_for_put_cards.append(cards.list_of_cards.pop())
        
        if list_for_put_cards == self.croupier_hand:

            self.crupier_cards_value +=  cards.value_and_cards[list_for_put_cards[index]]

        if list_for_put_cards == self.Player_curret_hand:
                    
            self.value_cards_player += cards.value_and_cards[list_for_put_cards[index]]

    def two_cards_for_player(self):

        for self.index_for_player in range(0,2):
            self.set_card(self.Player_curret_hand, self.index_for_player, self.value_cards_player) 
    
    def __crupiers_two_cards(self):

        for self.card_of_crupier in range(0, 2):
            self.crupier_card(self.croupier_hand, self.card_of_crupier, self.crupier_cards_value )
        return self.croupier_hand[0]
    
    def mutation_of_as(self, index):

        mutation = cards.value_and_cards[self.croupier_hand[index]] = 11
        self.crupier_cards_value += mutation
        self.crupier_cards_value -= 1

    def set_mutation_of_as(self):

        for croupier_hand in range(len(self.croupier_hand)):
            if cards.value_and_cards(self.croupier_hand[croupier_hand]) == 1:
                if self.crupier_cards_value <= 11:
                    self.mutation_of_as(croupier_hand)
    
    def __Keep_holding_cards(self):

        if self.crupier_cards_value < 16:
            self.set_mutation_of_as()

            while self.crupier_cards_value < 16:
                self.card_of_crupier += 1
                self.crupier_card(self.croupier_hand, self.card_of_crupier)
                
        return self.croupier_hand

# f = Crupier()
# f.two_cards_for_player()
# print(f.Player_curret_hand)
# print(f.value_cards_player)