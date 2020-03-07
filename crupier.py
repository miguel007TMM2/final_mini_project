from deck_of_cards import Deck_of_cards
cards = Deck_of_cards()
from dice import Dice
dice = Dice()
import os

#This class is responsible for managing the dealer process in the game.
class Crupier():

    crupier_cards_value = 0
    card_of_crupier = 0
    bets = []
    dice.status()
    
    def __init__(self):
        super(Crupier, self).__init__()
        self.croupiers_hand = []
        self.Player_curret_hand = []

    # def initial_bet(self):
    #     point = str(dice.index) + '00'
    #     try:
    #         ask_initial_bet = input('Your initial initial_bet must be equal to or greater than ' +point+ ' point.' + 'Enter your initial initial_bet : ')    
    #         if int(ask_initial_bet) == int(point):
    #             self.bets.append(ask_initial_bet)
    #             print(self.bets)
    #         elif int(ask_initial_bet) !=  int(point) :
    #             print('Your initial initial_bet is below what is required')
    #             self.initial_bet()
                
    #     except ValueError:
    #         print('error to enter de initial_bet. the characters you entered are incorrect')
    #         self.initial_bet()

    def insurance(self):
        pass

    def player_card(self, list_for_put_cards):
        
        list_for_put_cards.append(cards.list_of_cards.pop())

    def crupier_card(self, list_for_put_cards, index):

        list_for_put_cards.append(cards.list_of_cards.pop())
        
        if list_for_put_cards == self.croupier_hand:
            self.crupier_cards_value +=  cards.value_and_cards[list_for_put_cards[index]]

    def two_cards(self):
        for index_for_player in range(0,2):
            self.player_card(self.Player_curret_hand) 
    
    
    def crupiers_two_cards(self):

        for self.card_of_crupier in range(0, 2):
            self.crupier_card(self.croupier_hand, self.card_of_crupier)
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
    
    def Keep_holding_cards(self):

        if self.crupier_cards_value < 16:
            self.set_mutation_of_as()

            while self.crupier_cards_value < 16:
                self.card_of_crupier += 1
                self.crupier_card(self.croupier_hand, self.card_of_crupier)
                
        return self.croupier_hand