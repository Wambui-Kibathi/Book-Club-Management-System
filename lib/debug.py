from .models import create_tables, session
from .models.book import Book
from .models.member import Member
from .models.club import Club
from .models.meeting import Meeting
from datetime import date

def create_sample_data():
    """Create simple sample data without Faker"""
    create_tables()
    
    # Create sample books
    books = [
        Book(title="To Kill a Mockingbird", author="Harper Lee", genre="Fiction", 
             summary="A story of racial injustice", publication_year=1960),
        Book(title="1984", author="George Orwell", genre="Dystopian", 
             summary="A dystopian social science fiction novel", publication_year=1949),
        Book(title="Pride and Prejudice", author="Jane Austen", genre="Romance", 
             summary="A romantic novel of manners", publication_year=1813)
    ]
    
    # Create sample members
    members = [
        Member(name="Alice Johnson", email="alice@email.com"),
        Member(name="Bob Smith", email="bob@email.com"),
        Member(name="Carol Williams", email="carol@email.com")
    ]
    
    # Create sample clubs
    clubs = [
        Club(name="Classic Literature Club", description="Discussing timeless classics"),
        Club(name="Sci-Fi Enthusiasts", description="Exploring science fiction worlds")
    ]
    
    # Add all to session and commit
    session.add_all(books)
    session.add_all(members)
    session.add_all(clubs)
    session.commit()
    
    # Add members to clubs
    clubs[0].members.extend([members[0], members[1]])
    clubs[1].members.extend([members[1], members[2]])
    
    # Create sample meetings
    meetings = [
        Meeting(date=date(2023, 10, 15), location="Central Library", 
                club_id=clubs[0].id, book_id=books[0].id),
        Meeting(date=date(2023, 11, 5), location="Coffee Shop Downtown", 
                club_id=clubs[1].id, book_id=books[1].id)
    ]
    
    session.add_all(meetings)
    session.commit()
    
    print("Sample data created successfully!")

if __name__ == "__main__":
    create_sample_data()