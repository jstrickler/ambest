#!/usr/bin/env python

fruits = ['watermelon', 'apple', 'mango', 'kiwi', 'apricot', 'lemon', 'guava']

# NEW_LIST = [EXPR for VAR ... in ITERABLE if CONDITION ...]


ufruits = [fruit.upper() for fruit in fruits]        # <1>
print("ufruits:", ufruits)

ufruits = []
for fruit in fruits:
    ufruits.append(fruit.upper())




afruits = [fruit.title() for fruit in fruits if fruit.startswith('a')]  # <2>

print("ufruits:", ufruits)
print("afruits:", afruits)
print()

values = [2, 42, 18, 39.7, 92, '14', "boom", ['a', 'b', 'c']]

doubles = [v * 2 for v in values]   # <3>

print("doubles:", doubles, '\n')

nums = [x for x in values if isinstance(x, int)]   # <4>
print(nums, '\n')

dirty_strings = ['   Gronk    ', 'PULABA       ', '        floog']

clean = [d.strip().lower() for d in dirty_strings]
for c in clean:
    print(">{}<".format(c), end=' ')
print("\n")

suits = 'Clubs', 'Diamonds', 'Hearts', 'Spades'
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

deck = [(rank, suit) for suit in suits for rank in ranks]   # <5>

for rank, suit in deck:
    print("{}-{}".format(rank, suit))
