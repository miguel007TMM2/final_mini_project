from deck_of_cards import Deck_of_cards
import os
from crupier import Crupier
lis_cards = Deck_of_cards()
#This class charge of generating the players
class Player(Crupier,Deck_of_cards):
    def __init__(self):
        super(Player, self).__init__()
        self.players = {}
        self.icono_for_player = ['☠', '☢', '☣' ,'♞','☯', '♪', '❆','✟']
        self.indexC = 0
        self.calls_points = 0
    
    
    def ask_for_letters(self, delimiter):
        self.player_card(self.players['player'+str(delimiter+1)]['cards'])
