#!/usr/bin/env python
from potus_amb import get_info, get_oldest, get_youngest, NUM_TERMS

print('PRESIDENT 1:')
for k, v in get_info(1).items():
    print(k, v)
print()

print('PRESIDENT {}:'.format(NUM_TERMS))
for k, v in get_info(NUM_TERMS).items():
    print(k, v)
print()

oldster = get_oldest()
print("Oldest is", oldster["firstname"], oldster["lastname"])

youngster = get_youngest()
print("Youngest is", youngster["firstname"], youngster["lastname"])
