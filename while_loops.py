#!/usr/bin/env python

i = 0
while i < 5:
    print(i)
    i += 1
print()

while True:
    user_name = input("What is your name? ")
    if user_name == '':
        continue
    if user_name == 'q':
        break
    print("Welcome", user_name)

