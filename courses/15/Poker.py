# create a class which represent a deck of cards (poker)
# we have a method to receive a specified number of cards
# we have a method to put all the cards back in the deck
import random


class PockerDeck:
    def __init__(self):
        self.put_cards_back()

    def put_cards_back(self):
        self.cards = {
            "trefla": [2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "q", "k", "a"],
            "inima rosie": [2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "q", "k", "a"],
            "romb": [2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "q", "k", "a"],
            "inima neagra": [2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "q", "k", "a"],
        }

    def get_cards(self, number_of_cards: int):
        cards = []
        for i in range(0, number_of_cards):
            extracted_card = self.__extract_one_card()
            cards.append(extracted_card)
        return cards

    def __extract_one_card(self):
        # TODO optimize, remove duplicate code
        random_colour = random.choice(["trefla", "inima rosie", "romb", "inima neagra"])
        random_number = random.choice(self.cards[random_colour])
        self.cards[random_colour].remove(random_number)
        return random_colour, random_number


if __name__ == "__main__":
    deck = PockerDeck()
    cards = deck.get_cards(5)
    print(cards)
    cards = deck.get_cards(2)
    print(cards)
    print(deck.cards)
    deck.put_cards_back()
    print(deck.cards)