#!/usr/bin/env python

from singledispatch import singledispatch


@singledispatch
def base(x):
    return None


@base.register(int)
def b_int(x):
    print("got an int")


@base.register(float)
def b_float(x):
    print("got a float")


base(1)
base(1.2)

