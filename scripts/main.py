from ctypes.wintypes import MAX_PATH
from importlib.machinery import WindowsRegistryFinder
from tkinter import N
import random


class Player:
    name = "no_name"
    number = 0
    cards = []

class Card:
    number = 0
    suit = "no_suit"

global_deck = []
players = []
max_players = 4 
current_players = []

def init_deck():
    suits = ["HEARTS","DIAMONDS","SPADES","CLUBS"]    
    for suit in suits:
        for num in range(1,14):
            card = Card()
            card.number = num
            card.suit = suit
            global_deck.append(card)
    return global_deck

def shuffle_deck():
    temp_deck = global_deck
    length_of_temp_deck = len(temp_deck)
    shuffled_deck = []
    #for i in range(len(temp_deck)):
        #print (str(temp_deck[i].number) + temp_deck[i].suit)
    for i in range(length_of_temp_deck):
        random_select = random.randint(0,len(temp_deck)-1)
        shuffled_deck.append(temp_deck[random_select])
        #print(str(shuffled_deck[len(shuffled_deck)-1].number))
        del temp_deck[random_select]
    print(len(shuffled_deck))

def create_players():
    wrong_selection = "default"
    num_of_players = 0
    while wrong_selection == "default": 
        wrong_selection = input("Select number of players (2-4): ")
        if wrong_selection == "":
            print("Select valid number of players. Retry! ")
            wrong_selection = "default"
        elif wrong_selection.isdigit() == False:
            print("Select a valid NUMBER of players. Retry! ")
            wrong_selection = "default"
        elif len(wrong_selection) >= 1:
            num_of_players = int(wrong_selection[0])
            if 1 < num_of_players and num_of_players < (max_players+1):  
                wrong_selection = "correct"  
                for num in range(num_of_players):
                    player = Player()
                    player.number = num+1
                    players.append(player)
            else:
                wrong_selection = "default"
        else:
            print("Select valid number of players. Retry! ")
            wrong_selection = "default"
    current_players = players
    return players    


def split_deck(players,deck):
    for num in range(len(deck)):
        players[num % len(players)].cards.append(deck[num])
    return players

#players = [player object with a .number and .cards ,]
def play_a_turn(players):
    print ("Player # "+player.number+"'s card is equal to "+player.cards[0].number+" of "+player.cards[0].suit)

def did_player_win(players): #return player that won and returns True or False if player los

def player_that_wins(players):
    did_player_win = False
    while did_player_win == False:
        for i in range(len(players)):
            if len(players[i].cards) == 0:    #remove player because they lost
                players.remove(players[i])       
            elif len(players[i].cards) == 52:
                print("PLAYER NUMBER " +players[i].number + " WINS!")
                did_player_win == True
            else:
                show_hand(players[i])
        



        while len(players[i].cards) != 52:
            
                current_players = 
        
    
    max_card = 0
    
    for player in players:
        if player.card.number > max_card:
            max_card = player.card.number
            winner = player
    

