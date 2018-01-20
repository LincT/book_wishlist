

from book import Book
from fileIO import FileIO as fileIO

from pprint import pprint
import json
from datetime import date


DATA_DIR = 'data'
BOOKS_FILE_NAME = str(fileIO.pathJoin(DATA_DIR, 'wishlist.txt'))
COUNTER_FILE_NAME = str(fileIO.pathJoin(DATA_DIR, 'counter.txt'))

separator = '^^^'  # a string probably not in any valid data relating to a book

book_list = []
counter = 0


def setup():
    """ Read book info from file, if file exists. """

    global counter

    data = fileIO.readAsString(BOOKS_FILE_NAME)
    if len(data) > 0:
        make_book_list(data)

    counter = fileIO.readAsPosInt(COUNTER_FILE_NAME)
    if counter == -1:
        counter = len(book_list)

def is_book(book_id):
    '''Checks if a book exists.'''
    for book in book_list:
        if book.id==int(book_id):
            return True
    return False

def shutdown():
    """Save all data to a file - one for books, one for the current counter value, for persistent storage"""

    output_data = make_output_data()

    # Create data directory
    fileIO.mkdir(DATA_DIR)

    # write data to file
    fileIO.overwrite(BOOKS_FILE_NAME,output_data)

    # write counter to data
    fileIO.overwrite(COUNTER_FILE_NAME,counter)


def get_books(**kwargs):
    """ Return books from data store. With no arguments, returns everything. """

    global book_list

    if len(kwargs) == 0:
        return book_list

    if 'read' in kwargs:
        read_books = [book for book in book_list if book.read == kwargs['read']]
        return read_books


def add_book(book):
    """ Add to db, set id value, return Book"""

    global book_list

    book.id = generate_id()
    book_list.append(book)


def generate_id():
    global counter
    counter += 1
    return counter


def set_read(book_id, read):
    """Update book with given book_id to read. Return True if book is found in DB and update is made, False otherwise."""

    global book_list

    for book in book_list:

        if book.id == book_id:
            book.read = True
            book.dateCompleted = str(date.today())
            return True

    return False  # return False if book id is not found

def delete_book(book_id):
    """Remove book with given book_id from booklist."""
    global book_list

    for book in book_list:

        if book.id == int(book_id):
            book_list.remove(book)
            return True
    return False #return False if book id is not found

def set_title(book_id, title):
    '''Update title of given book.  Return True if successful, False if id not found.'''
    for book in book_list:
        if book.id == int(book_id):
            book.title=title
            return True
    return False

def get_title(book_id):
    for book in book_list:
        if book.id==int(book_id):
            return book.title

def set_author(book_id, author):
    '''Update author of given book.  Return True if successful, False if id not found.'''
    for book in book_list:
        if book.id == int(book_id):
            book.author=author
            return True
    return False

def get_author(book_id):
    for book in book_list:
        if book.id==int(book_id):
            return book.author

def make_book_list(string_from_file):
    """ turn the string from the file into a list of Book objects"""

    global book_list

    books_str = string_from_file.split('\n')

    for book_str in books_str:
        if book_str.find(separator) > -1:  # backwards compatibility
            data = book_str.split(separator)
            title = data[0]
            author = data[1]
            read = data[2] == 'True'
            book_id = int(data[3])
            book = Book(title,author,read,book_id)
            book_list.append(book)
        else:
            if len(str(book_str).strip())>=1:
                data = json.loads(book_str)
                for entry in data:
                    title = data[entry]['title']
                    author = data[entry]['author']
                    read = data[entry]['read'] == 'True'
                    book_id = int(str(entry))
                    book = Book(title,author,read,book_id)
                    book_list.append(book)


def make_output_data():
    """ create a string containing all data on books, for writing to output file"""

    global book_list

    output_data = []

    for book in book_list:
        # output = [book.title, book.author, str(book.read), str(book.id)]
        output = \
            {
                str(book.id): {
                    'title':book.title,
                    'author':book.author,
                    'read':str(book.read)
                }
            }
        output_str = json.dumps(output)
        output_data.append(output_str)

    all_books_string = '\n'.join(output_data)

    return all_books_string
