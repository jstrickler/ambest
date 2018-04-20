#!/usr/bin/env python
from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData

engine = create_engine(
    'sqlite:///../DATA/presidents.db',
    echo=False
)

metadata = MetaData(bind=engine)

conn = engine.connect()

pres = Table(
    'presidents',
    metadata,
    autoload=True
)

# find Lincoln
s = pres.select(pres.c.termnum == 16)

results = s.execute()
for row in results:
    print(row.firstname, row.lastname, row.party)

print('-------------')
s = pres.select(pres.c.party == 'Republican')

for row in s.execute():
    print("{0:28s} {1.year} {2}".format(
        row.firstname + ' ' + row.lastname,
        row.termstart,
        row.birthstate
    ))
