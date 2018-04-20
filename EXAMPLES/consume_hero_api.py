#!/usr/bin/env python
#
import requests
from pprint import pprint

def print_if_ok(response, message):
    print("** {} **".format(message))
    print(response.status_code)
    if response.status_code == requests.codes.OK:
        pprint(response.json())
    else:
        print("Oops:") #, response.status_code)

response = requests.get('http://localhost:8000/api/v1/herolist')
print_if_ok(response, 'all heroes')
print('-' * 60)

response = requests.get('http://localhost:8000/api/v1/hero/1')
print_if_ok(response, 'hero #1')
print('-' * 60)

response = requests.get('http://localhost:8000/api/v1/hero/2')
print_if_ok(response, 'hero #2')

print('=' * 60)
response = requests.get('http://localhost:8000/api/v1/enemylist')
print_if_ok(response, 'all enemies')

print('-' * 60)
response = requests.get('http://localhost:8000/api/v1/enemy/1')
print_if_ok(response, 'enemy #1')

print('-' * 60)
response = requests.get('http://localhost:8000/api/v1/enemy/5')
print_if_ok(response, 'enemy #5')
