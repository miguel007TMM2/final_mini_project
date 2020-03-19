import os
import keyboard
import time
from players import Player
player = Player()

class View():
    def __init__(self):
        super(View, self).__init__()
        self.opcion = ["|1) Stand                    |","|2) Ask for letters          |","|3) Backing out              |"]
         
    def table(self, player, names):
        self.player1y2 =player['player1']['icon']+"  "+" ".join(player['player1']['cards'])+"  "+str(player['player1']['point'])+"                             "+player['player2']['icon']+"  "+" ".join(player['player2']['cards'])+"  "+str(player['player2']['point'])
        self.player3y4 =player['player3']['icon']+"  "+" ".join(player['player3']['cards'])+"  "+str(player['player3']['point'])+"                 "+player['player4']['icon']+"  "+" ".join(player['player4']['cards'])+"  "+str(player['player4']['point'])

       

        for space in range(87):
            if len(self.player1y2) < 75:
                self.player1y2 += " "

            if len(self.player1y2) >= 75:
                self.player1y2 = self.player1y2[0:75]

            if len(self.player3y4) < 69:
                self.player3y4 += " "

            if len(self.player3y4) >= 69:
                self.player3y4 = self.player3y4[0:69]

            if len(names['name']) <= 27:
                names['name'] += " "

            if len(names['name'])> 27:
                names['name'] = names['name'][0:28]

        self.icon_table = print("""
              ________________________________________________________________________________________ __________________________
              |      |   ________                                                  ________  |       |                            | 
              |      |  |        |          _________________________             |        | |       |                            |  
              |      |  |________|         |                         |            |________| |       |"""  +names['name']+"""|
              |       \                    |                         |                      /        """+self.opcion[0]+"""       
              |        \                   |_________________________|                     /         """+self.opcion[1]+"""      
              |         \_________________________________________________________________/          """+self.opcion[2]+"""       
              |                                                                                      |                            |   
              |                                                                                      |                            |   
              |                                                                                      |                            |   
              |                                                                                      |                            |   
              |                   ____  _            _       _            _                          |                            |   
              |                  | __ )| | __ _  ___| | __  | | __ _  ___| | __                      |                            |   
              |                  |  _ \| |/ _` |/ __| |/ _  | |/ _` |/ __| |/ /                      |___________________________ |   
              |                  | |_) | | (_| | (__|   | |_| | (_| | (__|   <                       |  
              |                  |____/|_|\__,_|\___|_|\_\___/ \__,_|\___|_|\_\                      |  
              |                                                                                      |
              |                                                                                      |
              |                                                                                      |
              |           """+self.player1y2+"""|                 
              |                                                                                      | 
              |                                                                                      | 
              |                 """+self.player3y4+"""|                                               
              |                                                                                      |                    
              |                                                                                      |
 
        
                                                                                                        """)

        

    def icon(self):
        self.icon_game_over = print("""

                      _______      ___      .___  ___.  _______      ______   ____    ____  _______ .______         
                     /  _____|    /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \        
                    |  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |       
                    |  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /        
                    |  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____ |  |\  \----.   
                    \ ______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____| 
                                                                
                                                                """+ "\n")
        return self.icon
    

