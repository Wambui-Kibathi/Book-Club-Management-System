from models import create_tables, session
from models.book import Book
from models.member import Member
from models.club import Club
from models.meeting import Meeting

if __name__ == "__main__":
    create_tables()
    print("Data created successfully!")