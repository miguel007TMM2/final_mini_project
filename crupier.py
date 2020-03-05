from deck_of_cards import Deck_of_cards
cards = Deck_of_cards()

class Crupier(Deck_of_cards):

    def __init__(self):
        super(Crupier, self).__init__()
        self.chips = {'⓵': 100 , '⓹' : 500 , '⓾': 1000}
        self.crupiers_chips = []
        self.list_cards_of_crupier = []
        self.Player_curret_hand = []
        self.generate_chips()

    def generate_chips(self):
        get_keys_of_chips = list(self.chips.keys())
        for get_key_of_chip in get_keys_of_chips:
            for multiplicator_chips in range(len(get_keys_of_chips)):
                self.crupiers_chips.append(get_keys_of_chips[multiplicator_chips])
                self.crupiers_chips.append(get_keys_of_chips[multiplicator_chips])

    def get_card(self, list_for_put_cards):
        list_for_put_cards.append(self.new_list_of_cards.pop())

    def Get_two_cards_for_player(self):
        for index_for_player in range(0,2):
            self.get_card(self.Player_curret_hand)

    