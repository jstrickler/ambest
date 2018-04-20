#!/usr/bin/env python

list1 = list() # <1>
list2 = ['apple', 'banana', 'mango']  # <2>
list3 = []  # <3>
list4 = 'apple banana mango'.split()  # <4>

print("list1:", list1)
print("list2:", list2)
print("list3:", list3)
print("list4:", list4)

print("list2[0]:", list2[0])   # <5>
print("list4[2]:", list4[2])   # <6>

print("list4[-1]:", list4[-1]) # <7>

fruits = list4

fruits.append('kiwi')
print(fruits, '\n')

x = ['cherry', 'lime', 'papaya']
fruits.extend(x)
print(fruits, '\n')

fruits.insert(0, 'guava')
fruits.insert(3, 'pomegranate')
print(fruits, '\n')

fruits[3] = 'durian'

print(fruits, '\n')

del fruits[3]
print(fruits, '\n')

fruits.remove('lime')
print(fruits, '\n')

f = fruits.pop()
print(f)
print(fruits, '\n')

f = fruits.pop(4)
print(f)
print(fruits, '\n')

