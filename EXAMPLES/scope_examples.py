#!/usr/bin/env python

x = 42 # <1>

def function_a():
    y = 5  # <2>

    def function_b():
        z = 32  # <3>
        print("function_b(): z is", z)      # <4>
        print("function_b(): y is", y)      # <5>
        print("function_b(): x is", x)      # <6>
        print("function_b(): type(x) is", type(x)) # <7>

    return function_b;

f = function_a()   # <8>
f() # <9>
