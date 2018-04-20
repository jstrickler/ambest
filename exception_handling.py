#!/usr/bin/env python
import sys

x = 23.6

values = 1.2, 8.9, 4.6, 5, 0, 9.7, '123', 2.7

for v in values:
    try:
        result = x / v
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print(err)
        # sys.exit(1)
    except Exception as err:
        print("HUH.", err)
    else:
        print(result)
    finally:
        print(f'DONE with {v}')

class MyException(Exception): pass

def shout():
    print("OUCH!")
    raise MyException("You're killing me!", 5, 'Wombat')



print("one")
try:
    shout()
except MyException as err:
    print(err.args[0], err.args[1])
print("two")


