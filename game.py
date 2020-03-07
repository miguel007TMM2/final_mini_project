from players import *
from crupier import Crupier
from deck_of_cards import Deck_of_cards
import os
crup = Crupier()
po = Player()
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
                    'state': True,
                    'poins': 10000,
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

def Win():
    winer = 0
    iterator = 1
    for poins1 in po.values_of_cards_players:
        while iterator < len(po.values_of_cards_players):
            points2 = po.values_of_cards_players[iterator]
            if poins1 > points2 and poins1 <= 21:
                winer = poins1
            else:    
                winer = points2
            if iterator < len(po.values_of_cards_players):
                iterator += 1
            else:
                break
    winer_posicion = po.values_of_cards_players.index(winer)
    print("El ganador es ",po.players['player'+str(winer_posicion+1)]['name'],"Con ",po.values_of_cards_players[winer_posicion],"Puntos")

def system_of_turns():
    delimiter = 0
    print("First card of crupier : " + str(crup.crupiers_two_cards()) + "  Point : " + str(card.value_and_cards[crup.crupiers_two_cards()]))
    while delimiter < (len(po.players)): 
        print(po.players['player'+str(delimiter+1)])
        po.point_of_cards()
        if po.players['player'+str(delimiter+1)]['state'] == True:
            moviment = input("1) stand  2) ask for letters  3) backing out: ➤ ")

            if moviment.isdigit():
                if int(moviment) <= 3:
                    if int(moviment) == 1:
                        if delimiter < len(po.players):
                            delimiter += 1
                            pass
                        else:
                            break
                            
                    if int(moviment) == 2:
                        if po.values_of_cards_players[delimiter] < 21:
                            po.ask_for_letters(delimiter)
                            po.values_of_cards_players[delimiter] += card.value_and_cards[po.players['player'+str(delimiter+1)]['cards'][len(po.players['player'+str(delimiter+1)]['cards'])-1]]

                        else:
                            os.system("clear")
                            print("You have to stand, your cards have exceeded or is equal to the score of 21")
                            pass 
                        

                    if int(moviment) == 3:
                        po.players['player'+str(delimiter+1)]['state'] = False
                        po.values_of_cards_players.pop(delimiter)
                        pass

                else:
                    print("error when selecting your movement try 1, 2 or 3")
            else:
                print("error you have inserted an invalid option")
        else:
            delimiter += 1
            pass
        #print("Cards of crupier : " + str(crup.Keep_holding_cards()) + "  Point : " + str(card.value_and_cards[crup.crupiers_two_cards()]))
    
    Win()
p = generate_players()
system_of_turns()