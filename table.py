
# from players import Player
# from game import *
# class view(Player):
#     def __init__(self):
#         super(view, self).__init__()

from players import Creator_of_Player
class view(Creator_of_Player):
    def __init__(self):
        super(view, self).__init__()


    def table(self):
        print("      _______________________________________________________________________________________  ")
        print("      |      |   ________                                                  ________  |      |  ")
        print("      |      |  |        |          _________________________             |        | |      |  ")
        print("      |      |  |________|         |                         |            |________| |      |  ")  
        print("      |      |                     |                         |                       |      |  ")  
        print("      |       \                    |                         |                      /       |  ")  
        print("      |        \                   |_________________________|                     /        |  ")  
        print("      |         \_________________________________________________________________/         |  ")  
        print("      |                                                                                     |  ")
        print("      |                                                                                     |  ")
        print("      |                                                                                     |  ")
        print("      |                                                                                     |  ")
        print("      |                   ____  _            _       _            _                         |  ")
        print("      |                  | __ )| | __ _  ___| | __  | | __ _  ___| | __                     |  ")
        print("      |                  |  _ \| |/ _` |/ __| |/ _  | |/ _` |/ __| |/ /                     |  ")
        print("      |                  | |_) | | (_| | (__|   | |_| | (_| | (__|   <                      |  ")
        print("      |                  |____/|_|\__,_|\___|_|\_\___/ \__,_|\___|_|\_\                     |  ")
        print("      |                                                                                     |  ")  
        print("      |     "+str(self.players['player1'][0])+"                                                                    |  ")
        print("      |       |¯¯¯¯¯¯|                                                    |¯¯¯¯¯¯|          |  ")                      
        print("      |       |      |             "+str(self.players['player2'][0])+"        ______             |      |          |  ")
        print("      |       |      |             |¯¯¯¯¯¯|           |      |            |      |          |  ")
        print("      |       |      |             |      |           |      |            |      |          |  ")
        print("      |        ¯¯¯¯¯¯              |      |           |      |             ¯¯¯¯¯¯           |  ")  
        print("      \        "+str(self.players['player1'][1]+self.players['player1'][2])+"               |______|           |______|                              /   ")
        print("       \                            "+str(self.players['player2'][1]+self.players['player2'][2])+"                                                        /    ")
        print("        \                                                                                 /     ")
        print("         \ ______________________________________________________________________________/      ")
        print("           ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯       ")
                


vista = view()
vista.table()
    
# from players import Player
# from game import *
# class view(Player):
#     def __init__(self):
#         super(view, self).__init__()


#     def table(self, delimiter):
#         print("      _______________________________________________________________________________________  ")
#         print("      |      |   ________                                                  ________  |      |  ")
#         print("      |      |  |        |          _________________________             |        | |      |  ")
#         print("      |      |  |________|         |                         |            |________| |      |  ")  
#         print("      |      |                     |                         |                       |      |  ")  
#         print("      |       \                    |                         |                      /       |  ")  
#         print("      |        \                   |_________________________|                     /        |  ")  
#         print("      |         \_________________________________________________________________/         |  ")  
#         print("      |                                                                                     |  ")
#         print("      |                                                                                     |  ")
#         print("      |                                                                                     |  ")
#         print("      |                                                                                     |  ")
#         print("      |                   ____  _            _       _            _                         |  ")
#         print("      |                  | __ )| | __ _  ___| | __  | | __ _  ___| | __                     |  ")
#         print("      |                  |  _ \| |/ _` |/ __| |/ _  | |/ _` |/ __| |/ /                     |  ")
#         print("      |                  | |_) | | (_| | (__|   | |_| | (_| | (__|   <                      |  ")
#         print("      |                  |____/|_|\__,_|\___|_|\_\___/ \__,_|\___|_|\_\                     |  ")
#         print("      |                                                                                     |  ")
#         print("      |    

