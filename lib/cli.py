from helpers import (
    exit_program,
    init_database,
    list_books,
    find_book_by_title,
    create_book,
    list_members,
    create_member,
    list_clubs,
    create_club,
    add_member_to_club,
    schedule_meeting,
)

def main():
    init_database()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_books()
        elif choice == "2":
            find_book_by_title()
        elif choice == "3":
            create_book()
        elif choice == "4":
            list_members()
        elif choice == "5":
            create_member()
        elif choice == "6":
            list_clubs()
        elif choice == "7":
            create_club()
        elif choice == "8":
            add_member_to_club()
        elif choice == "9":
            schedule_meeting()
        else:
            print("Invalid choice. Please try again.")

def menu():
    print("\n=== Book Club Management System ===")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all books")
    print("2. Find book by title")
    print("3. Add a new book")
    print("4. List all members")
    print("5. Add a new member")
    print("6. List all clubs")
    print("7. Create a new club")
    print("8. Add member to club")
    print("9. Schedule a meeting")

if __name__ == "__main__":
    main()