# Book Club Management System

A command-line interface (CLI) application for managing book clubs, members, books, and meetings.

## Features
# CRUD Operations

- Complete Member Management: Create, view, edit, and delete club members
- Complete Book Management: Add, search, edit, and remove books from the database
- Complete Club Management: Create clubs with genres, manage descriptions, and organize meetings
- Complete Meeting Management: Schedule, view, edit, and delete book club meetings
- Membership Management: Add members to specific clubs and track relationships

# Advanced Features

- Database Migrations: Alembic integration for safe schema evolution
- Genre Categorization: Clubs organized by literary genres (Romance, Fantasy, Sci-Fi, etc.)
- Relationship Management: Many-to-many relationships between members and clubs
- Professional Error Handling: Comprehensive input validation and transaction rollbacks

## Technology Stack

- Python 3.8+
- SQLAlchemy ORM: Database object-relational mapping
- Alembic: Database migrations and schema management
- SQLite: Lightweight database storage
- Pipenv: Dependency management and virtual environment

## Installation

1. Clone this repository
2. Install dependencies: `pipenv install`
3. Enter the virtual environment: `pipenv shell`
4. Initialize the database: `alembic upgrade head`
5. Run the application: `python main.py`

## Usage

The application provides a menu-driven interface with the following options:

1. List all books
2. Find book by title
3. Add a new book
4. Edit a book
5. Delete a book
6. List all members
7. Add a new member
8. Edit a member
9. Delete a member
10. List all clubs
11. Create a new club
12. Edit a club
13. Delete a club
14. Add member to club
15. Schedule a meeting
16. List all meetings
17. Edit a meeting
18. Delete a meeting
0. Exit the program

## Database Migrations

This project uses Alembic for database migrations:

- Create a new migration: `alembic revision --autogenerate -m "Description of changes"`
- Apply migrations: `alembic upgrade head`
- Revert migrations: `alembic downgrade -1`

## File Structure

- main.py: Application entry point (newly added)
- lib/cli.py: Main command-line interface with complete CRUD menu options
- lib/helpers.py: Helper functions for all database operations with full CRUD implementation
- lib/models/: Directory containing data models with proper relationships
  - __init__.py: Database configuration with session management
  - book.py: Book model with title, author, genre, summary, and publication_year fields
  - member.py: Member model with name and email fields
  - club.py: Club model with name, description, and genre fields (genre recently added via migration)
  - meeting.py: Meeting model with date, location, notes, and relationships to clubs and books
- lib/debug.py: Script for creating sample data without Faker dependency
- alembic.ini: Alembic configuration with SQLite database URL
- migrations/: Directory containing database migration scripts
  - env.py: Configured with proper model imports and path setup
  - script.py.mako: Migration template
  - versions/: Contains executed migration files
- book_club.db: SQLite database file (auto-generated after migrations)
- Pipfile: Dependency management with SQLAlchemy and Alembic
- Pipfile.lock: Locked dependency versions

## Database

The application uses SQLite with SQLAlchemy ORM and Alembic for migrations. The database file `book_club.db` will be created automatically when you first run the application.

## License

This project is licensed under the MIT License.

## Author

Wambui Kibathi
