from players import Player
from crupier import Crupier
from dice import Dice
from deck_of_cards import Deck_of_cards
from view import View
import os
import time
import keyboard
dealer = Crupier()
dice =  Dice()
dice.status()
show = View()
player = Player()
cards = Deck_of_cards()
numb_game = 1


#This function is responsible for creating the players' keys and assigning them, a name, their initial letters and some cards
def generate_players():

    print("The limit of players that you can play at the same time are 4 ")
    limit_players = input("Entry number of players ➤ ") 

    if limit_players.isdigit():
        
        if int(limit_players) <= 4 and int(limit_players) > 0:
            os.system("clear")
            
            for delimiter in range(int(limit_players)):
                dealer.get_two_cards()
                def select_name():
                    global name_of_player
                    
                    name_of_player = input("Entry name of player"+str(delimiter+1)+" ➤ ")
                    os.system("clear")
                    if len(name_of_player) >= 10:
                        print("error the length of your name is too long test with a name less than 10 digits")
                        select_name()

                    else:
                        return name_of_player
                select_name()
                print("Select you icon")
               
                def select_icon():
                    number_icon = 1
                    for icons in player.icono_for_player:
                        print(number_icon,icons)
                        number_icon += 1
                    ask_for_icon = input("insert a number of you icon ➤ ")
                    os.system("clear")
                    if ask_for_icon.isdigit():
                        if int(ask_for_icon) > 0 and int(ask_for_icon) <= 8:
                            player.players.update({
                                
                                'player'+str(delimiter+1):{ 
                                'name':  name_of_player,
                                'icon':  player.icono_for_player[int(ask_for_icon)-1],
                                'state': True,
                                'chip': 10000,
                                'point': dealer.Player_curret_hand[1],
                                'cards': dealer.Player_curret_hand[0],
                                'initial_bet' : [False , 0], 
                                'bet': [False, 0],
                                'insurance': None}})

                            dealer.Player_curret_hand  = [[]]
                        else:
                            os.system("clear")
                            input("error the option you have inserted is not valid test with a number from 1 to 5 press enter for continue") 
                            select_icon()  
                    else:
                        input("error the option you have inserted is not valid test with a number from 1 to 5 press enter for continue") 
                        select_icon()
                select_icon()
        else:
            os.system("clear")
            input("Error entering the number of players, try a number from 1 to 4 enter to continue... ")
            generate_players()

    else:
        os.system("clear")
        input("Error entering the number of players, try a number from 1 to 4 enter to continue...") 
        generate_players()


def initial_bet():

    global numb_game 
    try:
        initial_tokens = str(dice.index) + '00'
        if player.players['player'+ str(numb_game)]['state'] == True:
            if player.players['player'+ str(numb_game)]['chip'] > int(initial_tokens):

                bet = input('Enter your initial bet, point ' + initial_tokens + ' player ' + player.players['player'+ str(numb_game)]['name'] + " : ")
                if bet.isdigit():

                    if int(bet)  >= int(initial_tokens):

                        player.players['player'+ str(numb_game)]['chip'] = player.players['player'+ str(numb_game)]['chip'] - int(bet)
                        player.players['player'+ str(numb_game)]['initial_bet'][1] = int(bet)
                        player.players['player'+ str(numb_game)]['initial_bet'][0] = True
                        player.players['player'+ str(numb_game)]['bet'][0] = True 

                    else:
                        print('Your bet is below accepted')
                        contue_ask = input('Enter to continue or write exit to finish the game.... ')

                        if contue_ask !=  'exit':
                            initial_bet()

                        if contue_ask.isdigit() == False:

                            if contue_ask == 'exit':
                                player.players['player'+ str(numb_game)]['state'] = False
                                numb_game += 1
                                initial_bet()

                else:
                    print('Did not introduce anything or is it misspelled ')
                    contue_ask = input('Enter to continue or write exit to finish the game.... ')

                    if contue_ask !=  'exit':
                        initial_bet()

                    if contue_ask.isdigit() == False:

                        if contue_ask == 'exit':
                            player.players['player'+ str(numb_game)]['state'] = False
                            numb_game += 1
                            initial_bet()

                if True in player.players['player'+ str(numb_game)]['initial_bet']:
                    numb_game += 1 

                if numb_game > len(player.players):
                    numb_game = 1 

            else:
                print('You can t keep betting for this reason you lost')
                player.players['player'+ str(numb_game)]['state'] = False
                for player_card in range (len(player.players['player'+ str(numb_game)]['cards'])):
                    dealer.cards_cemetery.append(player.players['player'+ str(numb_game)]['cards'].pop())
                numb_game += 1
        else:
            numb_game += 1
            initial_bet()

    except KeyError:
        show.icon()


count_players = 2

def bets():

    global count_players
    minimum_bet = 50

    if count_players <= len(player.players):
        if player.players['player'+ str(count_players)]['state'] == True:
            if player.players['player'+ str(count_players)]['bet'][0] == False:

                if player.players['player'+ str(count_players)]['chip'] > minimum_bet:

                    make_bets = input('the minimum bet is '+ str(minimum_bet) + '. Enter your bet player ' + player.players['player'+ str(count_players)]['name'] + ' : ')
                    if make_bets.isdigit():

                        if int(make_bets) >= minimum_bet:

                            player.players['player'+ str(count_players)]['chip'] = player.players['player'+ str(count_players)]['chip'] - int(make_bets)
                            player.players['player'+ str(count_players)]['bet'][1] = int(make_bets)
                            player.players['player'+ str(count_players)]['bet'][0] = True 
                            count_players += 1
                            bets()

                        else:
                            print('Your bet is below accepted')
                            contue_ask = input('Enter to continue or write exit to finish the game.... ')

                            if contue_ask !=  'exit':
                                bets()

                            if contue_ask.isdigit() == False:

                                if contue_ask == 'exit':
                                    player.players['player'+ str(numb_game)]['state'] = False
                                    count_players += 1
                                    bets()
                    else:
                        print('What you have entered is not a digit or you did not write it correctly')
                        bets()


                else:
                    print('You can no longer continue betting and for this reason you will be removed from the game. Enter to continue ....')
                    count_players += 1
                    bets()
        else:
            count_players += 1
            bets()        
        
def double_bet(count):
    player.players['player'+ str(count)]['chip'] = player.players['player'+ str(count)]['chip'] - player.players['player'+ str(count)]['initial_bet'][1]
    player.players['player'+ str(count)]['chip'] = player.players['player'+ str(count)]['chip'] - player.players['player'+ str(count)]['bet'][1]

    player.players['player'+ str(count)]['initial_bet'][1] = player.players['player'+ str(count)]['initial_bet'][1] * 2
    player.players['player'+ str(count)]['bet'][1] = player.players['player'+ str(count)]['bet'][1] * 2

def insurance():

    verification = 1
    if cards.value_and_cards [dealer.crupier_curret_hand[0]] == 1 or cards.value_and_cards [dealer.crupier_curret_hand[0]] == 11:

        while verification <= len(player.players):
            if player.players['player'+ str(verification)]['chip'] >= 50:

                print('The first dealer card is an As. Do you want to make a insurance bet ? ' + 'player ' +  str(player.players['player'+ str(verification)]['name']))
                bet_insurance = input('Between your insurance bet  or press enter to not bet  : ')

                if bet_insurance.isdigit():
                    if int(bet_insurance) <= player.players['player'+ str(verification)]['chip']:
                        player.players['player'+ str(verification)]['chip'] = player.players['player'+ str(verification)]['chip'] - int(bet_insurance)
                        player.players['player'+ str(verification)]['insurance'] = int(bet_insurance) 

                        print('your bet is made')
                        verification += 1
                        time.sleep(0.30)
                        os.system("clear")

                    else:
                        print('you don t have that many points to bet, write your bet again')

                elif bet_insurance == '':
                    print('you didn t bet for sure')
                    verification += 1
                    time.sleep(0.30)
                    os.system("clear")

                else:
                    print('incorrect values')

            else:
                print( str(player.players['player'+ str(verification)]['name'])+ 'you lose because you don t have enough to keep betting')
                verification += 1
                time.sleep(0.30)
                os.system("clear")


def Win_or_lost():#This function is responsible for selecting a winner

    win = 1
    index = 1
    kind_reward = 0

    while win <= len(player.players):
    
        if player.players['player'+ str(win)]['state'] == True :

            if player.players['player'+ str(win)]['initial_bet'][1] == 0:
                kind_reward = 'bet'
            elif player.players['player'+ str(win)]['bet'][1] == 0:
                kind_reward = 'initial_bet'
            
            reward = player.players['player'+ str(win)][kind_reward][1] * 2
            bet_back = player.players['player'+ str(win)][kind_reward][1]     

            if player.players['player'+ str(win)]['point'] > dealer.values_cards_crupier and player.players['player'+ str(win)]['point'] < 21:

                player.players['player'+ str(win)]['chip'] = player.players['player'+ str(win)]['chip'] + reward

                print('winner')
                print('Player : ' , player.players['player'+ str(win)]['name'])
                print('Card scoring : ' , player.players['player'+ str(win)]['point'])
                print('Profits : ' ,  reward )
                input('Enter to continue')
                win += 1

            elif player.players['player'+ str(win)]['point'] == dealer.values_cards_crupier and player.players['player'+ str(win)]['point'] < 21:

                player.players['player'+ str(win)]['chip'] = player.players['player'+ str(win)]['chip'] + bet_back

                print('Tie')
                print('Player : ' , player.players['player'+ str(win)]['name'])
                print('Card scoring : ' ,player.players['player'+ str(win)]['point'])
                print('Profits : ' , bet_back)
                input('Enter to continue')
                win += 1

            elif player.players['player'+ str(win)]['point'] < dealer.values_cards_crupier and dealer.values_cards_crupier < 21:
                
                print('Lost')
                print('Player : ' , player.players['player'+ str(win)]['name'])
                print('Card scoring : ' ,player.players['player'+ str(win)]['point'])
                print('losses : ' , bet_back )
                input('Enter to continue')
                win += 1

            elif dealer.values_cards_crupier > 21:
                
                player.players['player'+ str(win)]['chip'] = player.players['player'+ str(win)]['chip'] + reward
                print('winner')
                print('Player : ' , player.players['player'+ str(win)]['name'])
                print('Card scoring : ' , player.players['player'+ str(win)]['point'])
                print('Profits : ' , reward )
                input('Enter to continue')
                win += 1

        else:
            win += 1





class Menu:
    def __init__(self):

        self.iterator = 0
        self.delimiter = 1
        self.cards_crupier_Value = cards.value_and_cards[dealer.crupier_curret_hand[0]]

    def moveMenu(self):
            time.sleep(0.15)
            if player.players['player'+str(self.delimiter)]['state']:
                if self.iterator == 0:

                    show.opcion[3] = "|4) double the bet           |"
                    show.opcion[1] = "|2) Ask for letters          |" 
                    show.opcion[2] = "|3) Backing out              |" 
                    show.opcion[0] = "|1) Stand  ◄                 |"
                    os.system("clear")
                    show.table(player.players, player.players['player'+str(self.delimiter)], dealer.crupier_curret_hand[0],self.cards_crupier_Value)
                    
                elif self.iterator == 1:

                    show.opcion[0] = "|1) Stand                    |" 
                    show.opcion[2] = "|3) Backing out              |" 
                    show.opcion[1] = "|2) Ask for letters ◄        |"
                    show.opcion[3] = "|4) double the bet           |"
                    os.system("clear")
                    show.table(player.players, player.players['player'+str(self.delimiter)], dealer.crupier_curret_hand[0],self.cards_crupier_Value)
                
                
                elif self.iterator == 2:

                    show.opcion[0] = "|1) Stand                    |" 
                    show.opcion[1] = "|2) Ask for letters          |" 
                    show.opcion[2] = "|3) Backing out  ◄           |"
                    show.opcion[3] = "|4) double the bet           |"
                    os.system("clear")
                    show.table(player.players,  player.players['player'+str(self.delimiter)], dealer.crupier_curret_hand[0],self.cards_crupier_Value)
                elif self.iterator == 3:

                    show.opcion[0] = "|1) Stand                    |" 
                    show.opcion[1] = "|2) Ask for letters          |" 
                    show.opcion[2] = "|3) Backing out              |"
                    show.opcion[3] = "|4) double the bet ◄         |"
                    os.system("clear")
                    show.table(player.players,  player.players['player'+str(self.delimiter)], dealer.crupier_curret_hand[0],self.cards_crupier_Value)
            
                    

                while True:
                    if self.delimiter >= 5:
                        break 
                        
                    
                    if keyboard.is_pressed("down"):
                        self.iterator += 1

                        if self.iterator == 4:
                            self.iterator = 0

                        self.moveMenu()

                    elif keyboard.is_pressed("up"):
                        self.iterator -= 1

                        if self.iterator == -1:
                            self.iterator = 3

                        self.moveMenu()

                    if keyboard.is_pressed(" "):

                        if self.iterator == 1:

                            if player.players['player'+str(self.delimiter)]['point'] < 21:

                                player.players['player'+str(self.delimiter)]['point'] = dealer.get_card(player.players['player'+str(self.delimiter)]['cards'])
                                show.table(player.players, player.players['player'+str(self.delimiter)], dealer.crupier_curret_hand[0],self.cards_crupier_Value)
                                self.moveMenu()

                            else:

                                input("You have to stand, your cards have exceeded or is equal to the score of 21")
                                self.moveMenu()
                
                        if self.iterator == 0:

                            if self.delimiter < len(player.players):
                                self.delimiter += 1

                            if player.players['player'+str(self.delimiter)]['state']:
                                show.table(player.players, player.players['player'+str(self.delimiter)], dealer.crupier_curret_hand[0],self.cards_crupier_Value)
                            else:
                                break
                            
                            self.moveMenu()

                        if self.iterator == 3:
                            double_bet(self.delimiter)
                            self.moveMenu()

                        if self.iterator == 2:
                            

                            player.players['player'+str(self.delimiter)]['state'] = False
                            player.players['player'+str(self.delimiter)]['name'] =  ""
                            player.players['player'+str(self.delimiter)]['icon'] =  ""
                            player.players['player'+str(self.delimiter)]['chip'] =  ""
                            player.players['player'+str(self.delimiter)]['point'] = ""
                            player.players['player'+str(self.delimiter)]['cards'] = ""
                            player.players['player'+str(self.delimiter)]['bet'] = [False," "]
                            player.players['player'+str(self.delimiter)]['initial_bet'] = [False, " "]
                            
                        
                                
                            self.delimiter += 1
                            self.iterator = 0
                            self.moveMenu()  
                dealer.Keep_holding_cards()
                show.table(player.players,  player.players['player1'], " ".join(dealer.crupier_curret_hand),dealer.values_cards_crupier)
                                 
            
                


            if player.players['player1']['state'] == False and player.players['player2']['state'] == False and player.players['player3']['state'] == False and player.players['player4']['state'] == False:
                show.icon()
                os.sys.exit()
                                     
def new_game():
    ask_new_game = input('Do you want to play again ? Select 1) Yes or 2) No  for continue : ')
    os.system("clear")
    if ask_new_game.isdigit():
        if int(ask_new_game) == 1 or int(ask_new_game) == 2:
            if int(ask_new_game) == 1:
                numb_game = 1
                cards
                for reset in range(1,5):
                   player.players['player'+str(reset)]['cards'] = ""
                   player.players['player'+str(reset)]['point'] = ""
                   player.players['player'+str(reset)]['bet'] = [False , 0]
                   player.players['player'+str(reset)]['initial_bet'] = [False , 0]

                   if player.players['player'+str(reset)]['state']:
                        dealer.get_two_cards()
                        player.players['player'+str(reset)]['cards'] = dealer.Player_curret_hand[0]
                        player.players['player'+str(reset)]['point'] = dealer.Player_curret_hand[1]
                        dealer.Player_curret_hand  = [[]]
                        
                dealer.crupier_curret_hand = []
                dealer.values_cards_crupier = 0
                dealer.crupiers_two_cards()
                initial_bet()
                menu = Menu()
                menu.moveMenu()
                
            elif int(ask_new_game):
                print('Thanks for playing with us.')
        else:
            print('your entry is not valid')
            new_game()
    else:
        print('your entry is not valid')
        new_game()

    #         else:
    #             print("error when inserting movement test with 1 or 2")


generate_players()
initial_bet()
bets()
menu = Menu()
menu.moveMenu()
Win_or_lost()
new_game()