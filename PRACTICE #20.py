class Book:
    def __init__(self, title, author, isbn, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies

    def __str__(self):
        return f"{self.title.title()} by {self.author}"
class Patron:
    def __init__(self, name, library_card_number):
        self.name = name
        self.library_card_number = library_card_number
        self.books_borrowed = []

    def __str__(self):
        return f"{self.name} (Library Card: {self.library_card_number})"
class Library:
    def __init__(self):
        self.books = []
        self.patrons = []
    def display_books(self):Caad
            for book in self.books:
                print(f"{book} - Available Copies: {book.available_copies}")
    def add_book(self, book):
        self.books.append(book)
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
    def register_patron(self, patron):
        self.patrons.append(patron)
    def remove_patron(self, patron):
        if patron in self.patrons:
            self.patrons.remove(patron)
    def borrow_book(self, patron, book):
        if book in self.books and book.available_copies > 0:
            book.available_copies -= 1
            patron.books_borrowed.append(book)
    def return_book(self, patron, book):
        if book in patron.books_borrowed:
            book.available_copies += 1
            patron.books_borrowed.remove(book)
    def display_patrons(self):
        print("Patrons registered in the library:")
        for patron in self.patrons:
            print(patron)
def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add a new book")
        print("2. Remove a book")
        print("3. Register a new patron")
        print("4. Remove a patron")
        print("5. Borrow a book")
        print("6. Return a book")
        print("7. Display list of books")
        print("8. Display list of patrons")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            available_copies = int(input("Enter number of available copies: "))
            book = Book(title, author, isbn, available_copies)
            library.add_book(book)
            print(f"{title.title()} successfully added to the library. ")

        elif choice == '2':
            title = input("Enter title of the book to remove: ")
            low = title.lower()
            for book in library.books:
                if book.title == low:
                    library.remove_book(book)
                    print(f" {title.title()} removed from the library")
                    break

        elif choice == '3':
            name = input("Enter patron's name: ")
            library_card_number = input("Enter patron's library card number: ")
            print(f"Hello {name.title()}, You\'re library card number is {library_card_number}")
            patron = Patron(name, library_card_number)
            library.register_patron(patron)

        elif choice == '4':
            library_card_number = input("Enter patron's library card number to remove: ")
            for patron in library.patrons:
                if patron.library_card_number == library_card_number:
                    print(f"{patron.library_card_number} succesfully removed from the list")
                    library.remove_patron(patron)
                    break

        elif choice == '5':
            library_card_number = input("Enter patron's library card number: ")
            book_title = input("Enter title of the book to borrow: ")
            patron = None
            for p in library.patrons:
                if p.library_card_number == library_card_number:
                    patron = p
                    break
                else:
                    print("Patron not found (´。＿。｀), please try again")
            if patron:
                for book in library.books:
                    if book.title == book_title:
                        library.borrow_book(patron, book)
                        print(f"{book.title} is borrowed by {library_card_number}")
                        print(f"Number of copies of {book.title.title()}: {book.available_copies} ")
                        break

        elif choice == '6':
            library_card_number = input("Enter patron's library card number: ")
            book_title = input("Enter title of the book to return: ")
            patron = None
            for p in library.patrons:
                if p.library_card_number == library_card_number:
                    patron = p
                    break
                else:
                    print("Patron not found (´。＿。｀), please try again")

            if patron:
                for book in patron.books_borrowed:
                    if book.title == book_title:
                        library.return_book(patron, book)
                        print(f"{book.title} is returned by {library_card_number}")
                        print(f"Number of copies of {book.title.title()}: {book.available_copies} ")
                        break

        elif choice == '7':
            library.display_books()

        elif choice == '8':
            library.display_patrons()

        elif choice == '9':
            print("Until next time o(￣┰￣*)ゞ")
            break

        else:
            print("Invalid choice. (っ °Д °;)っ Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()