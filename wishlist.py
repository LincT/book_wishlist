#Main program

import ui, datastore



def handle_choice(choice):

    if choice == '1':
        show_unread()

    elif choice == '2':
        show_read()

    elif choice == '3':
        book_read()

    elif choice == '4':
        new_book()

    elif choice == '5':
        delete_book()

    elif choice == '6':
        edit_book()

    elif choice == '7':
        search()

    elif choice == 'q':
        quit()

    else:
        ui.message('Please enter a valid selection')


def show_unread():
    '''Fetch and show all unread books, sorted as requested by user.'''
    unread = datastore.get_books(read=False)
    preference=ui.get_sort_info('n')
    if preference=='1':
        ui.show_list(datastore.sort_list('title', unread))
    elif preference=='2':
        ui.show_list(datastore.sort_list('author', unread))
    elif preference=='3':
        ui.show_list(unread)


def show_read():
    '''Fetch and show all read books, sorted as requested by user.'''
    read = datastore.get_books(read=True)
    preference = ui.get_sort_info('r')
    if preference == '1':
        ui.show_list(datastore.sort_list('title', read))
    elif preference == '2':
        ui.show_list(datastore.sort_list('author', read))
    elif preference == '3':
        ui.show_list(datastore.sort_list('rating', read))
    elif preference == '4':
        ui.show_list(read)


def book_read():
    """ Get choice from user, edit datastore, display success/error"""
    book_id = ui.ask_for_book_id()
    rate=ui.get_rating()
    if datastore.set_read(book_id, True, rate):
        ui.message('Successfully updated')
    else:
        ui.message('Book id not found in database')

def edit_book():
    """Get book id from user, edit book title or author, display success/error message"""
    book_id=ui.ask_for_book_id()
    if datastore.is_book(book_id): #does the book exist?
        option=ui.edit_book_info()
        if option == '1':
            title=datastore.get_title(book_id)
            new_title=ui.get_edit_info(option, title)
            datastore.set_title(book_id, new_title)
            ui.message('Book title has been changed')
        elif option == '2':
            author=datastore.get_author(book_id)
            new_author=ui.get_edit_info(option, author)
            datastore.set_author(book_id, new_author)
            ui.message('Book author has been changed')
        else:
            return

    else:
        ui.message('Book id not found in database')

def new_book():
    """Get info from user, add new book"""
    new_book = ui.get_new_book_info()
    if datastore.check_duplicate(new_book.title, new_book.author): #True if duplicate exists
        if ui.get_input("Book with same title and author was already added.  To add anyway, type y.").lower()[0]!="y":
            ui.message("entry canceled")
    else:
        datastore.add_book(new_book)
        ui.message('Book added: ' + str(new_book))

def delete_book():
    """Delete book by book id and report success or failure"""
    book_id=ui.ask_for_book_id()
    if datastore.delete_book(book_id):
        ui.message('Successfully deleted')
    else:
        ui.message('Book id not found in database')

def search():
    """Search title or search author for a given string and display results"""
    option = ui.get_search_input()
    term = ui.get_input("Please type your search term (not case sensitive).")
    if term != "-1":
        ui.message(datastore.search(option, term))

def quit():
    """Perform shutdown tasks"""
    datastore.shutdown()
    ui.message('Bye!')


def main():

    datastore.setup()

    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.display_menu_get_choice()
        handle_choice(choice)


if __name__ == '__main__':
    main()
