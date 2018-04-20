#!/usr/bin/env python

class Spam():

    def __enter__(self):
        print("Welcome to Spam!")
        return self # 'wombats'

    def __exit__(self, *stuff):
        print("Leaving Spam")

    def __str__(self):
        return 'spammy-wammy'

with Spam() as s:
    print(f"Doing some cool stuff with {s}...")


