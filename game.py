from players import *
from crupier import Crupier
import os
crup = Crupier()
po = Player()
#This function is responsible for creating the players' keys and assigning them, a name, their initial letters and some cards
def generate_players():
    print("The limit of players that you can play at the same time are 4 ")
    limit_players = input("Entry number of players ➤ ") 
    if limit_players.isdigit():
        if int(limit_players) <= 4:
            os.system("clear")
            
            for delimiter in range(int(limit_players)):
                crup.Get_two_cards_for_player()
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
    while delimiter < (len(po.players)):
        moviment = input("1) stand  2) ask for letters: ➤ ")
        if moviment.isdigit():
            if int(moviment) <= 2:
                if int(moviment) == 1:
                    pass
                if int(moviment) == 2:
                    po.ask_for_letters(delimiter)
            else:
                print("mamaguebo noo")

p = generate_players()

system_of_turns()