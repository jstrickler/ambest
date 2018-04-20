#!/usr/bin/env python

print("Anyone for Mahjong?")
for i in range(0x1F000, 0x1f02C):   # <4>
    print(chr(i), end=' ')
print('---')
print("\U0001F000")
