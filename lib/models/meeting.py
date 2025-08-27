from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True)
    club_id = Column(Integer, ForeignKey("clubs.id"), nullable=False)
    date = Column(Date, nullable=False)
    location = Column(String)
    notes = Column(String)
    book_id = Column(Integer, ForeignKey("books.id"))

    club = relationship("Club", back_populates="meetings")
    book = relationship("Book")

    def __repr__(self):
        return f"<Meeting(id={self.id}, date='{self.date}', location='{self.location}')>"
