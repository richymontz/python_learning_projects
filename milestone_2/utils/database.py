from .database_connection import DatabaseConnection


def create_book_table():
    _books_database_query('CREATE TABLE IF NOT EXISTS  books '
                          '(name text primary key, author text, read integer)')


def add_book(name, author):
    _books_database_query('INSERT INTO books VALUES(?, ?, 0)', (name, author))


def get_all_books():
    query_results = _books_database_query('SELECT * FROM books', is_select=True)
    books = [
        {'name': row[0], 'author': row[1], 'read': row[2]}
        for row in query_results
    ]

    return books


def read_book(name):
    _books_database_query('UPDATE books SET read = 1 WHERE name = ?', arguments=(name,))


def delete_book(name):
    _books_database_query('DELETE FROM books WHERE name = ?', (name,))


def _books_database_query(query, arguments=(), is_select=False):
    with DatabaseConnection("book_database.db") as connection:
        cursor = connection.cursor()

        if len(arguments) > 0:
            cursor.execute(query, arguments)
        else:
            cursor.execute(query)

        results = []

        if is_select:
            results = cursor.fetchall()

    return results
