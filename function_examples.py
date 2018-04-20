#!/usr/bin/env python


def get_message():
    return "Hello, AMBest world"

# m = get_message()
# print(m)

def print_hello():
    m = get_message()
    print(m)

print_hello()

def greet(greeting, target='world'):
    print(f"{greeting}, {target}")

greet('hello', 'world')
greet("Hi", 'Mom')
greet('Howdy')

def greet_many(greeting, *args):
    for target in args:
        print(f"{greeting}, {target}")


greet_many('hello', 'world')
greet_many("Hi", 'Mom')
greet_many('Howdy')
greet_many("What's happenin'", 'Mom', 'Dad', 'Cousin Itt')


def process(*, file_type, file_name):
    print('processing ->', file_type, file_name)

process(file_type='pdf', file_name='spam.pdf')
process(file_name='foo.barf', file_type='unknown')


def config(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

config(user='bob', folder='/users/bob/mystuff')

def generic(*args, **kwargs):
    pass

def simple(x, y):
    return x ** y

print(simple(5, 8))
print(simple(1.2, 14))

def less_simple(*, x, y):
    return x ** y

print(less_simple(x=5, y=8))
print(less_simple(y=1.2, x=14))


print(simple(y=9, x=11))
