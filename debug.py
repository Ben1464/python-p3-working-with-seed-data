# lib/debug.py

from models import Game
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Set up the database
engine = create_engine('sqlite:///your_database.db')  # Update with your database URL
Session = sessionmaker(bind=engine)
session = Session()

import ipdb; ipdb.set_trace()
