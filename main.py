from library import (
    sh_books,
    search_book,
    search_category,
    issue_book,
    return_book,
    show_members,
    show_library_statistics
)


while True:

    print("\n======================================")
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("======================================")

    print("1. Show Available Books")
    print("2. Search Book")
    print("3. Search by Category")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Show Members")
    print("7. Library Statistics")
    print("8. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        sh_books()

    elif choice == "2":
        search_book()

    elif choice == "3":
        search_category()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        show_members()

    elif choice == "7":
        show_library_statistics()

    elif choice == "8":
        print("\nThank you for using the Library Management System!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 8.")