from deck_of_cards import Deck_of_cards
cards = Deck_of_cards()
from dice import Dice
dice = Dice()
import os

#This class is responsible for managing the dealer process in the game.
class Crupier():

    crupier_cards_value = 0
    card_of_crupier = 0
    cards_as = ['A♥', 'A♠', 'A♣', 'A♦']
    bets = []

    def __init__(self):
        super(Crupier, self).__init__()
        self.croupier_hand = []
        self.Player_curret_hand = []

    def bet(self):
        dice.status()
        point = str(dice.index) + '00'
        try:
            ask_initial_bet = input('Your initial bet must be equal to or greater than ' +point+ ' point.' + 'Enter your initial bet : ')    
            if int(ask_initial_bet) != int(point):
                os.system("clear")

                ask_to_continue = input('Your initial bet is below what is required, enter to continue or exit to let play : ')
                if ask_to_continue.strip() == '':
                    os.system("clear")
                    self.bet()

                elif ask_to_continue != '':
                    ask_to_continue

                elif ask_to_continue.strip() == 'exit':
                    pass
            
            elif ask_initial_bet:
                self.bets.append(ask_initial_bet)
                return self.bets
                
        except ValueError:
            print('error to enter de bet. the characters you entered are incorrect')
            self.bet()

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

    def mutation_of_as(self, index):

        mutation = cards.value_and_cards[self.croupier_hand[index]] = 11
        self.crupier_cards_value += mutation
        self.crupier_cards_value -= 1

    def set_mutation_of_as(self):

        for list_card_of_crupier in range(len(self.croupier_hand)):
            if self.croupier_hand[list_card_of_crupier]  in self.cards_as:
                if self.crupier_cards_value <= 11:
                    self.mutation_of_as(list_card_of_crupier)
    
    def Keep_holding_cards(self):

        if self.crupier_cards_value < 16:
            self.set_mutation_of_as()

            while self.crupier_cards_value < 16:
                self.card_of_crupier += 1
                self.crupier_card(self.croupier_hand, self.card_of_crupier)

