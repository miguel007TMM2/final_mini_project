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



def select_name(iterator):

    global name_of_player
    
    name_of_player = input("Entry name of player"+str(iterator+1)+" ➤ ")
    os.system("clear")

    if len(name_of_player) >= 10:

        print("error the length of your name is too long test with a name less than 10 digits")
        select_name()
    else:
        return name_of_player


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
                input('Enter to continue')

                win += 1

            elif dealer.values_cards_crupier >= 21:
                
                player.players['player'+ str(win)]['chip'] = player.players['player'+ str(win)]['chip'] + reward

                print('winner')
                print('Player : ' , player.players['player'+ str(win)]['name'])
                print('Card scoring : ' , player.players['player'+ str(win)]['point'])
                print('Profits : ' , reward )
                input('Enter to continue')

                win += 1
        else:
            win += 1

def new_game():
    ask_new_game = input('Do you want to play again ? Select 1) Yes or 2) No  for continue : ')
    os.system("clear")

    if ask_new_game.isdigit():
        if int(ask_new_game) == 1 or int(ask_new_game) == 2:
            if int(ask_new_game) == 1:
                numb_game = 1

                for reset in range(1, 5):

                    for player_card in range (len(player.players['player'+ str(reset)]['cards'])):
                        dealer.cards_cemetery.append(player.players['player'+ str(reset)]['cards'].pop())
                        cards.list_of_cards.append(dealer.cards_cemetery.pop())
                        cards.shuffle_the_cards(cards.list_of_cards)

                    player.players['player'+str(reset)]['cards'] = ''
                    player.players['player'+str(reset)]['point'] = ''
                    player.players['player'+str(reset)]['bet'] = [False , 0]
         

                    if player.players['player'+str(reset)]['state'] == True:

                        dealer.get_two_cards()

                        player.players['player'+str(reset)]['cards'] = dealer.Player_curret_hand[0]
                        player.players['player'+str(reset)]['point'] = dealer.Player_curret_hand[1]
                        dealer.Player_curret_hand  = [[]]
                        
                dealer.crupier_curret_hand = []
                dealer.values_cards_crupier = 0
                dealer.crupiers_two_cards()
                bets()
                menu = Menu()
                
            elif int(ask_new_game):
                print('Thanks for playing with us.')

        else:
            print('your entry is not valid')
            new_game()
            
    else:
        print('your entry is not valid')
        new_game()

class Game:
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
                                self.moveMenu()

                            else:
                                break
                        
                        if self.iterator == 3:
                    
                            double_bet(self.iterator)
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
                           
                            
                            self.delimiter += 1
                            self.iterator = 0
                            self.moveMenu()  
                dealer.Keep_holding_cards()
                show.table(player.players,  player.players['player1'], " ".join(dealer.crupier_curret_hand),dealer.values_cards_crupier)
                                 
            if player.players['player1']['state'] == False and player.players['player2']['state'] == False and player.players['player3']['state'] == False and player.players['player4']['state'] == False:
                show.icon()
                os.sys.exit()

            Win_or_lost()
            new_game()
            
generate_players()
bets()
menu = Menu()
menu.moveMenu()

