from .helpers import (
    exit_program,
    init_database,
    list_books,
    find_book_by_title,
    create_book,
    edit_book,
    delete_book,
    list_members,
    create_member,
    edit_member,
    delete_member,
    list_clubs,
    create_club,
    edit_club,
    delete_club,
    add_member_to_club,
    schedule_meeting,
    list_meetings,
    edit_meeting,
    delete_meeting
)

def main():
    init_database()
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            list_books()
        elif choice == "2":
            find_book_by_title()
        elif choice == "3":
            create_book()
        elif choice == "4":
            edit_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            list_members()
        elif choice == "7":
            create_member()
        elif choice == "8":
            edit_member()
        elif choice == "9":
            delete_member()
        elif choice == "10":
            list_clubs()
        elif choice == "11":
            create_club()
        elif choice == "12":
            edit_club()
        elif choice == "13":
            delete_club()
        elif choice == "14":
            add_member_to_club()
        elif choice == "15":
            schedule_meeting()
        elif choice == "16":
            list_meetings()
        elif choice == "17":
            edit_meeting()
        elif choice == "18":
            delete_meeting()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

def menu():
    print("\n=== Book Club Management System ===")
    print("Please select an option:")
    print("1. List all books")
    print("2. Find book by title")
    print("3. Add a new book")
    print("4. Edit a book")
    print("5. Delete a book")
    print("6. List all members")
    print("7. Add a new member")
    print("8. Edit a member")
    print("9. Delete a member")
    print("10. List all clubs")
    print("11. Create a new club")
    print("12. Edit a club")
    print("13. Delete a club")
    print("14. Add member to club")
    print("15. Schedule a meeting")
    print("16. List all meetings")
    print("17. Edit a meeting")
    print("18. Delete a meeting")
    print("0. Exit the program")

if __name__ == "__main__":
    main()