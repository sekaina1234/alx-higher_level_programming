#!/usr/bin/python3
"""Add the State object 'Louisiana' to the database
hbtn_0e_6_usa and print its states.id.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>"
              .format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the SQLAlchemy engine and bind it to the specified database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the 'Louisiana' state and add it to the database
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    # Print the newly created state's states.id
    print(new_state.id)

    # Close the session
    session.close()
