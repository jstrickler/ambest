#!/usr/bin/env python

def main():
    x = 5
    other_value = spam(x)
    print("in main: other_value is", other_value)

def spam(value):
    y = 10
    print("in spam(): value is", value)
    return y

if __name__ == '__main__':
    main()
