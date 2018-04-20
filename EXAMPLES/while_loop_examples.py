#!/usr/bin/env python

while True:      # <1>
    name = input("Enter a name (or q to quit): ")
    if name == '':
        continue   # <2>
    if name.lower() == 'q':
        print("goodbye!")
        break   # <3>
    print("welcome,", name)

