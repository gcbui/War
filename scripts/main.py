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
    shuffled_deck = []
    for i in range(52):
        random_select = random.randint(0,len(temp_deck))
        shuffled_deck.append(temp_deck[random_select])
        del temp_deck[random_select]
    return shuffled_deck

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
            if 1 < num_of_players and num_of_players < 5:  
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
    return players    


def split_deck(players,deck):
    for num in range(len(deck)):
        players[num % len(players)].cards.append(deck[num])
    return players

def player_that_wins(players):
    pass
    #.pop(0)

    

