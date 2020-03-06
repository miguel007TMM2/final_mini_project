import os
from crupier import Crupier
from deck_of_cards import Deck_of_cards

lis_cards = Deck_of_cards()
#This class charge of generating the players
class Player(Crupier,Deck_of_cards):
    def __init__(self):
        super(Player, self).__init__()
        self.players = {}
        self.values_of_cards_players = []
        self.icono_for_player = ['☠', '☢', '☣' ,'♞','☯']
        self.indexC = 0
        self.value_As = ['A♥', 'A♠', 'A♣', 'A♦']
    
    
    def ask_for_letters(self, delimiter):
        self.player_card(self.players['player'+str(delimiter+1)]['cards'])


    def point_of_cards(self):
        for keys_player in self.players:  
            for read_cards in self.players[keys_player]['cards']:
                self.indexC += self.value_and_cards[read_cards]
            
            self.values_of_cards_players.append(self.indexC)
            
            self.indexC = 0
        self.indexC = 0   
