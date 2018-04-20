#!/usr/bin/env python

from sqlalchemy import create_engine, select, Table, MetaData, bindparam

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

s = pres.select(pres.c.party == bindparam('party'))

results = s.execute(party='Republican')
for row in results:
    print("{0:28s} {1.year} {2}".format(row.firstname + ' ' + row.lastname, row.termstart, row.birthstate))

print("---------")
results = s.execute(party='Whig')
for row in results:
    print("{0:28s} {1.year} {2}".format(row.firstname + ' ' + row.lastname, row.termstart, row.birthstate))

print("---------")
results = s.execute(party='Federalist')
for row in results:
    print("{0:28s} {1.year} {2}".format(row.firstname + ' ' + row.lastname, row.termstart, row.birthstate))
