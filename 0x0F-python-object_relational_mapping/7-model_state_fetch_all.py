#!/usr/bin/python3
""" a script that lists all State objects from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()
all_states = session.query(State).order_by(State.id).all()

for state in all_states:
    print("{}: {}".format(state.id, state.name))

session.close()
