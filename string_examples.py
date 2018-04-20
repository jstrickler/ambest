#!/usr/bin/env python


s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''

print("I'm your huckleberry")

print('The "book" is over there')


print('''I'm "your" huckleberry''')

query = """
select *
from mutual_of_omaha
where
date = '2014-04'
"""

print("hello\ngoodbye\nhello again")


print(r'spam\n')

cave_man = 'Barney Rubble'
print(cave_man)
print(cave_man.upper())
print(cave_man.index('Bar'))
print(cave_man.count('b'))
print(len(cave_man))
print(cave_man.startswith('Foo'))
print(cave_man.startswith('Bar'))
print('Poke' in cave_man)
print('Rub' in cave_man)

s = '      All my exes live in Texas       '
print('|' + s.lstrip() + '|')
print('|' + s.rstrip() + '|')
print('|' + s.strip() + '|')
print('|' + s + '|')
print()


s = 'xyxxxxyyyxyyxxAll my exes live in Texasxyxyyxyxyxxxxxxxxxxxxxxx'
print('|' + s.lstrip('xy') + '|')
print('|' + s.rstrip('xy') + '|')
print('|' + s.strip('xy') + '|')
print()

