from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from lib.models import Base

club_members = Table(
    "club_members",
    Base.metadata,
    Column("club_id", Integer, ForeignKey("clubs.id")),
    Column("member_id", Integer, ForeignKey("members.id"))
)

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    clubs = relationship("Club", secondary="club_members", back_populates="members")

    def __repr__(self):
        return f"<Member(id={self.id}, name={self.name}, email={self.email})>"
