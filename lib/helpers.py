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

def get_entity_by_id(model, entity_id, entity_name):
    """Get entity by ID with error handling"""
    try:
        entity = session.query(model).filter_by(id=int(entity_id)).first()
        if not entity:
            print(f"{entity_name} with ID {entity_id} not found")
        return entity
    except ValueError:
        print(f"Invalid {entity_name.lower()} ID")
        return None

def safe_commit(success_msg, error_msg):
    """Safely commit changes with error handling"""
    try:
        session.commit()
        print(success_msg)
        return True
    except Exception as e:
        print(f"{error_msg}: {e}")
        session.rollback()
        return False

def get_input_or_default(prompt, default):
    """Get user input or return default value"""
    value = input(prompt)
    return value if value else default

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
        safe_commit(f"Successfully created book: {title}", "Error creating book")
    except ValueError:
        print("Invalid publication year")

def edit_book():
    list_books()
    book_id = input("Enter the ID of the book to edit: ")
    book = get_entity_by_id(Book, book_id, "Book")
    if not book:
        return
    
    print(f"Editing: {book.title} by {book.author}")
    print("Leave field blank to keep current value")
    
    book.title = get_input_or_default(f"New title [{book.title}]: ", book.title)
    book.author = get_input_or_default(f"New author [{book.author}]: ", book.author)
    book.genre = get_input_or_default(f"New genre [{book.genre}]: ", book.genre)
    book.summary = get_input_or_default(f"New summary [{book.summary}]: ", book.summary)
    
    year_input = input(f"New publication year [{book.publication_year}]: ")
    if year_input:
        try:
            book.publication_year = int(year_input)
        except ValueError:
            print("Invalid year, keeping current value")
    
    safe_commit(f"Successfully updated book: {book.title}", "Error editing book")

def delete_book():
    list_books()
    book_id = input("Enter the ID of the book to delete: ")
    book = get_entity_by_id(Book, book_id, "Book")
    if book:
        title = book.title
        session.delete(book)
        safe_commit(f"Successfully deleted book: {title}", "Error deleting book")

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
    
    member = Member(name=name, email=email)
    session.add(member)
    safe_commit(f"Successfully created member: {name}", "Error creating member")

def edit_member():
    list_members()
    member_id = input("Enter the ID of the member to edit: ")
    member = get_entity_by_id(Member, member_id, "Member")
    if not member:
        return
    
    print(f"Editing: {member.name} ({member.email})")
    print("Leave field blank to keep current value")
    
    member.name = get_input_or_default(f"New name [{member.name}]: ", member.name)
    member.email = get_input_or_default(f"New email [{member.email}]: ", member.email)
    
    safe_commit(f"Successfully updated member: {member.name}", "Error editing member")

def delete_member():
    list_members()
    member_id = input("Enter the ID of the member to delete: ")
    member = get_entity_by_id(Member, member_id, "Member")
    if member:
        name = member.name
        session.delete(member)
        safe_commit(f"Successfully deleted member: {name}", "Error deleting member")

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

    club = Club(name=name, description=description, genre=genre)
    session.add(club)
    safe_commit(f"Successfully created club: {name}", "Error creating club")

def edit_club():
    list_clubs()
    club_id = input("Enter the ID of the club to edit: ")
    club = get_entity_by_id(Club, club_id, "Club")
    if not club:
        return
    
    print(f"Editing: {club.name}")
    print("Leave field blank to keep current value")
    
    club.name = get_input_or_default(f"New name [{club.name}]: ", club.name)
    club.description = get_input_or_default(f"New description [{club.description}]: ", club.description)
    club.genre = get_input_or_default(f"New genre [{club.genre}]: ", club.genre)

    safe_commit(f"Successfully updated club: {club.name}", "Error editing club")

def delete_club():
    list_clubs()
    club_id = input("Enter the ID of the club to delete: ")
    club = get_entity_by_id(Club, club_id, "Club")
    if club:
        name = club.name
        session.delete(club)
        safe_commit(f"Successfully deleted club: {name}", "Error deleting club")

def add_member_to_club():
    list_clubs()
    club_id = input("Enter club ID: ")
    club = get_entity_by_id(Club, club_id, "Club")
    if not club:
        return
    
    list_members()
    member_id = input("Enter member ID: ")
    member = get_entity_by_id(Member, member_id, "Member")
    if not member:
        return
    
    if member in club.members:
        print(f"{member.name} is already in {club.name}")
    else:
        club.members.append(member)
        safe_commit(f"Successfully added {member.name} to {club.name}", "Error adding member to club")

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
    club = get_entity_by_id(Club, club_id, "Club")
    if not club:
        return
    
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
        safe_commit("Successfully scheduled meeting", "Error scheduling meeting")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD")

def edit_meeting():
    list_meetings()
    meeting_id = input("Enter the ID of the meeting to edit: ")
    meeting = get_entity_by_id(Meeting, meeting_id, "Meeting")
    if not meeting:
        return
    
    print(f"Editing: {meeting.club.name} meeting on {meeting.date}")
    print("Leave field blank to keep current value")
    
    current_book = meeting.book.title if meeting.book else "None"
    list_books()
    book_id = input(f"New book ID [{current_book}]: ")
    if book_id:
        try:
            meeting.book_id = int(book_id)
        except ValueError:
            print("Invalid book ID, keeping current value")
    
    date_str = input(f"New date (YYYY-MM-DD) [{meeting.date}]: ")
    if date_str:
        try:
            meeting.date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format, keeping current value")
    
    meeting.location = get_input_or_default(f"New location [{meeting.location}]: ", meeting.location)
    meeting.notes = get_input_or_default(f"New notes [{meeting.notes}]: ", meeting.notes)
    
    safe_commit(f"Successfully updated meeting on {meeting.date}", "Error editing meeting")

def delete_meeting():
    list_meetings()
    meeting_id = input("Enter the ID of the meeting to delete: ")
    meeting = get_entity_by_id(Meeting, meeting_id, "Meeting")
    if meeting:
        date = meeting.date
        session.delete(meeting)
        safe_commit(f"Successfully deleted meeting on {date}", "Error deleting meeting")