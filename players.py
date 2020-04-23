
#This class charge of generating the players
class Player():
    attributes = {}
    icono_for_player = ['☠', '☢', '☣' ,'♞','☯', '♪', '❆','✟']


    for rename in range(1,6):

        attributes.update({

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

      
    
    
