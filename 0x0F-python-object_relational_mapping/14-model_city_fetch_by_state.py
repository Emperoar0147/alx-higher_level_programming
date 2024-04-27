#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and print them
    cities = session.query(State, City).join(City).order_by(City.id).all()
    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
