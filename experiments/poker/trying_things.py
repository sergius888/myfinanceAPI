# create a poker game while respecting the rules( flop river turn) - details below
# max 6 players that receive a random hand of 2 poker cards after initiating shuffle
# -> after each of them will be asked if they want to bet and how much
# each have a stack of chips of x$ -> bet, check, fold -> small big blind automatically -

# transfer pot to winner, last define best hand
import random
from random import randint
import itertools

def check_number_of_players():
    players = int(input("How many players will be playing?"))
    while players > 6:
        limited = int(input("The table is limited to 6 players, please pick again."))
        if limited <= 6:
            return limited
    else:
        return players

# print(check_number_of_players())





# suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
# cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
#
# c = list(itertools.product(suits, cards))
#
# print(c)
suits = {
    0: 'Clubs',
    1: 'Diamonds',
    2: 'Hearts',
    3: 'Spades'
}

cards = {
    0: 'Ace',
    1: '2',
    2: '3',
    3: '4',
    4: '5',
    5: '6',
    6: '7',
    7: '8',
    8: '9',
    9: '10',
    10: 'Jack',
    11: 'Queen',
    12: 'King'
}

c = list(itertools.product(cards.values(), suits.values()))
# print(c)




# #
# numar = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
# culoare = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
# #
# pairs = itertools.product(cards, suits)
#
# # filtering the pairs
# result = [pair for pair in pairs if pair[0] != pair[1]]
# print(result)




# for a, b in c:
#     forms = "{} of {}".format(b, a)
#     print(forms)



# list of strings
# string_list = [' of '.join(item) for item in c]
# print(string_list)
#
# player_1 = random.sample(string_list, 2)
# print(player_1)



data = [['QuaaludeEffect', 'something in the way']]

# tweet_name = data[0][0]
# tweet_text = data[0][1]
# tweet_message = f'{tweet_name} just tweeted: {tweet_text}'
#
# print(tweet_message)

def tweet_message(message):
    tweet_name = message[0][0]
    tweet_text = message[0][1]
    return f'{tweet_name} just tweeted: {tweet_text}'

ass = tweet_message(data)

print(ass)
# This gives us: new_list without player hands
# new_list = [fruit for fruit in string_list if fruit not in player_1]
# print(new_list)



def function(num_hand: int):
    lst_players = ["Player_1", "Player_2", "Player_3", "Player_4", "Player_5", "Player_6"]
    players_playing = lst_players[0:num_hand]
    print(players_playing)
    print(len(players_playing))

# function(5)



# for x in string_list:
#     if x





# player_1 = random.sample(string_list, 2)
# player_2 = random.sample(string_list, 2)
# player_3 = random.sample(string_list, 2)
# player_4 = random.sample(string_list, 2)
# player_5 = random.sample(string_list, 2)



# print(player_1)
# print(player_1[0])
# print(player_1[1])
#
# for x in string_list:
#     if x != player_1[0] and x != player_1[1]:
#         print(x)




# print(handout_cards(string_list))

# print(player_2)
# print(player_3)
# print(player_4)
# print(player_5)
# print(player_1[0])



# 1 to 6 players=> each get 1 random pair- each start with a stack of chips -> sb/bb automatically withdrawn from 2 players ->
# next they will be asked to input: raise ... check, fold, one by one. After last one: Flop = ..., again start with sb.. and so on
# in the end define winner hands, winner takes all (for now - )


