import os
import keyboard
import time
from players import Player
player = Player()

class View():
    def __init__(self):
        super(View, self).__init__()
        
        self.opcion = ["|1) Stand                    |","|2) Ask for letters          |","|3) Backing out              |","|4) double the bet           |"]
        
    def table(self, player, current_player, cupier,point_crup):
        self.spoint = ""
        self.schips = ""
        self.current_bet = str(current_player['bet'][1])

        if len(str(current_player['chip'])) < 5:
            self.schips += " "
        
        if len(str(current_player['point'])) < 2:
            self.spoint += " "    
            
        self.curret_cards = " ".join(current_player['cards'])
        
        self.crupier_info = str(cupier)+" Point: "+str(point_crup)
        self.player1y2 =player['player1']['icon']+"  "+" ".join(player['player1']['cards'])+" "+str(player['player1']['point'])+"                       "+player['player2']['icon']+" "+" ".join(player['player2']['cards'])+" "+str(player['player2']['point'])
        self.player3y4 =player['player3']['icon']+"  "+" ".join(player['player3']['cards'])+" "+str(player['player3']['point'])+"                       "+player['player4']['icon']+" "+" ".join(player['player4']['cards'])+" "+str(player['player4']['point']) 
        
        for space in range(87):
            
            if len(self.player1y2) < 75:
                self.player1y2 += " "

            elif len(self.player1y2) > 75:
                self.player1y2 = self.player1y2[0:75]

            if len(self.player3y4) < 75:
                self.player3y4 += " "

            if len(self.player3y4) > 75:
                self.player3y4 = self.player3y4[0:75]
            
            if len(current_player['name']) <= 25:
                current_player['name'] += " "

            if len(current_player['name'])> 25:
                current_player['name'] = current_player['name'][0:26]
            
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
              |      |  |        |          _________________________             |        | |       |"""+current_player['icon']+""" """  +current_player['name']+"""|  
              |      |  |________|         |        """+"Crupier"+"""          |            |________| |       |     """+"***Menu Game***"+"""        |
              |       \                    |                         |                      /        """+self.opcion[0]+"""       
              |        \                   |_________________________|                     /         """+self.opcion[1]+"""      
              |         \_________________________________________________________________/          """+self.opcion[2]+"""         
              |                                                                                      """+self.opcion[3]+"""           
              |                                 """,self.crupier_info,"""|                            |
              |                                                                                      |"""+"Point: ",current_player['point'],self.spoint,"""                |    
              |                                                                                      |"""+"Chips: ",current_player['chip'],self.schips,"""             |   
              |                   ____  _            _       _            _                          |"""+"Cards: ",self.curret_cards,"""|   
              |                  | __ )| | __ _  ___| | __  | | __ _  ___| | __                      |"""+"Bet:   ",self.current_bet,"""|   
              |                  |  _ \| |/ _` |/ __| |/ _  | |/ _` |/ __| |/ /                      |___________________________ |   
              |                  | |_) | | (_| | (__|   | |_| | (_| | (__|   <                       |  
              |                  |____/|_|\__,_|\___|_|\_\___/ \__,_|\___|_|\_\                      |  
              |                                                                                      |
              |                                                                                      |
              |                                                                                      |
              |           """+self.player1y2+"""|                           
              |               """+player['player1']['name'][0:10]+"""                       """+player['player2']['name'][0:10]+"""                  
              |                                                                                      | 
              |           """+self.player3y4+"""|                                               
              |               """+player['player3']['name'][0:10]+"""                            """+player['player4']['name'][0:10]+"""                                                                               
              |                                                                                      |
 
    
                                                                                                        """)

    def icon(self):
        os.system("clear")
        self.icon_game_over = print("""

                      _______      ___      .___  ___.  _______      ______   ____    ____  _______ .______         
                     /  _____|    /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \        
                    |  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |       
                    |  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /        
                    |  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____ |  |\  \----.   
                    \ ______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____| 
                                                                
                                                                """+ "\n")
       
    


