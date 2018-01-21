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

    elif choice == '9':
        search()

    elif choice == 'q':
        quit()

    else:
        ui.message('Please enter a valid selection')


def show_unread():
    """Fetch and show all unread books"""
    unread = datastore.get_books(read=False)
    ui.show_list(unread)


def show_read():
    """Fetch and show all read books"""
    read = datastore.get_books(read=True)
    ui.show_list(read)


def book_read():
    """ Get choice from user, edit datastore, display success/error"""
    book_id = ui.ask_for_book_id()
    if datastore.set_read(book_id, True):
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
    if datastore.search(new_book.title) != "No match found":
        if ui.get_input("similar entries found, do you wish to still add this book?").lower()[0]!="y":
            ui.message("entry canceled")
    else:
        datastore.add_book(new_book)
        ui.message('Book added: ' + str(new_book))

def delete_book():
    book_id=ui.ask_for_book_id()
    if datastore.delete_book(book_id):
        ui.message('Successfully deleted')
    else:
        ui.message('Book id not found in database')

def search():
    term = ui.get_input("please enter a search term (not case sensitive)")
    if term != "-1":
        print(datastore.search(term))

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
