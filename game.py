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
numb_game = 1

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
                        if int(select_icon) > 0 and int(select_icon) <= 8:
                            player.players.update({
                                'player'+str(delimiter+1):{ 
                                'name':  name_of_player,
                                'icon':  player.icono_for_player[int(select_icon)-1],
                                'state': True,
                                'chip': 10000,
                                'point': 0,
                                'cards': crup.Player_curret_hand,
                                'initial_bet' : False, 
                                'bet': False }})
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
    initial_bet()
    bets()

def keep_playing():
    global numb_game
    ask_cotinue = input('Do you want to try again ? Select 1) Yes or 2) No  for continue : ')
    os.system("clear")
    if ask_cotinue.isdigit():
        if int(ask_cotinue) == 1 or int(ask_cotinue) == 2:
            if int(ask_cotinue) == 1:
                initial_bet()
            elif int(ask_cotinue) == 2:
                numb_game += 1
                player.players['player'+ str(numb_game)]['state'] = False
                initial_bet()
        else:
            print('incorrect values')
            keep_playing()
            

    else:
        print('incorrect values')
        keep_playing()
        


def initial_bet():

    global numb_game 
    try:
        initial_tokens = str(dice.index) + '00'
        if player.players['player'+ str(numb_game)]['chip'] > int(initial_tokens):
            bet = input('Enter your initial bet, point ' + initial_tokens + ' player ' + player.players['player'+ str(numb_game)]['name'] + " : ")
            if bet.isdigit():
                if int(bet)  >= int(initial_tokens):
                    player.players['player'+ str(numb_game)]['chip'] = player.players['player'+ str(numb_game)]['chip'] - int(bet)
                    crup.dic_bets.update({'name' : { player.players['player'+ str(numb_game)]['name'] : int(bet) }})
                    player.players['player'+ str(numb_game)]['initial_bet'] = True
                    player.players['player'+ str(numb_game)]['bet'] = True 
                    # print( player.players['player'+ str(numb_game)])
                    # print(crup.dic_bets['name'][player.players['player'+ str(numb_game)]['name']])
                else:

                    print('incorrect values')
                    keep_playing()

            else:
                print('Did not introduce anything')
                keep_playing()

            if player.players['player'+ str(numb_game)]['initial_bet'] == True:
                numb_game += 1 
            if numb_game > len(player.players):
                numb_game = 1 
        else:
            print('You can t keep betting for this reason you lost')
            player.players['player'+ str(numb_game)]['state'] = False
            for player_card in range (len(player.players['player'+ str(numb_game)]['cards'])):
                crup.cards_cemetery.append(player.players['player'+ str(numb_game)]['cards'].pop())
            numb_game += 1

    except KeyError:
        print('All players lose')
        print("""
                  _______      ___      .___  ___.  _______      ______   ____    ____  _______ .______         
                 /  _____|    /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \        
                |  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |       
                |  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /        
                |  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____ |  |\  \----.   
                \ ______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____| 
                                                                """+ "\n")

        def new_game():
            ask_new_game = input('Do you want to play again ? Select 1) Yes or 2) No  for continue : ')
            os.system("clear")
            if ask_new_game.isdigit():
                if int(ask_new_game) == 1 or int(ask_new_game) == 2:
                    if int(ask_new_game) == 1:
                        numb_game = 1
                        generate_players()
                    elif int(ask_new_game):
                        print('Thanks for playing with us.')
                else:
                    print('your entry is not valid')
                    new_game()
            else:
                print('your entry is not valid')
                new_game()
        new_game()

count_players = 2

def bets():
    global count_players
    minimum_bet = 50
    if count_players <= len(player.players):
        if player.players['player'+ str(count_players)]['bet'] == False :
            make_bets = input('the minimum bet is '+ str(minimum_bet) + '. Enter your bet player ' + player.players['player'+ str(count_players)]['name'] + ' : ')
            if make_bets.isdigit():
                if int(make_bets) >= minimum_bet:
                    player.players['player'+ str(count_players)]['chip'] = player.players['player'+ str(count_players)]['chip'] - int(make_bets)
                    crup.dic_bets.update({'name' : { player.players['player'+ str(count_players)]['name'] : int(make_bets) }})
                    player.players['player'+ str(count_players)]['bet'] == True 
                    print(crup.dic_bets['name'])
                    count_players += 1
                    bets()

    # for count_players in range(len(player.players)):
    #     if player.players['player'+ str(numb_game + count_players)]['name']
        

def insurance():
    pass

#This function is responsible for selecting a winner
def Win():
   pass

def system_of_turns():
    delimiter = 0
    player.point_of_cards(delimiter)
    
    while delimiter < (len(player.players)):
        player.point_of_cards_asing(delimiter)
        print(player.players['player'+str(delimiter+1)])
        if player.players['player'+str(delimiter+1)]['state'] == True:
            if player.players['player'+str(delimiter+1)]['point'] <= 21: 
                player.point_of_cards_asing(delimiter)
                moviment = input("1) Stand  2) Ask for letters  3) Backing out: ➤ ")

                if moviment.isdigit():
                    if int(moviment) <= 3:
                        if int(moviment) == 1:
                            os.system("clear")
                            
                            if delimiter < len(player.players):
                                delimiter += 1
                                pass
                            else:
                                break
                            print(player.players['player'+str(delimiter+1)])
                        
                        if int(moviment) == 2:
                            if  player.players['player'+str(delimiter+1)]['point']< 21:  
                                os.system("clear")
                                player.ask_for_letters(delimiter)
                                player.point_of_cards(delimiter)
                                print(player.players['player'+str(delimiter+1)])
                            else:
                                print("Is equal to the score of 21 insert opcion 1 for stand ")
        
                            if int(moviment) == 3:
                                os.system("clear")
                                print(player.players['player'+str(delimiter+1)])
                                player.players['player'+str(delimiter+1)]['state'] = False

                    else:
                        os.system("clear")
                        print("Error when selecting your movement try 1, 2 or 3")
                else:
                    os.system("clear")
                    print("Error you have inserted an invalid option")
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
# generate_players()
