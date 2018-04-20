#!/usr/bin/env python

person = 'Bob'
value = 488
bigvalue = 3735928559
result = 234.5617282027

print('{0:s}'.format(person))    # <1>
print('{name:s}'.format(name=person))    # <2>
print('{0:d}'.format(value))    # <3>
print('{0:b}'.format(value))    # <4>
print('{0:o}'.format(value))    # <5>
print('{0:x}'.format(value))    # <6>
print('{0:X}'.format(bigvalue))    # <7>
print('{0:f}'.format(result))    # <8>
print('{0:.2f}'.format(result))    # <9>
