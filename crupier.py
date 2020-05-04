import os
from cards import Deck

class Crupier():

    values_cards_crupier = 0

    def __init__(self, deck_of_cards): #Each time the class is called this will be executed by granting the dealer 2 cards

        self.deck_of_cards = deck_of_cards
        self.cards = self.deck_of_cards.list_of_cards
        self.crupier_current_hand = []
        self.crupier_iterator = 0
        self.crupiers_two_cards()

    def mutation_of_as(self, index, put_list, addition): #This method changes the value of the As

        mutation = put_list [index].value = 1
        addition += mutation
        addition -= 1

    def set_mutation_of_as(self, index, enter_list, sum_value): #This method calls the mutation of the As if the value of the cards in total does not exceed 10 points

        for index in range(len(enter_list)):

            if enter_list[index].value == 11:
                if sum_value >= 11:
                    self.mutation_of_as(index, enter_list, sum_value)

    def get_two_cards(self):

        two_cards = []
        for card in range(2):
            two_cards.append(self.cards.pop())

        return two_cards

    def get_card_for_crupier(self, index): #this method takes care of passing a card to the dealer by passing the value of the card to a variable

        self.crupier_current_hand.append(self.deck_of_cards.list_of_cards.pop())
        self.set_mutation_of_as(self.crupier_iterator, self.crupier_current_hand, self.values_cards_crupier)
        self.values_cards_crupier += self.crupier_current_hand[index].value

    def crupiers_two_cards(self): #it takes two cards for dealer just calling the method that takes one card twice

        for self.crupier_iterator in range(0, 2):
            self.get_card_for_crupier(self.crupier_iterator)

    def Keep_holding_cards(self):#This method continues taking dealer cards until reaching 16 points or going over

        self.set_mutation_of_as(self.crupier_iterator, self.crupier_current_hand, self.values_cards_crupier)
        while self.values_cards_crupier <= 16:
    
            self.crupier_iterator += 1
            self.get_card_for_crupier(self.crupier_iterator)

