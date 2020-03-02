import os
from crupier import Crupier
from deck_of_cards import Deck_of_cards
#This class charge of generating the players
class Creator_of_Player(Crupier,Deck_of_cards):
    def __init__(self):
        super(Creator_of_Player, self).__init__()
        self.players = {}
        self.values_of_cards_players = []
        self.icono_for_player = ['☠', '☢', '☣' ,'♞','☯']
        self.indexC = 0
        self.value_As = ['A♥', 'A♠', 'A♣', 'A♦']
        self.generate_players()
        self.point_of_cards()
#This function is responsible for creating the players' keys and assigning them, a name, their initial letters and some cards
    def generate_players(self):
        print("The limit of players that you can play at the same time are 4 ")
        try:
            self.limit_players = int(input("Entry number of players ➤ ")) 
            if self.limit_players <= 4:
                os.system("clear")
                for self.delimiter in range(self.limit_players):
                    self.Get_two_cards_for_player()
                    self.name_of_players(self.delimiter)
                    if len(self.name_of_player) <= 8:
                        self.Player_curret_hand.append(self.name_of_player)                         
                        print("select you icon ")
                        for icons in self.icono_for_player: 
                            print(icons)
                        self.select_icon = int(input("insert a number in order of appearance of its icon ➤ "))
                        self.Player_curret_hand.append(self.icono_for_player[self.select_icon-1])
                        self.players.update({'player'+str(self.delimiter+1): self.Player_curret_hand})
                        self.Player_curret_hand = [[]]
                        os.system("clear")
                    else:
                        print("The player name can only contain a maximum of 8 characters")
                        self.name_of_players(self.delimiter)
                        
            else:
                os.system("clear")
                input("Error entering the number of players, try a number from 1 to 4 enter to continue... ")
                self.generate_players()
        except ValueError:
            os.system("clear")
            input("Error entering the number of players, try a number from 1 to 4 enter to continue... ")
            self.generate_players()


    def name_of_players(self,delimiter):
        self.name_of_player = input("Entry name of player"+str(delimiter+1)+" ➤ ")
        
    def point_of_cards(self):
       for keys_player in self.players:  
           for read_cards in self.players[keys_player][0]:
                self.indexC += self.dic_value_of_the_cards[read_cards]
           self.values_of_cards_players.append(self.indexC)
           self.indexC = 0
       self.indexC = 0   



p = Creator_of_Player()

        