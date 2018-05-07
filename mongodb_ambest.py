#!/usr/bin/env python
import re
from pymongo import MongoClient
from bson import json_util
from pprint import pprint

DB_NAME = 'ambest'

mc = MongoClient()

try:
    mc.drop_database(DB_NAME)
except:
    pass

db = mc[DB_NAME]

companies = db.companies

with open('MongoDB document example.txt') as amb_in:
    data = json_util.loads(amb_in.read())

companies.insert_many(data)

result = companies.find_one()

pprint(result)
print('-' * 60)

print(result['rating_assessment'])
print('-' * 60)

result = companies.find_one({'amb_number': 5902})
print(result)
print('-' * 60)
print(result['analyst'][0]['email'])
print('-' * 60)

result = companies.find_one({'report_text.operating_performance': 'splendid'})
print(result["company_name"])
print('-' * 60)

