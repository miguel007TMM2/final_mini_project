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
        self.calls_points = 0
    
    
    def ask_for_letters(self, delimiter):
        self.player_card(self.players['player'+str(delimiter+1)]['cards'])


    def point_of_cards(self):
        if self.calls_points == 0:  
            for keys_player in self.players:  
                for read_cards in self.players[keys_player]['cards']:
                    if self.value_and_cards[read_cards] == 1:
                        
                        self.select_valor = input("select valor of as 1) 1 point 2) 11 point ➤ ")

                        if self.select_valor.isdigit():
                            if int(self.select_valor) <=2 and int(self.select_valor) >0:
                                if int(self.select_valor) == 1:
                                    
                                    self.value_and_cards[read_cards] = 1
                                    self.indexC += self.value_and_cards[read_cards]

                                if int(self.select_valor) == 2:
                                    self.value_and_cards[read_cards] = 11
                                    self.indexC += self.value_and_cards[read_cards]
                            else:
                                print("error you have inserted an invalid option try 1 or 2")
                                self.point_of_cards()
                        else:
                            print("error you have inserted an invalid option")
                            self.point_of_cards()
                    else:
                        self.indexC += self.value_and_cards[read_cards]
                
                self.values_of_cards_players.append(self.indexC)
                
                self.indexC = 0
            self.indexC = 0   
            self.calls_points += 1
        # else:
        #     self.values_of_cards_players[delimiter] += card.value_and_cards[self.players['player'+str(delimiter+1)]['cards'][len(self.players['player'+str(delimiter+1)]['cards'])-1]]
