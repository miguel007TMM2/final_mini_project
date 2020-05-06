class Player:

    def __init__(self,name = None,icon = None,state =  None,chips =  None,cards =  None,point =  None, bet =  None ,bet_state =  None):
        self.name = name

        self.icon = icon

        self.state = state

        self.chips = chips

        self.point = point

        self.cards = cards
        
        self.bet = bet
        
        self.bet_state = bet_state


    def calculate_player_point(self):

        point = 0
        for value_card in self.cards:
            point +=  value_card.value

        return point 

    def reset_data(self):

        if self.state == True:

            self.cards = ''
            self.point = ""
            self.bet = 0
            self.bet_state = False
            self.cards = []
            self.point = 0
        
        

    
