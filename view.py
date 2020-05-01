import os
import keyboard
import time

class View:
    def __init__(self):
        super(View, self).__init__()
        self.opcion = ["|1) Stand                    |","|2) Ask for cards            |" ,"|3) double the bet           |"]

    def table(self, current_player, cupier,point_crup):#This function is in charge of regulating the spaces and displaying the table

        self.spoint = ""
        self.schips = str(current_player.chips)
        self.curret_cards = ""     
        self.current_bet = str(current_player.bet) 

        if len(str(current_player.point)) < 2:
            self.spoint += " "   

        for i in current_player.cards:
            self.curret_cards += str(i) + " "

        self.crupier_info = str(cupier)+" Point: "+str(point_crup)

        for space in range(87):

            if len(self.schips) < 21:
                self.schips += " "

            if len(self.schips) > 21:
                self.schips = self.schips[0:21]

            if len(current_player.name) <= 25:
                current_player.name += " "

            if len(current_player.name)> 25:
                current_player.name = current_player.name[0:26]

            if len(self.curret_cards)<= 18:
                self.curret_cards += " "

            if len(self.crupier_info) < 51:
                self.crupier_info += " "

            if len(self.crupier_info)>51:
                self.crupier_info = self.crupier_info[0:52]

            if len(self.current_bet) < 19:
                self.current_bet += " "

            if len(self.current_bet) > 19:
                self.current_bet = self.current_bet[0:19]

        self.icon_table = print("""
              ________________________________________________________________________________________ __________________________
              |      |   ________                                                  ________  |       |                            | 
              |      |  |        |          _________________________             |        | |       |"""+current_player.icon+""" """  +current_player.name+"""|  
              |      |  |________|         |        """+"Crupier"+"""          |            |________| |       |     """+"***Menu Game***"+"""        |
              |       \                    |                         |                      /        """+self.opcion[0]+"""       
              |        \                   |_________________________|                     /         """+self.opcion[1]+"""      
              |         \_________________________________________________________________/          """+self.opcion[2]+"""                    
              |                                 """,self.crupier_info,"""|                            |
              |                                                                                      |"""+"Point: ",current_player.point,self.spoint,"""                |    
              |                                                                                      |"""+"Chips: "+self.schips+"""|   
              |                   ____  _            _       _            _                          |"""+"Cards: ",self.curret_cards,"""|   
              |                  | __ )| | __ _  ___| | __  | | __ _  ___| | __                      |"""+"Bet:   ",self.current_bet,"""|   
              |                  |  _ \| |/ _` |/ __| |/ _  | |/ _` |/ __| |/ /                      |___________________________ |   
              |                  | |_) | | (_| | (__|   | |_| | (_| | (__|   <                       |  
              |                  |____/|_|\__,_|\___|_|\_\___/ \__,_|\___|_|\_\                      |  
              |                                                                                      |
              |                                                                                      |
              |______________________________________________________________________________________|

    
                                                                                                        """)
    def icon(self):
        os.system("cls")
        self.icon_game_over = print("""

                      _______      ___      .___  ___.  _______      ______   ____    ____  _______ .______         
                     /  _____|    /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \        
                    |  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |       
                    |  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /        
                    |  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____ |  |\  \----.   
                    \ ______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____| 
                                                                
                                                                """+ "\n")
 
