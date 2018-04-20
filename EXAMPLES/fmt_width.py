#!/usr/bin/env python

name = 'Ann Elk'
value = 10000
airspeed = 22.347
# note: [] are used to show field widths
print('[{0:s}]'.format(name))     # <1>
print('[{0:10s}]'.format(name))   # <2>
print('[{0:3s}]'.format(name))    # <3>
print('[{0:3.3s}]'.format(name))  # <4>
print()
print('[{0:8d}]'.format(value))       # <5>
print('[{0:8f}]'.format(value))       # <6>
print('[{0:8f}]'.format(airspeed))    # <7>
print('[{0:.2f}]'.format(airspeed))   # <8>
print('[{0:8.3f}]'.format(airspeed))  # <9>
