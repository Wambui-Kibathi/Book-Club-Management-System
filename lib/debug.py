from .models import create_tables, session
from .models.book import Book
from .models.member import Member
from .models.club import Club
from .models.meeting import Meeting
from datetime import date

# Sample data constants
SAMPLE_BOOKS = [
    ("To Kill a Mockingbird", "Harper Lee", "Fiction", "A story of racial injustice", 1960),
    ("1984", "George Orwell", "Dystopian", "A dystopian social science fiction novel", 1949),
    ("Pride and Prejudice", "Jane Austen", "Romance", "A romantic novel of manners", 1813)
]

SAMPLE_MEMBERS = [
    ("Alice Johnson", "alice@email.com"),
    ("Bob Smith", "bob@email.com"),
    ("Carol Williams", "carol@email.com")
]

SAMPLE_CLUBS = [
    ("Classic Literature Club", "Discussing timeless classics"),
    ("Sci-Fi Enthusiasts", "Exploring science fiction worlds")
]

def create_sample_data():
    """Create sample data for testing"""
    create_tables()
    
    # Create and add books
    books = [Book(title=title, author=author, genre=genre, summary=summary, publication_year=year) 
             for title, author, genre, summary, year in SAMPLE_BOOKS]
    
    # Create and add members
    members = [Member(name=name, email=email) for name, email in SAMPLE_MEMBERS]
    
    # Create and add clubs
    clubs = [Club(name=name, description=desc) for name, desc in SAMPLE_CLUBS]
    
    session.add_all(books + members + clubs)
    session.commit()
    
    # Add members to clubs
    clubs[0].members.extend([members[0], members[1]])
    clubs[1].members.extend([members[1], members[2]])
    
    # Create meetings
    meetings = [
        Meeting(date=date(2023, 10, 15), location="Central Library", club_id=clubs[0].id, book_id=books[0].id),
        Meeting(date=date(2023, 11, 5), location="Coffee Shop Downtown", club_id=clubs[1].id, book_id=books[1].id)
    ]
    
    session.add_all(meetings)
    session.commit()
    print("Sample data created successfully!")

if __name__ == "__main__":
    create_sample_data()