from .models import session, create_tables
from .models.book import Book
from .models.member import Member
from .models.club import Club
from .models.meeting import Meeting
from datetime import datetime


def init_database():
    create_tables()
    print("Database initialized successfully!")

def exit_program():
    print("Thank you for using Book Club Manager. Goodbye!")
    exit()

# Book-related functions
def list_books():
    books = session.query(Book).all()
    if not books:
        print("No books found.")
        return
    for book in books:
        print(f"{book.id}: {book.title} by {book.author}")

def find_book_by_title():
    title = input("Enter the book title: ")
    book = session.query(Book).filter(Book.title.ilike(f"%{title}%")).first()
    if book:
        print(f"{book.id}: {book.title} by {book.author} ({book.genre})")
        print(f"Summary: {book.summary}")
        print(f"Publication Year: {book.publication_year}")
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

def edit_book():
    list_books()
    book_id = input("Enter the ID of the book to edit: ")
    
    try:
        book = session.query(Book).filter_by(id=int(book_id)).first()
        if not book:
            print(f"Book with ID {book_id} not found")
            return
        
        print(f"Editing: {book.title} by {book.author}")
        print("Leave field blank to keep current value")
        
        title = input(f"New title [{book.title}]: ") or book.title
        author = input(f"New author [{book.author}]: ") or book.author
        genre = input(f"New genre [{book.genre}]: ") or book.genre
        summary = input(f"New summary [{book.summary}]: ") or book.summary
        
        publication_year = input(f"New publication year [{book.publication_year}]: ")
        publication_year = int(publication_year) if publication_year else book.publication_year
        
        book.title = title
        book.author = author
        book.genre = genre
        book.summary = summary
        book.publication_year = publication_year
        
        session.commit()
        print(f"Successfully updated book: {book.title}")
        
    except Exception as e:
        print(f"Error editing book: {e}")
        session.rollback()

def delete_book():
    list_books()
    book_id = input("Enter the ID of the book to delete: ")
    
    try:
        book = session.query(Book).filter_by(id=int(book_id)).first()
        if book:
            session.delete(book)
            session.commit()
            print(f"Successfully deleted book: {book.title}")
        else:
            print(f"Book with ID {book_id} not found")
    except Exception as e:
        print(f"Error deleting book: {e}")
        session.rollback()

# Member-related functions
def list_members():
    members = session.query(Member).all()
    if not members:
        print("No members found.")
        return
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

def edit_member():
    list_members()
    member_id = input("Enter the ID of the member to edit: ")
    
    try:
        member = session.query(Member).filter_by(id=int(member_id)).first()
        if not member:
            print(f"Member with ID {member_id} not found")
            return
        
        print(f"Editing: {member.name} ({member.email})")
        print("Leave field blank to keep current value")
        
        name = input(f"New name [{member.name}]: ") or member.name
        email = input(f"New email [{member.email}]: ") or member.email
        
        member.name = name
        member.email = email
        
        session.commit()
        print(f"Successfully updated member: {member.name}")
        
    except Exception as e:
        print(f"Error editing member: {e}")
        session.rollback()

def delete_member():
    list_members()
    member_id = input("Enter the ID of the member to delete: ")
    
    try:
        member = session.query(Member).filter_by(id=int(member_id)).first()
        if member:
            session.delete(member)
            session.commit()
            print(f"Successfully deleted member: {member.name}")
        else:
            print(f"Member with ID {member_id} not found")
    except Exception as e:
        print(f"Error deleting member: {e}")
        session.rollback()

# Club-related functions
def list_clubs():
    clubs = session.query(Club).all()
    if not clubs:
        print("No clubs found.")
        return
    for club in clubs:
        genre_info = f" - Genre: {club.genre}" if club.genre else ""
        print(f"{club.id}: {club.name} - {club.description}{genre_info}")

def create_club():
    name = input("Enter club name: ")
    description = input("Enter club description: ")
    genre = input("Enter club genre: ")

    try:
        club = Club(name=name, description=description, genre=genre)
        session.add(club)
        session.commit()
        print(f"Successfully created club: {name}")
    except Exception as e:
        print(f"Error creating club: {e}")
        session.rollback()

def edit_club():
    list_clubs()
    club_id = input("Enter the ID of the club to edit: ")
    
    try:
        club = session.query(Club).filter_by(id=int(club_id)).first()
        if not club:
            print(f"Club with ID {club_id} not found")
            return
        
        print(f"Editing: {club.name}")
        print("Leave field blank to keep current value")
        
        name = input(f"New name [{club.name}]: ") or club.name
        description = input(f"New description [{club.description}]: ") or club.description
        genre = input(f"New genre [{club.genre}]: ") or club.genre

        club.name = name
        club.description = description
        club.genre = genre

        session.commit()
        print(f"Successfully updated club: {club.name}")
        
    except Exception as e:
        print(f"Error editing club: {e}")
        session.rollback()

def delete_club():
    list_clubs()
    club_id = input("Enter the ID of the club to delete: ")
    
    try:
        club = session.query(Club).filter_by(id=int(club_id)).first()
        if club:
            session.delete(club)
            session.commit()
            print(f"Successfully deleted club: {club.name}")
        else:
            print(f"Club with ID {club_id} not found")
    except Exception as e:
        print(f"Error deleting club: {e}")
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
            # Check if member is already in the club
            if member in club.members:
                print(f"{member.name} is already in {club.name}")
            else:
                club.members.append(member)
                session.commit()
                print(f"Successfully added {member.name} to {club.name}")
        else:
            print("Invalid club or member ID")
    except Exception as e:
        print(f"Error adding member to club: {e}")
        session.rollback()

# Meeting-related functions
def list_meetings():
    meetings = session.query(Meeting).all()
    if not meetings:
        print("No meetings scheduled.")
        return
    
    for meeting in meetings:
        book_info = f" - Book: {meeting.book.title}" if meeting.book else ""
        print(f"{meeting.id}: {meeting.club.name} on {meeting.date}{book_info}")

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

def edit_meeting():
    list_meetings()
    meeting_id = input("Enter the ID of the meeting to edit: ")
    
    try:
        meeting = session.query(Meeting).filter_by(id=int(meeting_id)).first()
        if not meeting:
            print(f"Meeting with ID {meeting_id} not found")
            return
        
        print(f"Editing: {meeting.club.name} meeting on {meeting.date}")
        print("Leave field blank to keep current value")
        
        # Show current book if exists
        current_book = meeting.book.title if meeting.book else "None"
        list_books()
        book_id = input(f"New book ID [{current_book}]: ")
        book_id = int(book_id) if book_id else meeting.book_id
        
        date_str = input(f"New date (YYYY-MM-DD) [{meeting.date}]: ")
        date = datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else meeting.date
        
        location = input(f"New location [{meeting.location}]: ") or meeting.location
        notes = input(f"New notes [{meeting.notes}]: ") or meeting.notes
        
        meeting.book_id = book_id
        meeting.date = date
        meeting.location = location
        meeting.notes = notes
        
        session.commit()
        print(f"Successfully updated meeting on {meeting.date}")
        
    except Exception as e:
        print(f"Error editing meeting: {e}")
        session.rollback()

def delete_meeting():
    list_meetings()
    meeting_id = input("Enter the ID of the meeting to delete: ")
    
    try:
        meeting = session.query(Meeting).filter_by(id=int(meeting_id)).first()
        if meeting:
            session.delete(meeting)
            session.commit()
            print(f"Successfully deleted meeting on {meeting.date}")
        else:
            print(f"Meeting with ID {meeting_id} not found")
    except Exception as e:
        print(f"Error deleting meeting: {e}")
        session.rollback()