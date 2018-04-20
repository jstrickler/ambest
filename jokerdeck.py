#!/usr/bin/env python

from carddeck import CardDeck

class Animal():
    def shout(self):
        print("wahooooooo")

class Dog(Animal):
    def bark(self):
        print("Woof woof")

class JokerDeck(CardDeck, Dog):

    def _create_deck(self):
        super()._create_deck()
        self._cards.append("Joker 1")
        self._cards.append("Joker 2")

