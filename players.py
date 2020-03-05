import os
from crupier import Crupier
from deck_of_cards import Deck_of_cards

lis_cards = Deck_of_cards()
#This class charge of generating the players
class Player(Crupier,Deck_of_cards):
    def __init__(self):
        self.players = {}
        self.values_of_cards_players = []
        self.icono_for_player = ['☠', '☢', '☣' ,'♞','☯']
        self.indexC = 0
        self.value_As = ['A♥', 'A♠', 'A♣', 'A♦']
    
    
    def ask_for_letters(self, delimiter):
        self.players['player'+str(delimiter+1)]['cards'].append(lis_cards.new_list_of_cards[0])
        lis_cards.new_list_of_cards.pop(0)


    def point_of_cards():
        for keys_player in players:  
            for read_cards in players[keys_player]['cards']:
                indexC += dic_value_of_the_cards[read_cards]
                values_of_cards_players.append(indexC)
            indexC = 0
        indexC = 0   
