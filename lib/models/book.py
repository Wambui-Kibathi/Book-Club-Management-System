from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from . import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    genre = Column(String)
    summary = Column(Text)
    publication_year = Column(Integer)

    def __repr__(self):
        return f"<Book(title={self.title}, author={self.author})>"