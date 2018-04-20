#!/usr/bin/env python

with open("../DATA/tyger.txt") as tyger_in:  # <1>
    for raw_line in tyger_in:  # <2>
        line = raw_line.rstrip('\n\r')
        if 'hammer' in line:
            print(line)  # <3>
