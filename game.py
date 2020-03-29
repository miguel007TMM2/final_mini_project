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


#This function is responsible for creating the players' keys and assigning them, a name, their initial cards   and some cards
def generate_players():

    print("The limit of players that you can play at the same time are 4 ")
    limit_players = input("Entry number of players ► ") 

    if limit_players.isdigit():
        
        if int(limit_players) <= 4 and int(limit_players) > 0:
            os.system("cls")
            
            for delimiter in range(int(limit_players)):
                dealer.get_two_cards()
                def select_name():
                    global name_of_player
                    
                    name_of_player = input("Entry name of player"+str(delimiter+1)+" ► ")
                    os.system("cls")
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
                    ask_for_icon = input("insert a number of you icon ► ")
                    os.system("cls")
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
                            os.system("cls")
                            input("error the option you have inserted is not valid test with a number from 1 to 8 press enter for continue") 
                            select_icon()  
                    else:
                        input("error the option you have inserted is not valid test with a number from 1 to 8 press enter for continue") 
                        select_icon()
                select_icon()
        else:
            os.system("cls")
            input("Error entering the number of players, try a number from 1 to 4 enter to continue... ")
            generate_players()

    else:
        os.system("cls")
        input("Error entering the number of players, try a number from 1 to 4 enter to continue...") 
        generate_players()


def bets():
    minimum_bet = 50
    count_players = 1

    while count_players <= len(player.players):

        if player.players['player'+ str(count_players)]['state'] == True:

            if player.players['player'+ str(count_players)]['bet'][0] == False:

                if player.players['player'+ str(count_players)]['chip'] > minimum_bet:

                    make_bets = input('the minimum bet is '+ str(minimum_bet) + '. Enter your bet player ' + player.players['player'+ str(count_players)]['name'] + ' : ')

                    if make_bets.isdigit():

                        if int(make_bets) >= minimum_bet:

                            if int(make_bets) <= player.players['player'+ str(count_players)]['chip']:

                                player.players['player'+ str(count_players)]['chip'] = player.players['player'+ str(count_players)]['chip'] - int(make_bets)
                                player.players['player'+ str(count_players)]['bet'][1] = int(make_bets)
                                count_players += 1

                            else:
                                print('Your bet is bigger than you own please make a correct bet')
                        else:

                            print('Your bet is below accepted')
                    else:

                        print('What you have entered is not a digit or you did not write it correctly')
                else:

                    input('You can no longer continue betting and for this reason you will be removed from the game. Enter to continue ....')
                    player.players['player'+ str(count_players)]['state'] = False
                    count_players += 1
            else:

                count_players += 1
        else:

            count_players += 1

def double_bet(count):

    if player.players['player'+ str(count)]['chip'] - player.players['player'+ str(count)]['bet'][1] > 0:

        player.players['player'+ str(count)]['chip'] = player.players['player'+ str(count)]['chip'] - player.players['player'+ str(count)]['bet'][1]
        player.players['player'+ str(count)]['bet'][1] = player.players['player'+ str(count)]['bet'][1] * 2
    else:

        print('You cannot continue doubling the bet or it no longer has points')


def Win_or_lost():#This function is responsible for selecting a winner

    win = 1
    kind_reward = 0

    while win <= len(player.players):
    
        if player.players['player'+ str(win)]['state'] == True :
        
            kind_reward = 'bet'
        
            reward = player.players['player'+ str(win)][kind_reward][1] * 2
            bet_back = player.players['player'+ str(win)][kind_reward][1]

            if player.players['player'+ str(win)]['point'] > dealer.values_cards_crupier and player.players['player'+ str(win)]['point'] <= 21:

                player.players['player'+ str(win)]['chip'] = player.players['player'+ str(win)]['chip'] + reward

                print('winner')
                print('Player : ' , player.players['player'+ str(win)]['name'])
                print('Card scoring : ' , player.players['player'+ str(win)]['point'])
                print('Profits : ' ,  reward )
                input('Enter to continue')

                win += 1

            elif player.players['player'+ str(win)]['point'] == dealer.values_cards_crupier and player.players['player'+ str(win)]['point'] <= 21:

                player.players['player'+ str(win)]['chip'] = player.players['player'+ str(win)]['chip'] + bet_back

                print('Tie')
                print('Player : ' , player.players['player'+ str(win)]['name'])
                print('Card scoring : ' ,player.players['player'+ str(win)]['point'])
                print('Profits : ' , bet_back)
                input('Enter to continue')

                win += 1

            elif player.players['player'+ str(win)]['point'] < dealer.values_cards_crupier and dealer.values_cards_crupier <= 21:
                
                print('Lost')
                print('Player : ' , player.players['player'+ str(win)]['name'])
                print('Card scoring : ' ,player.players['player'+ str(win)]['point'])
                print('losses : ' , bet_back )
                input('Enter to continue \n')

                win += 1
                
            elif player.players['player'+ str(win)]['point'] > 21 and  dealer.values_cards_crupier <= 21:

                print('Lost')
                print('Player : ' , player.players['player'+ str(win)]['name'])
                print('Card scoring : ' ,player.players['player'+ str(win)]['point'])
                print('losses : ' , bet_back )
                input('Enter to continue \n')

                win += 1

            elif dealer.values_cards_crupier > 21:
                
                player.players['player'+ str(win)]['chip'] = player.players['player'+ str(win)]['chip'] + reward

                print('winner')
                print('Player : ' , player.players['player'+ str(win)]['name'])
                print('Card scoring : ' , player.players['player'+ str(win)]['point'])
                print('Profits : ' , reward )
                input('Enter to continue \n')

                win += 1
        else:
            win += 1




class Game:
    def __init__(self):
        self.iterator = 0
        self.delimiter = 1
        self.cards_crupier_Value = cards.value_and_cards[dealer.crupier_curret_hand[0]]
        
        
    def moveMenu(self):
        if player.players['player'+str(self.delimiter)]['state']:
            if len(player.players['player'+str(self.delimiter)]['cards']) == 2:
                
                if player.players['player'+str(self.delimiter)]['point'] == 21:
                        os.system("cls")
                        print(""" 
                                        ____  _            _       _            _                        
                                        | __ )| | __ _  ___| | __  | | __ _  ___| | __                    
                                        |  _ \| |/ _` |/ __| |/ _  | |/ _` |/ __| |/ /                      
                                        | |_) | | (_| | (__|   | |_| | (_| | (__|   <                     
                                        |____/|_|\__,_|\___|_|\_\___/ \__,_|\___|_|\_\ 
                        
                                    you win """+player.players['player'+str(self.delimiter)]['name']+"""
                        """)
                        self.delimiter += 1
                        time.sleep(3)
                        os.system("cls")
                        self.moveMenu()

            time.sleep(0.15)
            if player.players['player'+str(self.delimiter)]['state']:
                if self.iterator == 0:

                    show.opcion[2] = "|3) double the bet           |"
                    show.opcion[1] = "|2) Ask for cards            |" 
                    show.opcion[0] = "|1) Stand  ◄                 |"
                    os.system("cls")
                    show.table(player.players, player.players['player'+str(self.delimiter)], dealer.crupier_curret_hand[0],self.cards_crupier_Value)
                    
                elif self.iterator == 1:

                    show.opcion[0] = "|1) Stand                    |" 
                    show.opcion[1] = "|2) Ask for cards   ◄        |" 
                    show.opcion[2] = "|3) double the bet           |"
                    os.system("cls")
                    show.table(player.players, player.players['player'+str(self.delimiter)], dealer.crupier_curret_hand[0],self.cards_crupier_Value)
                
                elif self.iterator == 2:

                    show.opcion[0] = "|1) Stand                    |" 
                    show.opcion[1] = "|2) Ask for cards            |" 
                    show.opcion[2] = "|3) double the bet ◄         |"
                    os.system("cls")
                    show.table(player.players,  player.players['player'+str(self.delimiter)], dealer.crupier_curret_hand[0],self.cards_crupier_Value)
            

                while True:
                    if self.delimiter >= 5:
                        break 
                        
                    
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

                        if self.iterator == 2:
                            if len(player.players['player'+str(self.delimiter)]['cards']) == 2:
                                double_bet(self.delimiter)
                                self.moveMenu()
                            else:
                                print("you cannot double the bet after requesting a card. you have to double the bet before asking for a card")
                                time.sleep(3)

                dealer.Keep_holding_cards()
                show.table(player.players,  player.players['player1'], " ".join(dealer.crupier_curret_hand),dealer.values_cards_crupier)
            else:
                self.delimiter += 1
                self.moveMenu()
        else:
            self.delimiter += 1

                
                                 
        

        Win_or_lost()
        new_game()

def new_game():
    ask_new_game = input('Do you want to play again ? Select 1) Yes or 2) No  for continue : ')
    os.system("cls")
    if ask_new_game.isdigit():
        if int(ask_new_game) == 1 or int(ask_new_game) == 2:
            if int(ask_new_game) == 1:
                numb_game = 1
                dealer.crupier_curret_hand = []
                dealer.values_cards_crupier = 0
                dealer.Player_curret_hand = [[]]
                dealer.cards.Generator_of_cards()
                dealer.cards.shuffle_the_cards(dealer.cards.list_of_cards)

                for reset in range(1, 5):
                    for player_card in range (len(player.players['player'+ str(reset)]['cards'])):
                        dealer.cards_cemetery.append(player.players['player'+ str(reset)]['cards'].pop())
                        
                    if player.players['player'+str(reset)]['state'] == True:
                        player.players['player'+str(reset)]['cards'] = ''
                        player.players['player'+str(reset)]['point'] = ""
                        player.players['player'+str(reset)]['bet'] = [False , 0]
                        dealer.get_two_cards()
                        player.players['player'+str(reset)]['cards'] = dealer.Player_curret_hand[0]
                        player.players['player'+str(reset)]['point'] = dealer.Player_curret_hand[1]
                        dealer.Player_curret_hand = [[]]


                dealer.crupier_curret_hand = []
                dealer.values_cards_crupier = 0
                dealer.crupiers_two_cards()

                bets()
                game = Game()
                game.moveMenu()

            elif int(ask_new_game):
                print('Thanks for playing with us.')
                time.sleep(5)
                os.sys.exit()
        else:
            print('your entry is not valid')
            new_game()

    else:
        print('your entry is not valid')
        new_game()

generate_players()
bets()
menu = Game()
menu.moveMenu()

