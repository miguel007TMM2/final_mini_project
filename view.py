import os
import keyboard
import time
from players import Player
inf_player = Player()
class View():
    def __init__(self):
        self.iterator = 0
        self.opcion = ["|1) Stand                    |","|2) Ask for letters          |","|3) Backing out              |"]
            
    def table(self):
        
        self.icon_table = print("""
              _______________________________________________________________________________________ __________________________
              |      |   ________                                                  ________  |      |                            | 
              |      |  |        |          _________________________             |        | |      |                            |  
              |      |  |________|         |                         |            |________| |      |    """+inf_player.players['player1']['name']+"""             |
              |       \                    |                         |                      /       """+self.opcion[0]+"""       
              |        \                   |_________________________|                     /        """+self.opcion[1]+"""      
              |         \_________________________________________________________________/         """+self.opcion[2]+"""       
              |                                                                                     |                            |   
              |                                                                                     |                            |   
              |                                                                                     |                            |   
              |                                                                                     |                            |   
              |                   ____  _            _       _            _                         |                            |   
              |                  | __ )| | __ _  ___| | __  | | __ _  ___| | __                     |                            |   
              |                  |  _ \| |/ _` |/ __| |/ _  | |/ _` |/ __| |/ /                     |___________________________ |   
              |                  | |_) | | (_| | (__|   | |_| | (_| | (__|   <                      |  
              |                  |____/|_|\__,_|\___|_|\_\___/ \__,_|\___|_|\_\                     |  
              |                                                                                     |
              |                                                                                     |
              |                                                                                     |
              |                """+inf_player.players['player1']['cards']+"""                                                                    |
              |                                                                                     |
              |                                                                                     |
              |                                                                                     |

        
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
    
    
    def moveUP(self):
        time.sleep(0.15)
        
        if self.iterator == 0:
            self.opcion[2] = "|3) Backing out              |"
            self.opcion[1] = "|2) Ask for letters          |" 
            self.opcion[0] = "|1) Stand  ◄                 |"
            os.system("clear")
            self.table()
           
        elif self.iterator == 1:
            self.opcion[0] = "|1) Stand                    |"
            self.opcion[2] = "|3) Backing out              |"
            self.opcion[1] = "|2) Ask for letters ◄        |"
            os.system("clear")
            self.table()
        elif self.iterator == 2:
            self.opcion[1] = "|2) Ask for letters          |" 
            self.opcion[0] = "|1) Stand                    |"
            self.opcion[2] = "|3) Backing out  ◄           |" 
            os.system("clear")
            self.table()
        self.iterator -= 1
        if self.iterator == -1:
            self.iterator = 2
        
    def moveDown(self):
        time.sleep(0.15)
        
        if self.iterator == 0:
            self.opcion[1] = "|2) Ask for letters          |" 
            self.opcion[2] = "|3) Backing out              |" 
            self.opcion[0] = "|1) Stand  ◄                 |"
            os.system("clear")
            self.table()
            
        elif self.iterator == 1:
            self.opcion[0] = "|1) Stand                    |" 
            self.opcion[2] = "|3) Backing out              |" 
            self.opcion[1] = "|2) Ask for letters ◄        |"
            os.system("clear")
            self.table()
        elif self.iterator == 2:
            self.opcion[0] = "|1) Stand                    |" 
            self.opcion[1] = "|2) Ask for letters          |" 
            self.opcion[2] = "|3) Backing out  ◄           |" 
            os.system("clear")
            self.table()
        self.iterator += 1

        if self.iterator == 3:
            self.iterator = 0

    def executeMoveMenu(self):
        while True:
            if keyboard.is_pressed("down"):
                self.moveDown()
        
            elif keyboard.is_pressed("up"):
                self.moveUP()
    


