from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Club(Base):
    __tablename__ = "clubs"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    genre = Column(String)
    members = relationship("Member", secondary="club_members", back_populates="clubs")
    meetings = relationship("Meeting", back_populates="club")

    def __repr__(self):
        return f"<Club(id={self.id}, name='{self.name}', genre='{self.genre}')>"
