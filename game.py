from players import Player
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
        input("Error entering the number of players, try a number from 1 to 4 enter to continue...") 
        generate_players()
    

def keep_playing():

    global numb_game 
    ask_cotinue = input('Do you want to try again ? Select 1) Yes or 2) No  for continue : ')
    os.system("clear")
    if ask_cotinue.isdigit():
        if int(ask_cotinue) == 1 or int(ask_cotinue) == 2:
            if int(ask_cotinue) == 1:
                initial_bet()
            elif int(ask_cotinue) == 2:
                numb_game  += 1
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
                print('Did not introduce anything or is it misspelled ')
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
        print(show.icon())

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
                if player.players['player'+ str(count_players)]['chip'] > minimum_bet:
                    if int(make_bets) >= minimum_bet:
                        player.players['player'+ str(count_players)]['chip'] = player.players['player'+ str(count_players)]['chip'] - int(make_bets)
                        crup.dic_bets.update({'name' : { player.players['player'+ str(count_players)]['name'] : int(make_bets) }})
                        player.players['player'+ str(count_players)]['bet'] == True 
                        print(crup.dic_bets['name'])
                        count_players += 1
                        bets()
                    else:
                        print('Your bet is below accepted')
                        contue_ask = input('Enter to continue or write exit to finish the game.... ')
                        if contue_ask == '':
                            bets()
                            pass
                        elif contue_ask.upper() == ' Exit':
                            pass
                        

            else:
                pass
    # for count_players in range(len(player.players)):
    #     if player.players['player'+ str(numb_game + count_players)]['name']
        

def insurance():
    pass

#This function is responsible for selecting a winner
def Win():
   pass

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
