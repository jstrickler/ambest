#!/usr/bin/env python
from potus import get_info

for i in range(1, 46):
    print('PRESIDENT {}:'.format(i))
    for field, value in get_info(i).items():
        print(field, value)
    print()

