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
        self.icono_for_player = ['☠', '☢', '☣' ,'♞','☯', '♪', '❆','✟']

    def select_name(self,iterator):
        global name_of_player

        name_of_player = input("Entry name of player"+str(iterator+1)+" ► ")
        os.system("cls")

        if len(name_of_player) >= 10:

            print("error the length of your name is too long test with a name less than 10 digits")
            self.select_name(iterator)

        else:
            return name_of_player

    def select_icon(self,iterator):
        number_icon = 1
        
        for icons in self.icono_for_player:

            print(number_icon,icons)
            number_icon += 1
        
        ask_for_icon = input("insert a number of you icon ► ")
        os.system("cls")

        if ask_for_icon.isdigit():

            if int(ask_for_icon) > 0 and int(ask_for_icon) < 8:

                self.players.append(Player(name_of_player,self.icono_for_player[int(ask_for_icon)],True,10000,dealer.Player_curret_hand[1],dealer.Player_curret_hand[0],0,False))
                dealer.Player_curret_hand = [[]]
                
            else:
                os.system("cls")
                input("error the option you have inserted is not valid test with a number from 1 to 8 press enter for continue")
                self.select_icon(iterator)
        else:
            input("Error the option you have inserted is not valid test with a number from 1 to 8 press enter for continue")
            self.select_icon(iterator)

    def generate_players(self):

        print("The limit of players that you can play at the same time are 4 ")
        self.limit_players = input("Entry number of players ► ")

        if self.limit_players.isdigit():

            if int(self.limit_players) <= 4 and int(self.limit_players) > 0:

                os.system("cls")

                for delimiter in range(int(self.limit_players)):

                    dealer.get_two_cards()
                    self.select_name(delimiter)

                    print("Select you icon")
                    self.select_icon(delimiter)

            else:
                os.system("cls")
                input("Error entering the number of players, try a number from 1 to 4 enter to continue...")
                self.generate_players()

        else:
            os.system("cls")
            input("Error entering the number of players, try a number from 1 to 4 enter to continue...")
            self.generate_players()


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

    def winner_data(self, player, point, reward):

        print("winner")
        print('dealer points : ', dealer.values_cards_crupier)
        print("Player: ", player)
        print("Card scoring: ", point)
        print("Profits: ", reward)
        input("Enter to continue \n")

    def loser_data(self,player, point, losses):

        print("lost")
        print('dealer points : ',dealer.values_cards_crupier)
        print("Player: ", player)
        print("Card scoring: ", point)
        print("losses: ", losses )
        input("Enter to continue \n")

    def tie_data(self, player, point, reward):

        print("Tie")
        print('dealer points : ', dealer.values_cards_crupier)
        print("Player: ", player)
        print("Card scoring: ", point)
        print("Profits: ", reward)
        input("Enter to continue \n")

    def calculate_final_results(self):

        self.win = 0

        while self.win < len(self.players):

            if self.players[self.win].state == True:

                self.reward = self.players[self.win].bet * 2
                self.bet_back = self.players[self.win].bet

                if self.players[self.win].point > dealer.values_cards_crupier and self.players[self.win].point <= 21:
                    
                    self.players[self.win].chips = self.players[self.win].chips + self.reward
                    self.winner_data(self.players[self.win].name, self.players[self.win].point, self.reward)
                    self.win += 1

                elif self.players[self.win].point == dealer.values_cards_crupier and self.players[self.win].point <= 21:

                    self.players[self.win].chips = self.players[self.win].chips + self.bet_back
                    self.tie_data(self.players[self.win].name, self.players[self.win].point, self.reward)
                    self.win += 1

                elif self.players[self.win].point < dealer.values_cards_crupier and dealer.values_cards_crupier <= 21:

                    self.loser_data(self.players[self.win].name, self.players[self.win].point, self.bet_back)
                    self.win += 1

                elif self.players[self.win].point > 21 and dealer.values_cards_crupier <= 21:

                    self.loser_data(self.players[self.win].name, self.players[self.win].point, self.bet_back)
                    self.win += 1

                elif dealer.values_cards_crupier > 21:

                    self.players[self.win].chips = self.players[self.win].chips + self.reward
                    self.winner_data(self.players[self.win].name, self.players[self.win].point, self.reward)
                    self.win += 1
            else:
                self.win += 1

    def reset_dealer_data(self):

        dealer.crupier_curret_hand = []
        dealer.values_cards_crupier = 0
        dealer.Player_curret_hand = [[]]
        dealer.deck_of_cards.generator_of_cards()
    
    def reset_player_data(self):

        for reset in range(len(self.players)):
    
            if self.players[reset].state == True:

                self.players[reset].cards = ''
                self.players[reset].point = ""
                self.players[reset].bet = 0
                self.players[reset].bet_state = False

                dealer.get_two_cards()

                self.players[reset].cards = dealer.Player_curret_hand[0]
                self.players[reset].point = dealer.Player_curret_hand[1]
                dealer.Player_curret_hand = [[]]

    def reset_game_data(self):
        
        self.reset_dealer_data()
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
        self.cards_crupier_Value = dealer.card_value.value[dealer.crupier_curret_hand[0]]
        self.crupier_all_cards = ""

    def menu_interaction(self):
        self.cards_crupier_Value = dealer.card_value.value[dealer.crupier_curret_hand[0]]
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
                    show.table(game.players[self.delimiter],dealer.crupier_curret_hand[0],self.cards_crupier_Value)

                elif self.iterator == 1:

                    show.opcion[0] = "|1) Stand                    |"
                    show.opcion[1] = "|2) Ask for cards   ◄        |"
                    show.opcion[2] = "|3) double the bet           |"

                    os.system("cls")
                    show.table(game.players[self.delimiter],dealer.crupier_curret_hand[0],self.cards_crupier_Value)

                elif self.iterator == 2:

                    show.opcion[0] = "|1) Stand                    |"
                    show.opcion[1] = "|2) Ask for cards            |"
                    show.opcion[2] = "|3) double the bet  ◄        |"

                    os.system("cls")
                    show.table(game.players[self.delimiter],dealer.crupier_curret_hand[0],self.cards_crupier_Value)

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

                                    show.table(game.players[self.delimiter],dealer.crupier_curret_hand[0],self.cards_crupier_Value)
                                    self.menu_interaction()

                                else:
                                    self.delimiter += 1
                            else:
                                break

                        if self.iterator == 1:

                            if game.players[self.delimiter].point < 21:

                                game.players[self.delimiter].point = dealer.get_card(game.players[self.delimiter].cards)
                                show.table(game.players[self.delimiter],dealer.crupier_curret_hand[0],self.cards_crupier_Value)
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
            for i in dealer.crupier_curret_hand:
                self.crupier_all_cards += str(i) + " "

            show.table(game.players[0],self.crupier_all_cards,dealer.values_cards_crupier)
            self.delimiter = 0
            self.crupier_all_cards = ""
            game.calculate_final_results()
            game.start_new_game()

game = Game()
menu = Menu()
game.generate_players()
game.betting_system()
menu.menu_interaction()