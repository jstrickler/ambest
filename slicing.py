#!/usr/bin/env python
from copy import deepcopy

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

print(fruits[:8])
print(fruits[-5:])

f1 = fruits
f1.append('durian')
print(fruits)
f2 = list(fruits)
f3 = fruits[::]

f4 = deepcopy(fruits)  # true copy

thing = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
]

t1 = thing
t1[0].append('x')
print(thing)

t2 = list(thing)
print(id(thing), id(t1), id(t2))
t2[0].append('y')
print(thing)
t3 = deepcopy(thing)
t3[0].append('z')
print(thing)
print(t3)

i = ['wombat', 'wallaby', 'javalina']
j = ['a', 'b', 'c']
k = [100, 200, 300]

print(list(zip(i, j, k)))




