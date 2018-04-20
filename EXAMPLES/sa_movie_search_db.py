#!/usr/bin/env python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sa_movie_models import Movie, Director

def main():
    session = setup()
    do_query_1(session)
    print()
    do_query_2(session)
    session.close()

def setup():
    engine = create_engine(
        'sqlite:///../DATA/movies.db',
        echo=False
    )
    SESSION = sessionmaker(bind=engine)
    return SESSION()

def do_query_1(session):
    for director in session.query(Director):
        if director.first_name == 'Steven':
            director.first_name = 'Bob'
        print(director.first_name, director.last_name)
        for movie in director.movies:
            print("\t{0} ({1})".format(movie.movie_name, movie.year))

def do_query_2(session):
    movie_name_query = 'M*A*S*H'

    # select * from Movie where movie_name  = 'M*A*S*H'
    for result in session.query(Movie).filter(Movie.movie_name==movie_name_query):
        print("{0} was directed by {1} {2}".format(
            movie_name_query,
            result.person.first_name,
            result.person.last_name,
        ))

if __name__ == '__main__':
    main()
