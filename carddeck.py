#!/usr/bin/env python
import random

class CardDeck():
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer):
        self._cards = []
        self.dealer = dealer
        self._create_deck()

    def _create_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = f'{rank}-{suit}'
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    @property  # getter property
    def dealer(self):
        return self._dealer

    # dealer = property(dealer)

    @dealer.setter # setter property
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @classmethod
    def get_suits(cls):
        return cls.SUITS

    @staticmethod
    def spam():
        print("Hi. I'm spam")

    # d1 + d2     d1.__add__(d2)

    def __len__(self):  # len(x) <=> x.__len__()
        return len(self._cards)


    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f'{my_name}({self.dealer}, {len(self)})'

    def __add__(self, other):
        tmp = CardDeck(self.dealer)
        tmp._cards = self.cards + other.cards
        return tmp

if __name__ == '__main__':
    d = CardDeck("Amelia")
    print(d)
    print(len(d))

    d2 = CardDeck("Boris")

    x = d + d2
    print(x)
    print(len(x))
