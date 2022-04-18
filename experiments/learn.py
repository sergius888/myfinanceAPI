
class Cards:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])



card = Cards(0, 12)
card2 = Cards(0, 14)

print(card.suit>card2.suit)

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Cards(suit, rank))

    def print_deck(self):
        for card in self.cards:
            print(card)

    # def __str__(self):
    #     s = ""
    #     for i in range(len(self.cards)):
    #         s = s + " " * i + str(self.cards[i]) + "\n"
    #     return s

    def shuffle(self):
        import random
        rng = random.Random()        # create a  random generator
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = rng.randrange(i, num_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]



deck = Deck()

print(deck.shuffle())















