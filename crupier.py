from deck_of_cards import Deck_of_cards
cards = Deck_of_cards()

#This class is responsible for managing the dealer process in the game.
class Crupier():

    crupier_cards_value = 0
    card_of_crupier = 0
    cards_as = ['A♥', 'A♠', 'A♣', 'A♦']

    def __init__(self):
        super(Crupier, self).__init__()
        self.croupier hand = []
        self.Player_curret_hand = [[]]

    def player_card(self, list_for_put_cards):
        
        list_for_put_cards.append(cards.list_of_cards.pop())

    def crupier_card(self, list_for_put_cards, index):

        list_for_put_cards.append(cards.list_of_cards.pop())
        
        if list_for_put_cards == self.croupier hand:
            self.crupier_cards_value +=  cards.value_and_cards[list_for_put_cards[index]]

    def two_cards(self):

        for index_for_player in range(0,2):
            self.player_card(self.Player_curret_hand[0])
    
    def crupiers_two_cards(self):

        for self.card_of_crupier in range(0, 2):
            self.crupier_card(self.croupier hand, self.card_of_crupier)

    def mutation_of_as(self, index):

        mutation = cards.value_and_cards[self.croupier hand[index]] = 11
        self.crupier_cards_value += mutation
        self.crupier_cards_value -= 1

    def set_mutation_of_as(self):

        for list_card_of_crupier in range(len(self.croupier hand)):
            if self.croupier hand[list_card_of_crupier]  in self.cards_as:
                if self.crupier_cards_value <= 11:
                    self.mutation_of_as(list_card_of_crupier)
    
    def Keep_holding_cards(self):

        if self.crupier_cards_value < 16:
            self.set_mutation_of_as()

            while self.crupier_cards_value < 16:
                self.card_of_crupier += 1
                self.crupier_card(self.croupier hand, self.card_of_crupier)
