#!/usr/bin/env python
import types

from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck('Andrew')
print(d1)

print(d1.dealer)

print(d1.dealer.upper())
print(d1.cards)

d1.shuffle()
print(d1.cards)
hand = []
for i in range(5):
    hand.append(d1.draw())
print("hand:", hand)

try:
    d1.dealer = 1234
except Exception as err:
    print(err)
else:
    print(d1.dealer)

d1.dealer="Kathy"

print(d1.dealer)

print(d1.get_suits())

print(CardDeck.get_suits())

j1 = JokerDeck('Bob')

j1.shuffle()

print(j1.cards)
j1.bark()

print(CardDeck.mro())
print(JokerDeck.mro())

j1.shout()

print(dir(j1))

funcs = [
    x for x in dir(j1)
    if callable(getattr(j1,x))
    if not x.startswith('_')
]
print(funcs)

print(d1)
print(j1)
