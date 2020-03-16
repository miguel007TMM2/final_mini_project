from players import Player
from crupier import Crupier
from deck_of_cards import Deck_of_cards
from view import View
import os
dealer = Crupier()
# dice =  Dice()
# dice.status()
show = View()
import os
player = Player()
cards = Deck_of_cards()
numb_game = 1
import keyboard
import time

#This function is responsible for creating the players' keys and assigning them, a name, their initial letters and some cards
def generate_players():

    print("The limit of players that you can play at the same time are 4 ")
    limit_players = input("Entry number of players ➤ ") 

    if limit_players.isdigit():
        
        if int(limit_players) <= 4 and int(limit_players) > 0:
            os.system("clear")
            
            for delimiter in range(int(limit_players)):
                dealer.two_cards_for_player()
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
                            del player.players['player'+str(delimiter+1)]
                            player.players.update({
                                
                                'player'+str(delimiter+1):{ 
                                'name':  name_of_player,
                                'icon':  player.icono_for_player[int(select_icon)-1],
                                'state': True,
                                'chip': 10000,
                                'point': 0,
                                'cards': dealer.Player_curret_hand,
                                'initial_bet' : False, 
                                'bet': False }})
                            dealer.Player_curret_hand  = []
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


def status_change():

    player.players['player'+ str(numb_game)]['initial_bet'] = 'Exit'
    player.players['player'+ str(numb_game)]['bet'] = 'Exit'
    player.players['player'+ str(numb_game)]['state'] = 'Exit'
        

def initial_bet():

    global numb_game 
    try:
        initial_tokens = str(dice.index) + '00'
        if player.players['player'+ str(numb_game)]['chip'] > int(initial_tokens):

            bet = input('Enter your initial bet, point ' + initial_tokens + ' player ' + player.players['player'+ str(numb_game)]['name'] + " : ")
            if bet.isdigit():

                if int(bet)  >= int(initial_tokens):

                    player.players['player'+ str(numb_game)]['chip'] = player.players['player'+ str(numb_game)]['chip'] - int(bet)
                    dealer.dic_bets.update({'name' : { player.players['player'+ str(numb_game)]['name'] : int(bet) }})
                    player.players['player'+ str(numb_game)]['initial_bet'] = True
                    player.players['player'+ str(numb_game)]['bet'] = True 

                else:
                    print('Your bet is below accepted')
                    contue_ask = input('Enter to continue or write exit to finish the game.... ')

                    if contue_ask !=  'exit':
                        initial_bet()

                    if contue_ask.isdigit() == False:

                        if contue_ask == 'exit':
                            status_change()
                            numb_game += 1
                            initial_bet()

            else:
                print('Did not introduce anything or is it misspelled ')
                contue_ask = input('Enter to continue or write exit to finish the game.... ')

                if contue_ask !=  'exit':
                    initial_bet()

                if contue_ask.isdigit() == False:

                    if contue_ask == 'exit':
                        status_change()
                        numb_game += 1
                        initial_bet()

            if player.players['player'+ str(numb_game)]['initial_bet'] == True:
                numb_game += 1 

            if numb_game > len(player.players):
                numb_game = 1 

        else:
            print('You can t keep betting for this reason you lost')
            player.players['player'+ str(numb_game)]['state'] = False
            for player_card in range (len(player.players['player'+ str(numb_game)]['cards'])):
                dealer.cards_cemetery.append(player.players['player'+ str(numb_game)]['cards'].pop())
            numb_game += 1

    except KeyError:
        show.icon()


count_players = 2

def bets():

    global count_players
    minimum_bet = 50

    if count_players <= len(player.players):
        if player.players['player'+ str(count_players)]['bet'] == False:

            if player.players['player'+ str(count_players)]['chip'] > minimum_bet:

                make_bets = input('the minimum bet is '+ str(minimum_bet) + '. Enter your bet player ' + player.players['player'+ str(count_players)]['name'] + ' : ')
                if make_bets.isdigit():

                    if int(make_bets) >= minimum_bet:

                        player.players['player'+ str(count_players)]['chip'] = player.players['player'+ str(count_players)]['chip'] - int(make_bets)
                        dealer.dic_bets.update({'name' : { player.players['player'+ str(count_players)]['name'] : int(make_bets) }})
                        player.players['player'+ str(count_players)]['bet'] == True 
                        print(dealer.dic_bets['name'])
                        count_players += 1
                        bets()

                    else:
                        print('Your bet is below accepted')
                        contue_ask = input('Enter to continue or write exit to finish the game.... ')

                        if contue_ask !=  'exit':
                            bets()

                        if contue_ask.isdigit() == False:

                            if contue_ask == 'exit':
                                status_change()
                                count_players += 1
                                bets()
                else:
                    print('What you have entered is not a digit or you did not write it correctly')
                    bets()


            else:
                print('You can no longer continue betting and for this reason you will be removed from the game. Enter to continue ....')
                count_players += 1
                bets()

        

# def insurance():
#     if cards.value_of_cards[dealer.croupier_hand[0]] = 11 or cards.value_of_cards[dealer.croupier_hand[0]] == 11
#     for 

#This function is responsible for selecting a winner
def Win():
   pass


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

    #         else:
    #             print("error when inserting movement test with 1 or 2")

        
    Win()

generate_players()

class Menu:
    def __init__(self):
        self.iterator = 0
        self.delimiter = 1
        
    def moveMenu(self):
        
            time.sleep(0.15)
            
            if self.iterator == 0:
                show.opcion[1] = "|2) Ask for letters          |" 
                show.opcion[2] = "|3) Backing out              |" 
                show.opcion[0] = "|1) Stand  ◄                 |"
                os.system("clear")
                show.table(player.players, player.players['player'+str(self.delimiter)])
                
            elif self.iterator == 1:
                show.opcion[0] = "|1) Stand                    |" 
                show.opcion[2] = "|3) Backing out              |" 
                show.opcion[1] = "|2) Ask for letters ◄        |"
                os.system("clear")
                show.table(player.players, player.players['player'+str(self.delimiter)])
            
            
            elif self.iterator == 2:
                show.opcion[0] = "|1) Stand                    |" 
                show.opcion[1] = "|2) Ask for letters          |" 
                show.opcion[2] = "|3) Backing out  ◄           |" 
                os.system("clear")
                show.table(player.players,  player.players['player'+str(self.delimiter)])

            while True:
                if keyboard.is_pressed("down"):
                    self.iterator += 1
                    if self.iterator == 3:
                        self.iterator = 0
                    self.moveMenu()

                elif keyboard.is_pressed("up"):
                    self.iterator -= 1
                    if self.iterator == -1:
                        self.iterator = 2
                    self.moveMenu()

                if keyboard.is_pressed("enter"):
                    if self.iterator == 1:
                        player.ask_for_letters(self.delimiter)
                        show.table(player.players, player.players['player'+str(self.delimiter)])
                        self.moveMenu()

                    if self.iterator == 0:
                        self.delimiter += 1
                        if player.players['player'+str(self.delimiter)]['state']:
                            show.table(player.players, player.players['player'+str(self.delimiter)])
                        else:
                            break
                        self.moveMenu()

menu = Menu()
menu.moveMenu()