
#This class has the dealer's tokens and is responsible for generating those of the players
class Chips_container():

    def __init__(self):
        self.color = True
        self.chips_and_values = {'⓵': 100, '⓹' : 500,  '⓾': 1000} #figures and values of blackjack tokens
        self.chips_of_crupier = {'⓵': 200, '⓹' : 200, '⓾': 200}#amount of chips the dealer has
        self.players_chips = {}

    #this function is responsible for generating the players' tokens
    def generate_chips_for_players(self):
        get_keys_chips = list(self.chips_values.keys())
        for get_key_chip in range(len(get_keys_chips)):
            self.players_chips.update({get_keys_chips_of_crupier[get_key_chip_of_crupie] : 10})    

    #this function will be called in case the dealer no longer has any more chips
    def resupply_crupier(self):
        get_keys_chips_of_crupier = list(self.chips_of_crupier.keys())
        for get_key_chip_of_crupier in range(len(get_keys_chips_of_crupier)):
            if self.chips_of_crupier[get_keys_chips_of_crupier[get_key_chip_of_crupier]] <= 20:
                self.chips_of_crupier[get_keys_chips_of_crupier[get_key_chip_of_crupier]] = 200
        
    
