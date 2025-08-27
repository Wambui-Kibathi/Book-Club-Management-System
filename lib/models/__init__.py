from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base   

Base = declarative_base()

engine = create_engine("sqlite:///book_club.db")
Session = sessionmaker(bind=engine)
session = Session()

def create_tables():
    Base.metadata.create_all(engine)

