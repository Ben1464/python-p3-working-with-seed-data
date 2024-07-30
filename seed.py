# lib/seed.py

from models import Game
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from faker import Faker
import random

# Set up the database
engine = create_engine('sqlite:///your_database.db')  # Update with your database URL
Session = sessionmaker(bind=engine)
session = Session()

# Clear old data
session.query(Game).delete()
session.commit()

# Add new data
print("Seeding games...")
fake = Faker()

games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(0, 60)
    )
    for i in range(50)
]

session.add_all(games)
session.commit()
print("Seeding completed.")
