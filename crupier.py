from deck_of_cards import Deck_of_cards

import os

#This class is responsible for managing the dealer process in the game.
class Crupier():

    Player_curret_hand = [[]]
    values_cards_crupier = 0
    cards_cemetery = []

    def __init__(self): #Each time the class is called this will be executed by granting the dealer 2 cards
        self.cards = Deck_of_cards()
        self.crupier_curret_hand = []
        self.crupier_iterator = 0
        self.crupiers_two_cards()
        self.set_mutation_of_as(self.crupier_iterator, self.crupier_curret_hand, self.values_cards_crupier)
        
    def mutation_of_as(self, index, put_list, addition): #This method changes the value of the As
    
        mutation = self.cards.value_and_cards[ put_list [index]] = 1
        addition += mutation
        addition -= 1

    def set_mutation_of_as(self, index, enter_list, sum_value): #This method calls the mutation of the As if the value of the cards in total does not exceed 10 points
        
        for index in range(len(enter_list)):

            if self.cards.value_and_cards[enter_list[index]] == 11:
                if sum_value > 10 :
                    self.mutation_of_as(index, enter_list, sum_value)
    
    def get_card(self, set_list): #this method takes care of taking a card and returning it with its value
        
        count = 0
        set_list.append(self.cards.list_of_cards.pop())
        
        for index in range(len(set_list)):

            self.set_mutation_of_as(index, set_list, count)
            count  += self.cards.value_and_cards[set_list[index]]
        return count

    def get_two_cards(self):# this method takes two cards to give to the player

        value = 0

        for iterator in range(0,2):

            self.get_card(self.Player_curret_hand[0])
            value += self.cards.value_and_cards[self.Player_curret_hand[0][iterator]]
        self.Player_curret_hand.append(value)

    def get_card_for_crupier(self, index): #this method takes care of passing a card to the dealer by passing the value of the card to a variable

        self.crupier_curret_hand.append(self.cards.list_of_cards.pop())
        self.set_mutation_of_as(self.crupier_iterator, self.crupier_curret_hand, self.values_cards_crupier )
        self.values_cards_crupier +=  self.cards.value_and_cards[self.crupier_curret_hand[index]]
        
    def crupiers_two_cards(self): #it takes two cards for dealer just calling the method that takes one card twice

        for self.crupier_iterator in range(0, 2):
            self.get_card_for_crupier(self.crupier_iterator)
    
    def Keep_holding_cards(self):#This method continues taking dealer cards until reaching 16 points or going over

        while self.values_cards_crupier <= 16:
            
            self.crupier_iterator += 1
            self.get_card_for_crupier(self.crupier_iterator)

