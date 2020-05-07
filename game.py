from players import Player
from crupier import Crupier
from cards import Deck
from view import View
import os
import time
import keyboard

deck_of_cards = Deck()
dealer = Crupier(deck_of_cards)
show = View()
class Game:

    def __init__(self):

        self.players = []
        self.player_icons = ['☠', '☢', '☣' ,'♞','☯', '♪', '❆','✟']

    def select_name(self,iterator):
        global name_of_player

        name_of_player = input("Entry name of player"+str(iterator+1)+" ► ")
        os.system("cls")

        if len(name_of_player) >= 10:

            print("error the length of your name is too long test with a name less than 10 digits")
            self.select_name(iterator)

        else:
            return name_of_player

    def select_icons(self,iterator):
        print("Select you icon")
        def show_icons(player_icon):
            for index in range(0,len(player_icon)):
                print(index + 1,player_icon[index])

        show_icons(self.player_icons)
        selected_icon = input("insert a number of you icon ► ")

        def entry_is_valid(value):
            if value.isdigit():
                return int(value) > 0 and int(value) <= 8

            return False

        if entry_is_valid(selected_icon):
            return self.player_icons[int(selected_icon) - 1]
            os.system("cls")

        else:
             os.system("cls")
             input("error the option you have inserted is not valid test with a number from 1 to 8 press enter for continue")
             self.select_icons(iterator)

    def create_players(self): 

        global player
        number_of_player = input("Entry number of players ► ")

        def is_entry_valid(entry):
            if number_of_player.isdigit():
                 return entry > 0 and entry <= 4

            return False

        if is_entry_valid(int(number_of_player)):
            os.system("cls")

            for n in range(int(number_of_player)):

                dealer.get_two_cards()
                player_name = self.select_name(n)
                player_icon = self.select_icons(n)
                self.players.append(Player(player_name,player_icon,True,10000,dealer.get_two_cards(),0,0,False))
                self.players[n].point = self.players[n].calculate_player_point()
        else:
            os.system("cls")
            input("Error entering the number of players, try a number from 1 to 4 enter to continue...")
            self.create_players()


    def betting_system(self):

        self.minimum_bet = 50
        self.count_players = 0

        while self.count_players < len(self.players):

            if self.players[self.count_players].state == True:

                if self.players[self.count_players].bet_state == False:

                    if self.players[self.count_players].chips > self.minimum_bet:

                        self.make_bets = input('the minimum bet is '+ str(self.minimum_bet) + '. Enter your bet player ' + self.players[self.count_players].name + ' you have ' + str(self.players[self.count_players].chips) + ' chips : ')

                        if self.make_bets.isdigit():

                            if int(self.make_bets) >= self.minimum_bet:

                                if int(self.make_bets) <= self.players[self.count_players].chips:

                                    self.players[self.count_players].chips = self.players[self.count_players].chips - int(self.make_bets)
                                    self.players[self.count_players].bet = int(self.make_bets)
                                    self.count_players += 1

                                else:
                                    print("Your bet is bigger than you own please make a correct bet")
                            else:
                                print("Your bet is below accepted")
                        else:
                            print("What you have entered is not a digit or you did not write it correctly")
                    else:
                        input("You can no longer continue betting and for this reason you will be removed from the game. Enter to continue ....")
                        self.players[self.count_players].state = False
                        self.count_players += 1
                else:
                    self.count_players += 1
            else:
                self.count_players += 1

    def double_bet(self,count):

        if self.players[count].chips - self.players[count].bet > 0:

            self.players[count].chips = self.players[count].chips - self.players[count].bet
            self.players[count].bet = self.players[count].bet * 2

        else:

            print("You cannot continue doubling the bet or it no longer has point")

    def player_data(self, player, point, bet_result, player_result):

        dealer_value_card = 'dealer points : ' + str(dealer.values_cards_crupier ) + " \n"
        player = "Player: " + str(player) + " \n"
        Card_scoring = "Card scoring: " + str(point) + " \n"
        bet_result = player_result +' : '+ str(bet_result) + "\n"

        data = dealer_value_card  + player + Card_scoring + bet_result

        input(data + "Enter to continue \n")

    def calculate_final_results(self):

        self.win = 0

        while self.win < len(self.players):

            if self.players[self.win].state == True:

                self.reward = self.players[self.win].bet * 2
                self.bet_back = self.players[self.win].bet

                if self.players[self.win].point > dealer.values_cards_crupier and self.players[self.win].point <= 21:

                    self.players[self.win].chips = self.players[self.win].chips + self.reward
                    self.player_data(self.players[self.win].name, self.players[self.win].point, self.reward, 'profits')
                    self.win += 1

                elif self.players[self.win].point == dealer.values_cards_crupier and self.players[self.win].point <= 21:

                    self.players[self.win].chips = self.players[self.win].chips + self.bet_back
                    self.player_data(self.players[self.win].name, self.players[self.win].point, self.reward, 'bet back')
                    self.win += 1

                elif self.players[self.win].point < dealer.values_cards_crupier and dealer.values_cards_crupier <= 21:

                    self.player_data(self.players[self.win].name, self.players[self.win].point, self.bet_back, 'losses')
                    self.win += 1

                elif self.players[self.win].point > 21 and dealer.values_cards_crupier <= 21:

                    self.player_data(self.players[self.win].name, self.players[self.win].point, self.bet_back, 'losses')
                    self.win += 1

                elif dealer.values_cards_crupier > 21:

                    self.players[self.win].chips = self.players[self.win].chips + self.reward
                    self.player_data(self.players[self.win].name, self.players[self.win].point, self.reward, 'profits')
                    self.win += 1
            else:
                self.win += 1

    def reset_game_data(self):
    
        dealer.reset_crupier_data()

        for reset in range(len(self.players)):
            self.players[reset].reset_data()
            self.players[reset].cards = dealer.get_two_cards()
            self.players[reset].point =  self.players[reset].calculate_player_point()

        
    def reset_game_data(self):
        dealer.reset_crupier_data()
        self.reset_player_data()
        dealer.crupiers_two_cards()
        self.betting_system()
        menu.delimiter = 0
        menu.iterator = 0   
        menu.menu_interaction()

    def start_new_game(self):

        self.ask_new_game = input("Do you want to play again ? write 1 for continue or 2 for exit the game : ")
        os.system("cls")

        if self.ask_new_game.isdigit():

            if int(self.ask_new_game) == 1 or int(self.ask_new_game) == 2:

                if int(self.ask_new_game) == 1:

                    self.reset_game_data()

                elif int(self.ask_new_game):
                    show.icon()
                    time.sleep(5)
                    os.sys.exit()
            else:
                print("Your entry is not valid")
                self.start_new_game()
        else:
            print("Your entry is not valid")
            self.start_new_game()

class Menu:

    def __init__(self):
        self.iterator = 0
        self.delimiter = 0
        self.cards_crupier_Value = dealer.crupier_current_hand[0].value
        self.crupier_all_cards = ""

    def menu_interaction(self):

        self.cards_crupier_Value = dealer.crupier_current_hand[0].value
        try:
            if game.players[self.delimiter].state == True:

                if len(game.players[self.delimiter].cards) == 2:

                    if game.players[self.delimiter].point == 21:

                        os.system("cls")
                        print( """
                                            ____  _            _       _            _                        
                                            | __ )| | __ _  ___| | __  | | __ _  ___| | __                    
                                            |  _ \| |/ _` |/ __| |/ _  | |/ _` |/ __| |/ /                      
                                            | |_) | | (_| | (__|   | |_| | (_| | (__|   <                     
                                            |____/|_|\__,_|\___|_|\_\___/ \__,_|\___|_|\_\ 
                            
                                    you win """+game.players[self.delimiter].name+"""
                        
                                                                                        """)

                        self.delimiter += 1
                        time.sleep(3)

                        self.menu_interaction()

                time.sleep(0.15)

                if self.iterator == 0:

                    show.opcion[0] = "|1) Stand  ◄                 |"
                    show.opcion[1] = "|2) Ask for cards            |"
                    show.opcion[2] = "|3) double the bet           |"

                    os.system("cls")
                    show.table(game.players[self.delimiter],dealer.crupier_current_hand[0],self.cards_crupier_Value)

                elif self.iterator == 1:

                    show.opcion[0] = "|1) Stand                    |"
                    show.opcion[1] = "|2) Ask for cards   ◄        |"
                    show.opcion[2] = "|3) double the bet           |"

                    os.system("cls")
                    show.table(game.players[self.delimiter],dealer.crupier_current_hand[0],self.cards_crupier_Value)

                elif self.iterator == 2:

                    show.opcion[0] = "|1) Stand                    |"
                    show.opcion[1] = "|2) Ask for cards            |"
                    show.opcion[2] = "|3) double the bet  ◄        |"

                    os.system("cls")
                    show.table(game.players[self.delimiter],dealer.crupier_current_hand[0],self.cards_crupier_Value)

                while True:

                    if self.delimiter > len(game.players)-1: 
                        break

                    if keyboard.is_pressed("down"):
                        self.iterator += 1

                        if self.iterator == 3:
                            self.iterator = 0

                        self.menu_interaction()

                    if keyboard.is_pressed("up"):
                        self.iterator -= 1

                        if self.iterator == -1:
                            self.iterator = 2

                        self.menu_interaction()

                    if keyboard.is_pressed(" "):

                        if self.iterator == 0:

                            if self.delimiter < len(game.players):
                                self.delimiter += 1

                                if game.players[self.delimiter].state == True:

                                    show.table(game.players[self.delimiter],dealer.crupier_current_hand[0],self.cards_crupier_Value)
                                    self.menu_interaction()

                                else:
                                    self.delimiter += 1
                            else:
                                break

                        if self.iterator == 1:

                            if game.players[self.delimiter].point < 21:

                                game.players[self.delimiter].cards.append(dealer.get_cards())
                                game.players[self.delimiter].point = game.players[self.delimiter].calculate_player_point()
                                show.table(game.players[self.delimiter],dealer.crupier_current_hand[0],self.cards_crupier_Value)
                                self.menu_interaction()

                            else:
                                input("You have to stand, your cards have exceeded or is equal to the score of 21")
                                self.menu_interaction()

                        if self.iterator == 2:
                            if len(game.players[self.delimiter].cards) == 2:
                                game.double_bet(self.delimiter)
                                self.menu_interaction()

                            else:
                                print("you cannot double the bet after requesting a card. you have to double the bet before asking for a card")
                                time.sleep(3)

            else:
                self.delimiter += 1
        except:
            pass        

        if self.delimiter > len(game.players)-1:
            dealer.Keep_holding_cards()
            for i in dealer.crupier_current_hand:
                self.crupier_all_cards += str(i) + " "

            show.table(game.players[0],self.crupier_all_cards,dealer.values_cards_crupier)
            self.delimiter = 0
            self.crupier_all_cards = ""
            game.calculate_final_results()
            game.start_new_game()

game = Game()
menu = Menu()
game.create_players()
game.betting_system()
menu.menu_interaction()