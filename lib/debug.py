from lib.models import create_tables, session
from lib.models.book import Book
from lib.models.member import Member
from lib.models.club import Club
from lib.models.meeting import Meeting
from helpers import generate_sample_data

if __name__ == "__main__":
    create_tables()
    generate_sample_data()
    print("Sample data created successfully!")