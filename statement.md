# LIBRARY MANAGEMENT SYSTEM

## Problem Statement

Managing a library manually can become difficult when the number of books and members increases.

It can be challenging to keep track of:

- Available books
- Issued books
- Returned books
- Library members
- Different book categories

Therefore, a simple computer-based system is required to perform basic library management operations in an organized manner.

---

## Project Objective

The objective of this project is to develop a simple Library Management System using Python.

The system should allow the user to:

1. View available books.
2. Search for a book.
3. Search for books according to their category.
4. Issue a book to a library member.
5. Return an issued book.
6. View library members.
7. View basic library statistics.

---

## Proposed Solution

The proposed solution is a console-based Python application.

The system will store book and member information using basic Python data structures such as:

- Dictionaries
- Tuples
- Sets

Different functions will be used to perform library operations.

The project will be divided into multiple Python files to keep the program organized.

---

## Project Requirements

The system should contain:

### Books

The system should maintain information about at least 100 books.

Each book should contain:

- Book ID
- Book title
- Author name
- Category

### Members

The system should maintain information about at least 50 library members.

Each member should have:

- Member ID
- Member name

### Categories

The system should contain multiple book categories such as:

- Programming
- Computer Science
- Networking
- Artificial Intelligence
- Machine Learning
- Database
- Cyber Security
- Mathematics
- Physics
- Chemistry
- Engineering
- Electronics
- Communication
- And other relevant categories

---

## Functional Requirements

### 1. View Available Books

The system should display books that are currently available for issuing.

### 2. Search Book

The user should be able to search for a book using its title.

The system should display the matching book and its current availability status.

### 3. Search by Category

The user should be able to enter a category and view the books belonging to that category.

### 4. Issue Book

The user should enter:

- Book ID
- Member ID

The system should check whether:

- The book exists.
- The member exists.
- The book is already issued.

If all conditions are satisfied, the book should be issued.

### 5. Return Book

The user should enter the Book ID.

The system should check whether the book is currently issued.

If the book is issued, it should be marked as available again.

### 6. View Members

The system should display the registered library members.

### 7. Library Statistics

The system should display:

- Total number of books
- Number of available books
- Number of issued books
- Total number of members
- Total number of categories

---

## Data Structures

The project will use basic Python data structures.

### Dictionary

Dictionaries will be used to store books and members.

Example:

```python
books = {
    101: ("Python Basics", "Ravi Kumar", "Programming")
}