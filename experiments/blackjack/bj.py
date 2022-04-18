import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit



class Deck:
    def __init__(self):
        self.deck = [] # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n " + card.__str__() # add each Card Object's print string
            return "The deck has:" + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0 # keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        print(values[card.rank])
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# test_deck = Deck()
# test_deck.shuffle()
# test_player = Hand()
# test_player.add_card(test_deck.deal())
# test_player.add_card(test_deck.deal())
# print(test_player.value)
#
# for card in test_player.cards:
#     print(card)


class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def take_bet(chips):
        while True:
            try:
                chips.bet = int(input("How many chips would you like to bet?"))
            except ValueError:
                print("Sorry, a bet must be an integer")
            else:
                if chips.bet > chips.total:
                    print("Sorry, your bet cannot exceed", chips.total)
                else:
                    break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing #controls while loop
    while True:
        x = input("Would you like to hit or stand? Enter 'h' or 's': ")

        if x[0].lower == 'h':
            hit(deck, hand)

        elif x[0] == 's':
            print("player stands. Dealer is playing")
            playing = False

        else:
            print("Sorry, please enter a valid response")
            continue
        break

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print("<card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand=", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand=", player.value)

def player_bust(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player, dealer):
    print("Dealer and Player tie! It's a push.")

deck = Deck()
deck.shuffle()

#Player hand
player_hand = Hand()
player_hand.add_card(deck.deal())
player_hand.add_card(deck.deal())
print(player_hand.value)

for card in player_hand.cards:
    print(card)

# Dealer hand
dealer_hand = Hand()
dealer_hand.add_card(deck.deal())
dealer_hand.add_card(deck.deal())
print(dealer_hand.value)
for card in dealer_hand.cards:
    print(card)

# player_chips = 100

show_some(player_hand, dealer_hand)

while playing:
    hit_or_stand(deck, player_hand)
    show_some(player_hand, dealer_hand)

    if player_hand.value > 21:
        player_bust(player_hand, dealer_hand, player_chips)
        break

if player_hand.value <= 21:
    while dealer_hand.value < 17:
        hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)

    print("\nPlayer's winings stand at", player_chips.total)

    new_game = input ("Would you like to play another hand? Enter 'y' or 'n': ")

    if new_game[0].lower() == 'y':
        playing = True
    else:
        print("Thanks for playing!")

