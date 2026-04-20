# Simple Library Management System

books = [
    'The Great Gatsby', 
    'To Kill a Mockingbird', 
    '1984', 
    'Pride and Prejudice', 
    'Moby Dick', 
    'The Catcher in the Rye', 
    'The Hobbit', 
    'Brave New World', 
    'The Lord of the Rings', 
    'Fahrenheit 451', 
    'The Alchemist', 
    'Crime and Punishment', 
    'Linear Algebra Done Right', 
]

authors = [
    'F. Scott Fitzgerald', 
    'Harper Lee', 
    'George Orwell', 
    'Jane Austen', 
    'Herman Melville', 
    'J.D. Salinger', 
    'J.R.R. Tolkien', 
    'Aldous Huxley', 
    'J.R.R. Tolkien', 
    'Ray Bradbury', 
    'Paulo Coelho', 
    'Fyodor Dostoevsky', 
    'Sheldon Axler', 
]

availability = [
    True, 
    True, 
    True, 
    True, 
    True, 
    True, 
    True, 
    True,
    True, 
    True, 
    True, 
    True, 
    False,
]

borrowers = [
    None, 
    None, 
    None, 
    None, 
    None, 
    None, 
    None, 
    None,
    None, 
    None, 
    None, 
    None,
    'Tom', 
]

history = [
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    [], 
    ['Tom'], 
]

users = [
    'Tom', 
]

user_borrow_books = [
    ['Linear Algebra Done Right'], 
]


# Functions

def add_book(title, author):
    """
    Adds a new book to the library.

    Parameters:
    - title (str): The title of the book.
    - author (str): The author of the book.
    """
    # TODO: Task 1
    if title in books:
        print(f"Book '{title}' already exists in the library.")
    else:
        books.append(title)
        authors.append(author)
        availability.append(True)
        borrowers.append(None)
        history.append([])
        print(f"Book '{title}' added to the library.")

def remove_book(title):
    """
    Removes a book from the library.

    Parameters:
    - title (str): The title of the book.
    """
    # TODO: Task 1
    if title in books:
        index = books.index(title)
        if availability[index] == True:
            books.pop(index)
            authors.pop(index)
            availability.pop(index)
            borrowers.pop(index)
            history.pop(index)
            print(f"Book '{title}' has been removed from the library.")
        else:
            print(f"Cannot remove '{title}' as it is currently checked out.")
    else:
        print(f"Book '{title}' does not exist in the library.")

def check_out_book(username, title):
    """
    Checks out a book to a user.

    Parameters:
    - username (str): The user's name.
    - title (str): The title of the book.
    """
    # TODO: Task 2
    if title not in books:
        print(f"Book '{title}' does not exist in the library.")
    else:
        index = books.index(title)
        if availability[index] == False:
            print(f"Book '{title}' is currently not available.")
        else:
            availability[index] = False
            borrowers[index] = username
            history[index].append(username)
            if username not in users:
                users.append(username)
                user_borrow_books.append([title])
            else:     
                borrow_index = users.index(username)
                user_borrow_books[borrow_index].append(title)
            print(f"Book '{title}' has been checked out to user '{username}'.")
        



def return_book(username, title):
    """
    Returns a book from a user.

    Parameters:
    - username (str): The user's name.
    - title (str): The title of the book.
    """
    # TODO: Task 2
    if title not in books:
        print(f"Book '{title}' does not exist in the library.")
    else:
        index = books.index(title)
        if availability[index] == True:
            print(f"Book '{title}' is not currently checked out.")
        else:
            if borrowers[index] != username:
                print(f"Book '{title}' is not checked out by user '{username}'.")
            else:
                borrow_index = users.index(username)
                availability[index] = True
                borrowers[index] = None
                user_borrow_books[borrow_index].remove(title)
                if user_borrow_books[borrow_index] == []:
                    user_borrow_books.pop(borrow_index)
                    users.pop(borrow_index)
                print(f"Book '{title}' has been returned by user '{username}'.")
def search_books(keyword, check_avail):
    """
    Searches for books by keyword in the title.

    Parameters:
    - keyword (str): The keyword to search for.
    - check_avail (bool): Whether we only show available books
    """
    # TODO: Task 3
    lower_keyword = keyword.lower()
    if check_avail == True:
        search_result = [book for book in books if lower_keyword in book.lower() and availability[books.index(book)] == True]
    else:
        search_result = [book for book in books if lower_keyword in book.lower() if check_avail == False ]
    print("Search results:")
    if search_result == []:
        print("(No books found with the given keyword)")
    else:
        for s in search_result:
            print(f"- {s} by {authors[books.index(s)]}")

def view_borrowing_history(title):
    """
    Views the borrowing history of a book.

    Parameters:
    - title (str): The title of the book.
    """
    # TODO: Task 4
    if title not in books:
        print(f"Book '{title}' does not exist in the library.")
    else:
        index = books.index(title)
        print(f"Borrowing history for '{title}':")
        if history[index] == []:
            print(f"No borrowing history for this book.")
        else:
            for i in range(1,len(history[index])+1):
                print(f"{i}. {history[index][i-1]}")
def main():
    """
    Main function to run the library system.
    """
    while True:
        print("\nWelcome to the Simple Library Management System")
        print("Please choose an option:")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Check Out a Book")
        print("4. Return a Book")
        print("5. Search for Books")
        print("6. View Borrowing History")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            title = input("Enter the book title: ").strip()
            author = input("Enter the author name: ").strip()
            add_book(title, author)
        elif choice == '2':
            title = input("Enter the book title to remove: ").strip()
            remove_book(title)
        elif choice == '3':
            username = input("Enter your username: ").strip()
            title = input("Enter the book title to check out: ").strip()
            check_out_book(username, title)
        elif choice == '4':
            username = input("Enter your username: ").strip()
            title = input("Enter the book title to return: ").strip()
            return_book(username, title)
        elif choice == '5':
            keyword = input("Enter a keyword to search for: ").strip()
            show_avail_response = input("List only the available books? (Y/N) ")
            check_avail = (show_avail_response.lower() == "y")
            search_books(keyword, check_avail)
        elif choice == '6':
            title = input("Enter the book title to view history: ").strip()
            view_borrowing_history(title)
        elif choice == '7':
            print("Thank you for using the library system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the script
if __name__ == "__main__":
    main()
