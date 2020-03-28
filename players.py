
#This class charge of generating the players
class Player():

    attributes = {}
    icono_for_player = ['☠', '☢', '☣' ,'♞','☯', '♪', '❆','✟']
    indexC = 0
    calls_points = 0

    def __init__(self):

        for rename in range(1,6):

            self.attributes.update({

            'player'+str(rename):{ 

            'name':  "",
            
            'icon':  "",

            'state': False,
            
            'chip':  "",
            
            'point': "",
            
            'cards':  "",
            
            'initial_bet' : [False, ""], 
            
            'bet': [False,""] 
                                    }})

      
    
    
