from data import books, members, iss_book, categories


def sh_books():
    print("\n========== AVAILABLE BOOKS ==========")

    count = 0

    for book_id, details in books.items():

        if book_id not in iss_book:
            print(
                book_id, "|",
                details[0], "|",
                details[1], "|",
                details[2]
            )
            count += 1

    print("-------------------------------------")
    print("Total available books:", count)


def search_book():
    title = input("\nEnter book title to search: ").strip().lower()

    if title == "":
        print("Please enter a book title.")
        return

    found = False

    print("\n========== SEARCH RESULTS ==========")

    for book_id, details in books.items():

        if title in details[0].lower():

            status = "Issued" if book_id in iss_book else "Available"

            print("Book ID:", book_id)
            print("Title:", details[0])
            print("Author:", details[1])
            print("Category:", details[2])
            print("Status:", status)
            print("-----------------------------------")

            found = True

    if not found:
        print("No book found.")


def search_category():
    print("\n========== BOOK CATEGORIES ==========")

    for category in sorted(categories):
        print("-", category)

    category = input("\nEnter category: ").strip().lower()

    if category == "":
        print("Please enter a category.")
        return

    found = False

    print("\n========== BOOKS IN CATEGORY ==========")

    for book_id, details in books.items():

        if category in details[2].lower():

            status = "Issued" if book_id in iss_book else "Available"

            print(
                book_id, "|",
                details[0], "|",
                details[1], "|",
                status
            )

            found = True

    if not found:
        print("No books found in this category.")


def issue_book():

    try:
        book_id = int(input("\nEnter book ID: "))
        member_id = int(input("Enter member ID: "))

    except ValueError:
        print("Please enter numbers only.")
        return

    if book_id not in books:
        print("Book does not exist.")
        return

    if member_id not in members:
        print("Member does not exist.")
        return

    if book_id in iss_book:
        print("Book is already issued.")
        return

    iss_book.add(book_id)

    with open("books.txt", "a") as file:
        file.write(
            str(book_id) + "," +
            str(member_id) + ",Issued\n"
        )

    print("Book issued successfully.")
    print("Book:", books[book_id][0])
    print("Issued to:", members[member_id])


def return_book():

    try:
        book_id = int(input("\nEnter book ID: "))

    except ValueError:
        print("Please enter a valid book ID.")
        return

    if book_id not in books:
        print("Book does not exist.")
        return

    if book_id not in iss_book:
        print("This book is not currently issued.")
        return

    iss_book.remove(book_id)

    with open("books.txt", "a") as file:
        file.write(
            str(book_id) + ",Returned\n"
        )

    print("Book returned successfully.")
    print("Book:", books[book_id][0])


def show_members():
    print("\n========== LIBRARY MEMBERS ==========")

    for member_id, name in members.items():
        print("Member ID:", member_id, "| Name:", name)

    print("-------------------------------------")
    print("Total members:", len(members))


def show_library_statistics():
    total_books = len(books)
    total_members = len(members)
    total_categories = len(categories)
    issued = len(iss_book)
    available = total_books - issued

    print("\n========== LIBRARY STATISTICS ==========")
    print("Total books:", total_books)
    print("Available books:", available)
    print("Issued books:", issued)
    print("Total members:", total_members)
    print("Total categories:", total_categories)

