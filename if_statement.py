#!/usr/bin/env python
"""
Simple examples of the if statement
"""

def spam():
    """
    The spam function.

    :return: value as int
    """
    return 42


VALUE = 65

if VALUE > 50:
    print('wombat')
    print('wallaby')
elif VALUE > 25:
    print("kookaburra")
    print("Tasmanian devil")
else:
    print("blue-ringed octopus")

print("spam", "spam", "spam", "spam", "spam", "spam", "spam",
      "spam", "spam", "spam", "spam", "spam", "spam", "spam",
      "spam", "spam", "spam", "spam", "spam", "spam", "spam",
      "spam", )


#  False None  0 0.0   ""  [] () {} set()

#   == !=  is  >  <  >= <=

#  and or not

x = 5
if x is None:
    print("OH")


#   A?B:C

# flag =  B if A else C











