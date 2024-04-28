#  ________  ________  ________        ___  _______   ________ _________        ________
# |\   __  \|\   __  \|\   __  \      |\  \|\  ___ \ |\   ____\\___   ___\     |\_____  \
# \ \  \|\  \ \  \|\  \ \  \|\  \     \ \  \ \   __/|\ \  \___\|___ \  \_|     \|____|\ /_
#  \ \   ____\ \   _  _\ \  \\\  \  __ \ \  \ \  \_|/_\ \  \       \ \  \            \|\  \
#   \ \  \___|\ \  \\  \\ \  \\\  \|\  \\_\  \ \  \_|\ \ \  \____   \ \  \          __\_\  \
#    \ \__\    \ \__\\ _\\ \_______\ \________\ \_______\ \_______\  \ \__\        |\_______\
#     \|__|     \|__|\|__|\|_______|\|________|\|_______|\|_______|   \|__|        \|_______|
# Author: Anna-Marie DiNofrio
# CIST2110-Project-3 Library Management System (LMS)
# Project 3 will implement a library management system (LMS) that will allow users to manage books, users, and a library to manage collection of books and users.
# The LMS will be menu driven and will allow users to add, delete, and update books and users.
# Users will also be able to borrow and return books.
# The LMS will also allow users to search for books and users.

# ENABLE WORD WRAP TO MAKE THINGS EASIER TO READ:
# VIEW (at the top) -> WORD WRAP

# Import statements:
from tabulate import tabulate
import csv

# Project outline and requirements:

# OUTLINE - The LMS will consist of the following classes and methods:

# 1. Create a Book class that has the following attributes (create a __init__ method)):
#    a. isbn (int)
#    b. title (string)
#    c. author (string)
#    d. borrowed (boolean) - this should not be passed in as a parameter, it should be set to False by default
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES

# Methods:
#    a. __str__ (returns a string representation of the book using the following format: ISBN: <ISBN>, Title: <Title>, Author: <Author>, Borrowed: <Borrowed>)
#    b. check_out - sets borrowed to True and returns a message that the book has been checked out
#    c. check_in - sets borrowed to False and returns a message that the book has been checked in
#    d. isBorrowed - returns True if the book is borrowed and False if the book is not borrowed
class Book:
    """
    Book class thas has an isbn, title, author, and borrowed status
    """
    def __init__(self, title: str, author: str, isbn: int, borrowed: bool = False) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.borrowed = borrowed
    def __str__(self) -> str:
        return f"ISBN: {self.isbn}, Title: {self.title}, Author: {self.author}, Borrowed: {self.borrowed}"
    def check_out(self) -> str:
        self.borrowed = True
        return f"{self.title} has been checked out"
    def check_in(self) -> str:
        self.borrowed = False
        return f"{self.title} has been checked in"
    def isBorrowed(self) -> bool:
        return self.borrowed


# 2. Create a User class that has the following attributes (create a __init__ method)):
#    a. name (string)
#    c. member_id (int)
#    d. borrowed_books (list of books) - this should not be passed in as a parameter, it should be set to an empty list by default
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES

# Methods:
#    a. __str__ (returns a string representation of the user using the following format: Name: <Name>, ID: <ID>, Borrowed Books: <Borrowed Books>)
#    b. borrow_book - adds the book to the borrowed_books list, updates the isBorrowed attribute of the book to True, and returns a message that the book has been checked out (should take a book object as a parameter)
#    c. return_book - removes the book from the borrowed_books list, updates the isBorrowed attribute of the book to False, and returns a message that the book has been checked in (should take a book object as a parameter)

class User:
    """
    User class that has a name, member_id, and list of borrowed books
    """
    def __init__(self, name: str, member_id: int, borrowed_books: list = []) -> None:
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books
    def __str__(self) -> str:
        return f"Name: {self.name}, ID: {self.member_id}, Borrowed Books: {self.borrowed_books}"
    def borrow_book(self, book: Book) -> str:
        self.borrowed_books.append(book)
        book.borrowed = True
        return f"{book.title} has been checked out"
    def return_book(self, book: Book) -> str:
        self.borrowed_books.remove(book)
        book.borrowed = False
        return f"{book.title} has been checked in"


# 3. Create a Library class that has the following attributes (create a __init__ method)):
#    a. books (list of books)
#    b. users (list of users)
# USE SELF IN THE __INIT__ METHOD TO CREATE THESE ATTRIBUTES

# Methods:
#    a. __str__ (returns a string representation of the library using the following format: Books: <Books>, Users: <Users>)
#    b. add_book - adds a book to the books list (should take a book object as a parameter)
#    c. add_user - adds a user to the users list (should take a user object as a parameter)
#    d. find_book - returns the book with the given ISBN (should take an ISBN as a parameter)
#    e. find_user - returns the user with the given ID (should take an ID as a parameter)
#    f. export_books_to_csv - exports the books list to a csv file (should take a filename as a parameter)
#       The csv file should have the following format: ISBN,Title,Author,Borrowed
#       The csv.DictWriter class is very useful for this: https://docs.python.org/3/library/csv.html#csv.DictWriter
#    g. export_users_to_csv - exports the users list to a csv file (should take a filename as a parameter)
#       This will be similar to the export_books_to_csv method but there is a slight difference with the borrowed_books attribute if you get stuck this code might help:
#       borrowed_books_titles = [book.title for book in user.borrowed_books]
#       Use that and pythons .join method to create a string of the borrowed books titles

class Library: 
    """
    Product library that has a list of books and users
    """
    def __init__(self, books: list = [], users: list = []) -> None:
        self.books = books
        self.users = users
    def __str__(self) -> str:
        return f"Books: {self.books}, Users: {self.users}"
    def add_book(self, book: Book) -> None:
        self.books.append(book)
    def add_user(self, user: User) -> None:
        self.users.append(user)
    def find_book(self, isbn: int) -> Book:
        for book in self.books:
            if book.isbn == isbn:
                return book
    def find_user(self, member_id: int) -> User:
        for user in self.users:
            if user.member_id == member_id:
                return user
    def export_books_to_csv(self, filename: str) -> None:
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["ISBN", "Title", "Author", "Borrowed"])
            writer.writeheader()
            for book in self.books:
                writer.writerow({"ISBN": book.isbn, "Title": book.title, "Author": book.author, "Borrowed": book.borrowed})
    def export_users_to_csv(self, filename: str) -> None:
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "ID", "Borrowed Books"])
            writer.writeheader()
            for user in self.users:
                borrowed_books_titles = [book.title for book in user.borrowed_books]
                writer.writerow({"Name": user.name, "ID": user.member_id, "Borrowed Books": ", ".join(borrowed_books_titles)})


# 4. Create a menu that will allow users to:
#    a. Add books
#    b. Add users
#    c. Delete books
#    d. Delete users
#    g. Borrow books
#    h. Return books
#    i. Search books
#    j. Check if book is available
#    k. Search users
#    l. Export books to csv
#    m. Export users to csv
#    z. Exit

def menu() -> str:
    while True:
        try:
            print("a. Add books")
            print("b. Add users")
            print("c. Delete books")
            print("d. Delete users")
            print("g. Borrow books")
            print("h. Return books")
            print("i. Search books")
            print("j. Check if book is available")
            print("k. Search users")
            print("l. Export books to csv")
            print("m. Export users to csv")
            print("z. Exit")
            choice = input("Enter a choice: ")
            return choice
        except ValueError:
            print("Invalid choice. Please enter a valid numer.")

# RQUIREMENTS:
# 1. You should be doing error checking on all user input (make sure the user enters a valid ISBN, ID, etc.) and handle any errors appropriately (i.e. if the user enters an invalid ISBN, ask them to enter a valid ISBN)
# 2. You should be using try except blocks to handle any errors
# 3. You should be using the classes and methods outlined above with the exact names and parameters
# 4. You should be using the menu to call the appropriate methods
# 5. There is a Project3Tests.py file that will help you test your code. You should be able to run that file and pass all the tests.
#    Remember to run pytest use the following command in the terminal: pytest Project3Tests.py
# 6. The Project3Tests.py file is missing 2 tests. test_user_return and test_library_find_user. You will need to implement those tests and ensure they pass.
# 7. In your main method you should create a Library object first to use for the rest of the program. You should not be creating a new library object every time you call a method. (Similar to the Store object in Lab 13)
# 8. In your main method you should be using a while loop to keep the program running until the user chooses to exit.

# IMPORTANT: You will only have 1 submission for this project so make sure you test your code thoroughly before submitting.

# You will be graded on the following:
# 1. Did you follow the project outline and requirements?
# 2. Does your code run without errors?
# 3. Did you use try except blocks to handle errors?
# 4. Did you use the classes and methods outlined above with the exact names and parameters?
# 5. Did you use the menu to call the appropriate methods?
# 6. Did you include docstrings for all classes and methods?
# 7. Did you include type hints for all methods?
# 8. Did your pytests for the test_user_return and test_library_find_user work?
# 9. Did you create a test plan that thoroghly tests the program?


def main():
    library = Library()
    while True:
        print("---------------------------")
        choice = menu()
        if choice == "a":
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            isbn = int(input("Enter the ISBN: "))
            book = Book(title, author, isbn)
            library.add_book(book)
            print(book)
        elif choice == "b":
            name = input("Enter the name: ")
            member_id = int(input("Enter the member ID: "))
            user = User(name, member_id)
            library.add_user(user)
        elif choice == "c":
            isbn = int(input("Enter the ISBN of the book to delete: "))
            book = library.find_book(isbn)
            library.books.remove(book)
        elif choice == "d":
            member_id = int(input("Enter the member ID of the user to delete: "))
            user = library.find_user(member_id)
            library.users.remove(user)
        elif choice == "g":
            isbn = int(input("Enter the ISBN of the book to borrow: "))
            member_id = int(input("Enter the member ID of the user borrowing the book: "))
            book = library.find_book(isbn)
            user = library.find_user(member_id)
            user.borrow_book(book)
        elif choice == "h":
            isbn = int(input("Enter the ISBN of the book to return: "))
            member_id = int(input("Enter the member ID of the user returning the book: "))
            book = library.find_book(isbn)
            user = library.find_user(member_id)
            user.return_book(book)
        elif choice == "i":
            isbn = int(input("Enter the ISBN of the book to search for: "))
            book = library.find_book(isbn)
            print(book)
        elif choice == "j":
            isbn = int(input("Enter the ISBN of the book to check if it is available: "))
            book = library.find_book(isbn)
            if book is None:
                print("The book is not available")
            else:
                print("The book is available")
        elif choice == "k":
            member_id = int(input("Enter the member ID of the user to search for: "))
            user = library.find_user(member_id)
            print(user)
            if user is None:
                print("The user is not available")
        elif choice == "l":
            filename = input("Enter the filename to export the books to: ")
            library.export_books_to_csv(filename)
        elif choice == "m":
            filename = input("Enter the filename to export the users to: ")
            library.export_users_to_csv(filename)
        elif choice == "z":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
