import os
from crupier import Crupier
from deck_of_cards import Deck_of_cards
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


    def point_of_cards_asing(self, delimiter):
        if self.calls_points == 0:  
                self.players['player'+str(delimiter+1)] 
                for read_cards in self.players['player'+str(delimiter+1)]['cards']:
                    if self.value_and_cards[read_cards] == 1:
                        print(self.players['player'+str(delimiter+1)]['cards'])
                        self.select_valor = input("Select valor of as 1) 1 point 2) 11 point ➤ ")

                        if self.select_valor.isdigit():
                            if int(self.select_valor) <=2 and int(self.select_valor) >0:
                                if int(self.select_valor) == 1:
                                    
                                    self.value_and_cards[read_cards] = 1
                                    self.indexC += self.value_and_cards[read_cards]

                                if int(self.select_valor) == 2:
                                    self.value_and_cards[read_cards] = 11
                                    self.indexC += self.value_and_cards[read_cards]
                            else:
                                print("Error you have inserted an invalid option try 1 or 2")
                                self.point_of_cards(delimiter)
                        else:
                            print("Error you have inserted an invalid option")
                            self.point_of_cards(delimiter)
                    else:
                        self.indexC += self.value_and_cards[read_cards]
                            
                self.players['player'+str(delimiter+1)]['point'] += self.indexC
                self.indexC = 0
               
                
                self.indexC = 0
               
    def point_of_cards(self, delimiter):
                for read_cards in self.players['player'+str(delimiter+1)]['cards']:
                    if self.value_and_cards[read_cards] == 1:
                        print(self.players['player'+str(delimiter+1)]['cards'])
                        self.select_valor = input("Select valor of as 1) 1 point 2) 11 point ➤ ")
                        if self.select_valor.isdigit():
                            if int(self.select_valor) <=2 and int(self.select_valor) >0:
                                if int(self.select_valor) == 1:
                                    self.value_and_cards[read_cards] = 1
                                    print(self.value_and_cards[read_cards])
                                    self.players['player'+str(delimiter+1)]['point'] += self.value_and_cards[read_cards] -1

                                elif int(self.select_valor) == 2:
                                    self.value_and_cards[read_cards] = 11
                                    print(self.value_and_cards[read_cards])
                                    self.players['player'+str(delimiter+1)]['point'] += self.value_and_cards[read_cards] -1

                                else:
                                    print("Error you have inserted an invalid option try 1 or 2")
                                    self.point_of_cards(delimiter)
                            else:
                                print(" Error you have inserted an invalid option")
                                self.point_of_cards(delimiter)
                   
                self.players['player'+str(delimiter+1)]['point'] += lis_cards.value_and_cards[self.players['player'+str(delimiter+1)]['cards'][len(self.players['player'+str(delimiter+1)]['cards'])-1]]
