# Book Club Management System

A command-line interface (CLI) application for managing book clubs, members, books, and meetings.

## Features

- Manage books with details like title, author, genre, and summary
- Manage club members with contact information
- Create and manage book clubs
- Schedule meetings for clubs with specific books
- Add members to clubs
- Database migrations with Alembic
- Sample data generation with Faker

## Installation

1. Clone this repository
2. Install dependencies: `pipenv install`
3. Enter the virtual environment: `pipenv shell`
4. Initialize the database: `alembic upgrade head`
5. Run the application: `python lib/cli.py`

## Usage

The application provides a menu-driven interface with the following options:

1. List all books
2. Find book by title
3. Add a new book
4. List all members
5. Add a new member
6. List all clubs
7. Create a new club
8. Add member to club
9. Schedule a meeting
10. Generate sample data (Faker)
0. Exit the program

## Database Migrations

This project uses Alembic for database migrations:

- Create a new migration: `alembic revision --autogenerate -m "Description of changes"`
- Apply migrations: `alembic upgrade head`
- Revert migrations: `alembic downgrade -1`

## File Structure

- `lib/cli.py`: Main command-line interface
- `lib/helpers.py`: Helper functions for database operations
- `lib/models/`: Directory containing data models
  - `book.py`: Book model
  - `member.py`: Member model
  - `club.py`: Club model
  - `meeting.py`: Meeting model
- `lib/debug.py`: Script for creating sample data
- `alembic.ini`: Alembic configuration
- `migrations/`: Directory containing database migration scripts

## Database

The application uses SQLite with SQLAlchemy ORM and Alembic for migrations. The database file `book_club.db` will be created automatically when you first run the application.

## Sample Data

To populate the database with sample data using Faker, run:
`python lib/debug.py`

Or use option 10 in the main menu.