from lib.models import session, create_tables
from lib.models.book import Book
from lib.models.member import Member
from lib.models.club import Club
from lib.models.meeting import Meeting
from datetime import datetime, date, timedelta
from faker import Faker
import random

fake = Faker()

def init_database():
    create_tables()
    print("Database initialized successfully!")

def exit_program():
    print("Thank you for using Book Club Manager. Goodbye!")
    exit()

# Book-related functions
def list_books():
    books = session.query(Book).all()
    for book in books:
        print(f"{book.id}: {book.title} by {book.author}")

def find_book_by_title():
    title = input("Enter the book title: ")
    book = session.query(Book).filter(Book.title.ilike(f"%{title}%")).first()
    if book:
        print(f"{book.id}: {book.title} by {book.author} ({book.genre})")
        print(f"Summary: {book.summary}")
    else:
        print(f"Book with title '{title}' not found")

def create_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    genre = input("Enter the genre: ")
    summary = input("Enter a summary: ")
    publication_year = input("Enter publication year: ")
    
    try:
        book = Book(
            title=title,
            author=author,
            genre=genre,
            summary=summary,
            publication_year=int(publication_year)
        )
        session.add(book)
        session.commit()
        print(f"Successfully created book: {title}")
    except Exception as e:
        print(f"Error creating book: {e}")
        session.rollback()

# Member-related functions
def list_members():
    members = session.query(Member).all()
    for member in members:
        print(f"{member.id}: {member.name} ({member.email})")

def create_member():
    name = input("Enter member name: ")
    email = input("Enter member email: ")
    
    try:
        member = Member(name=name, email=email)
        session.add(member)
        session.commit()
        print(f"Successfully created member: {name}")
    except Exception as e:
        print(f"Error creating member: {e}")
        session.rollback()

# Club-related functions
def list_clubs():
    clubs = session.query(Club).all()
    for club in clubs:
        print(f"{club.id}: {club.name} - {club.description}")

def create_club():
    name = input("Enter club name: ")
    description = input("Enter club description: ")
    
    try:
        club = Club(name=name, description=description)
        session.add(club)
        session.commit()
        print(f"Successfully created club: {name}")
    except Exception as e:
        print(f"Error creating club: {e}")
        session.rollback()

def add_member_to_club():
    list_clubs()
    club_id = input("Enter club ID: ")
    
    list_members()
    member_id = input("Enter member ID: ")
    
    try:
        club = session.query(Club).filter_by(id=int(club_id)).first()
        member = session.query(Member).filter_by(id=int(member_id)).first()
        
        if club and member:
            club.members.append(member)
            session.commit()
            print(f"Successfully added {member.name} to {club.name}")
        else:
            print("Invalid club or member ID")
    except Exception as e:
        print(f"Error adding member to club: {e}")
        session.rollback()

# Meeting-related functions
def schedule_meeting():
    list_clubs()
    club_id = input("Enter club ID: ")
    
    list_books()
    book_id = input("Enter book ID (or leave blank if not decided): ")
    
    date_str = input("Enter meeting date (YYYY-MM-DD): ")
    location = input("Enter meeting location: ")
    notes = input("Enter meeting notes: ")
    
    try:
        meeting = Meeting(
            date=datetime.strptime(date_str, "%Y-%m-%d").date(),
            location=location,
            notes=notes,
            club_id=int(club_id)
        )
        
        if book_id:
            meeting.book_id = int(book_id)
            
        session.add(meeting)
        session.commit()
        print("Successfully scheduled meeting")
    except Exception as e:
        print(f"Error scheduling meeting: {e}")
        session.rollback()

# Faker-related functions for generating sample data
def generate_sample_data():
    """Generate sample data using Faker"""
    print("Generating sample data...")
    
    # Generate books
    genres = ["Fiction", "Non-Fiction", "Science Fiction", "Fantasy", "Mystery", "Romance", "Biography"]
    books = []
    for _ in range(20):
        book = Book(
            title=fake.catch_phrase().title(),
            author=fake.name(),
            genre=random.choice(genres),
            summary=fake.paragraph(nb_sentences=3),
            publication_year=fake.year()
        )
        books.append(book)
    
    session.add_all(books)
    session.commit()
    print(f"Generated {len(books)} books")
    
    # Generate members
    members = []
    for _ in range(15):
        member = Member(
            name=fake.name(),
            email=fake.email()
        )
        members.append(member)
    
    session.add_all(members)
    session.commit()
    print(f"Generated {len(members)} members")
    
    # Generate clubs
    clubs = []
    for _ in range(5):
        club = Club(
            name=fake.company() + " Book Club",
            description=fake.sentence()
        )
        clubs.append(club)
    
    session.add_all(clubs)
    session.commit()
    print(f"Generated {len(clubs)} clubs")
    
    # Add random members to clubs
    for club in clubs:
        num_members = random.randint(3, 8)
        club_members = random.sample(members, num_members)
        club.members.extend(club_members)
    
    session.commit()
    print("Assigned members to clubs")
    
    # Generate meetings
    meetings = []
    for club in clubs:
        num_meetings = random.randint(2, 5)
        for _ in range(num_meetings):
            meeting = Meeting(
                date=fake.date_between(start_date='-1y', end_date='+1y'),
                location=fake.city(),
                notes=fake.paragraph(nb_sentences=2),
                club_id=club.id,
                book_id=random.choice(books).id if random.random() > 0.2 else None
            )
            meetings.append(meeting)
    
    session.add_all(meetings)
    session.commit()
    print(f"Generated {len(meetings)} meetings")
    
    print("Sample data generation complete!")