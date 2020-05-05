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


    def calculate_player_point(self, iterator, player):

        point = 0
        for value_card in player[iterator].cards:
            point +=  value_card.value

        return point 

    def reset_player_data(self, iterator, player, two_cards):

        if player[iterator].state == True:

            player[iterator].cards = ''
            player[iterator].point = ""
            player[iterator].bet = 0
            player[iterator].bet_state = False
            player[iterator].cards = two_cards
            player[iterator].point = self.calculate_player_point(iterator, player)
        
        

    
