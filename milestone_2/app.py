from utils import database

USER_CHOICE = """
Enter:
- 'a'  to add a new book
- 'l'  to list all books
- 'r'  to mark a book as read
- 'd'  to delete a book
- 'q' to quit
Your choice: """


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)

    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        if user_input == 'l':
            list_books()
        if user_input == 'r':
            prompt_mark_as_read()
        if user_input == 'd':
            prompt_delete_book()

        user_input = input(USER_CHOICE)


def prompt_add_book():
    name = input('Please enter a book name: ')
    author = input('Please enter the Author: ')

    database.add_book(name, author)


def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")


def prompt_mark_as_read():
    name = input('Please enter the book name: ')
    database.read_book(name)


def prompt_delete_book():
    name = input('Please enter the book name: ')
    database.delete_book(name)


menu()
