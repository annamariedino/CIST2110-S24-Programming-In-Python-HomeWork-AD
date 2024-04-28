# Test Plan for Project 3
## 1

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|

|001|test_book_creation| book = Book("Test Book", "Author Name", 1234567890), assert book.title == "Test Book", assert book.author == "Author Name", assert book.isbn == 1234567890, assert not book.borrowed | "Test Book", "Author Name", 1234567890 | 'Author Name' = 'Test Book' |Fail| AssertionError: had to reorder my program to match |
| 002 | test_book_creation| book = Book("Test Book", "Author Name", 1234567890), assert book.title == "Test Book", assert book.author == "Author Name", assert book.isbn == 1234567890, assert not book.borrowed | "Test Book", "Author Name", 1234567890 | '"Test Book", "Author Name", 1234567890 |Pass | NA |


## 2

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|

| 001 | test_library_find_book | library = Library(), book = Book("Test Book", "Author Name", 1234567890), library.add_book(book), found = library.find_book(1234567890), assert found == bookn | "Test Book", "Author Name", 1234567890 | 0x10528d8e0 == 0x10528daf0 | Fail | assert none == <Project3.Book object at 0x10409aa50> | 
| 002 | test_library_find_book | library = Library(), book = Book("Test Book", "Author Name", 1234567890), library.add_book(book), found = library.find_book(1234567890), assert found == bookn | "Test Book", "Author Name", 1234567890 | "Test Book", "Author Name", 1234567890 | ----- | ----- | 
| 003 | test_library_find_user | library = Library(), user = User("John Doe", 1), library.add_user(user), found = library.find_user(1), assert found == user | "John Doe", 1 | ---- |Fail | Assertion Error: assert <Project3.User object at 0x10211d100> == <Project3.User object at 0x10211cfb0>|
| 004 | test_library_find_user | library = Library(), user = User("John Doe", 1), library.add_user(user), found = library.find_user(1), assert found == user | "John Doe", 1 | ---- | ---- | ------ |

