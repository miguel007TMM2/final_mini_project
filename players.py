import os
from deck_of_cards import Deck_of_cards 
#This class charge of generating the players
class Creator_of_Player(Deck_of_cards):
    def __init__(self):
        super(Creator_of_Player, self).__init__()
        self.players = {}
        self.values_of_cards_players = []
        self.icono_for_player = ['☠', '☢', '☣' ,'♞','☯']
        self.indexC = 0

    
#This function is responsible for creating the players' keys and assigning them, a name, their initial letters and some cards
    def generate_players(self):
        print("The limit of players that you can play at the same time are 4 ")
        try:
            self.limit_players = int(input("Entry number of players ➤ ")) 
            if self.limit_players <= 4:
                os.system("clear")
                for self.delimiter in range(self.limit_players):
                    self.name_of_player = input("Entry name of player"+str(self.delimiter+1)+" ➤ ")
                    os.system("clear")
            else:
                os.system("clear")
                input("Error entering the number of players, try a number from 1 to 4 enter to continue... ")
                self.generate_players()
        except ValueError:
            os.system("clear")
            input("Error entering the number of players, try a number from 1 to 4 enter to continue... ")
            self.generate_players()

    def point_of_cards(self):
       for keys_player in self.players:  
           for read_cards in self.players[keys_player][0]:
                self.indexC += generartor.dic_value_of_the_cards[read_cards]
           self.Valors_players.append(self.indexC)
           self.indexC = 0
       self.indexC = 0   


test = Creator_of_Player()




        