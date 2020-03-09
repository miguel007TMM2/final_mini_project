from players import *
from crupier import Crupier
from deck_of_cards import Deck_of_cards
import os
crup = Crupier()
po = Player()
cards = Deck_of_cards()
#This function is responsible for creating the players' keys and assigning them, a name, their initial letters and some cards
def generate_players():

    print("The limit of players that you can play at the same time are 4 ")
    limit_players = input("Entry number of players ➤ ") 
    if limit_players.isdigit():
        
        if int(limit_players) <= 4:
            os.system("clear")
            
            for delimiter in range(int(limit_players)):
                crup.two_cards()
                name_of_player = input("Entry name of player"+str(delimiter+1)+" ➤ ")
                os.system("clear")
                print("Select you icon")

                number_icon = 1
                for icons in po.icono_for_player:
                    print(number_icon,icons)
                    number_icon += 1
                select_icon = int(input("insert a number of you icon ➤ "))
                os.system("clear")

                po.players.update({
                    'player'+str(delimiter+1):{ 
                    'name':  name_of_player,
                    'icon':  po.icono_for_player[select_icon-1],
                    'State': True,
                    'cards': crup.Player_curret_hand}})

                crup.Player_curret_hand  = []

        else:
            os.system("clear")
            input("Error entering the number of players, try a number from 1 to 4 enter to continue... ")
            generate_players()

    else:
        os.system("clear")
        print("Error entering the number of players, try a number from 1 to 4 enter to continue...") 
        generate_players()

def system_of_turns():
    
    delimiter = 0
    po.point_of_cards()
    
    while delimiter < (len(po.players)):
        print(po.players['player'+str(delimiter+1)]['cards'],po.values_of_cards_players[delimiter])
        moviment = input("1) stand  2) ask for letters: ➤ ")

        if moviment.isdigit():

            if int(moviment) <= 2:

                if int(moviment) == 1:
                    pass
                    delimiter += 1

                if po.values_of_cards_players[delimiter] < 21:
                    if int(moviment) == 2:
                        print(po.players['player'+str(delimiter+1)]['cards'],po.values_of_cards_players[delimiter])
                        po.ask_for_letters(delimiter)
                        po.values_of_cards_players[delimiter] += cards.value_and_cards[po.players['player'+str(delimiter+1)]['cards'][len(po.players['player'+str(delimiter+1)]['cards'])-1]]
                        
                else:
                    os.system("clear")
                    print("You have to stand, your cards have exceeded or is equal to the score of 21")
                    pass

            else:
                print("error when inserting movement test with 1 or 2")

generate_players()
system_of_turns()