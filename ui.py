from book import Book


def display_menu_get_choice():

    '''Display choices for user, return users' selection'''

    print('''
        1. Show unread books (wishlist)
        2. Show books that have been read
        3. Mark a book as read
        4. Add book to wishlist
        5. Delete a book from the wishlist
        6. Edit a book
        q. Quit
    ''')

    choice = input('Enter your selection: ')

    return choice


def show_list(books):
    ''' Format and display a list of book objects'''

    if len(books) == 0:
        print ('* No books *')
        return

    for book in books:
        print(book)

    print('* {} book(s) *'.format(len(books)))


def ask_for_book_id():

    ''' Ask user for book id, validate to ensure it is a positive integer '''

    while True:
        try:
            id = int(input('Enter book id:'))
            if id >= 0:
                return id
            else:
                print('Please enter a positive number ')
        except ValueError:
            print('Please enter an integer number')


def get_new_book_info():

    ''' Get title and author of new book from user '''

    title = input('Enter title: ')
    author = input('Enter author: ')
    return Book(title, author)


def message(msg):
    '''Display a message to the user'''
    print(msg)

def edit_book_info():
    info=input('1. Change book title.\n2. Change book author. \n3. Return to main menu.\n\nEnter your selection: ')
    if (info == '1') | (info == '2') | (info == '3'):
        return info
    else:
        print('Please enter 1, 2, or 3.')

def get_edit_info(option, old_info):
    if option=='1':
        info=input("Previous book title: "+ old_info+ "\nPlease enter revised title: ")
        return info
    elif option == '2':
        info=input("Previous book author: "+ old_info + "\nPlease enter revised author: ")
        return info