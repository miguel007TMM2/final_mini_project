from players import Player
from crupier import Crupier
from deck_of_cards import Deck_of_cards
from dice import Dice
import os
crup = Crupier()
dice =  Dice()
dice.status()
import os
player = Player()
card = Deck_of_cards()

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
                
                def select():

                    number_icon = 1

                    for icons in player.icono_for_player:
                        print(number_icon,icons)
                        number_icon += 1

                    select_icon = input("insert a number of you icon ➤ ")
                    os.system("clear")

                    if select_icon.isdigit():

                        if int(select_icon) > 0 and int(select_icon) <= 5:

                            player.players.update({
                                'player'+str(delimiter+1):{ 
                                'name':  name_of_player,
                                'icon':  player.icono_for_player[int(select_icon)-1],
                                'state': True,
                                'chip': 10000,
                                'point': 0,
                                'cards': crup.Player_curret_hand}})

                            crup.Player_curret_hand  = []

                        else:
                            os.system("clear")
                            input("error the option you have inserted is not valid test with a number from 1 to 5 press enter for continue") 
                            select()
                    else:
                            input("error the option you have inserted is not valid test with a number from 1 to 5 press enter for continue") 
                            select()

                select()

        else:
            os.system("clear")
            input("Error entering the number of players, try a number from 1 to 4 enter to continue... ")
            generate_players()

    else:
        os.system("clear")
        input("Error entering the number of players, try a number from 1 to 4 enter to continue...") 
        generate_players()

#This function is responsible for selecting a winner
def Win():
   pass

def system_of_turns():
    delimiter = 0
    player.point_of_cards(delimiter)
    print(player.players['player'+str(delimiter+1)])
    while delimiter < (len(player.players)):
        if player.players['player'+str(delimiter+1)]['state'] == True:
            if player.players['player'+str(delimiter+1)]['point'] <= 21: 
                moviment = input("1) stand  2) ask for letters  3) backing out: ➤ ")

                if moviment.isdigit():
                    if int(moviment) <= 1:
                        if int(moviment) == 1:
                            os.system("clear")
                            print(player.players['player'+str(delimiter+1)])
                            if delimiter < len(player.players):
                                delimiter += 1
                                pass
                            else:
                                break

                        
                        if int(moviment) == 2:
                            if  player.players['player'+str(delimiter+1)]['point']< 21:  
                                os.system("clear")
                                player.ask_for_letters(delimiter)
                                player.point_of_cards(delimiter)
                                print(player.players['player'+str(delimiter+1)])
                            else:
                                print("is equal to the score of 21 insert opcion 1 for stand ")
        
                            if int(moviment) == 3:
                                os.system("clear")
                                print(player.players['player'+str(delimiter+1)])
                                player.players['player'+str(delimiter+1)]['state'] = False
                                

                    else:
                        os.system("clear")
                        print("error when selecting your movement try 1, 2 or 3")
                else:
                    os.system("clear")
                    print("error you have inserted an invalid option")
            else:
                os.system("clear") 
                input(str(player.players['player'+str(delimiter+1)]['cards'])+" point "+str(player.players['player'+str(delimiter+1)]['point'])+" your cards have exceeded to the score of 21, you lose, press enter for continue...")
                player.players['player'+str(delimiter+1)]['state'] = False
                os.system("clear") 
                delimiter += 1
                print(player.players['player'+str(delimiter+1)])
                
                
                      
        else:
            delimiter += 1
            pass
        
    Win()
p = generate_players()
system_of_turns()