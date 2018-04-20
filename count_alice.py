#!/usr/bin/env python


count = 0

with open('DATA/alice.txt') as alice_in:
    for line in alice_in:
        if 'Alice' in line:
            count += 1

print(f"Alice occurred on {count} lines")
