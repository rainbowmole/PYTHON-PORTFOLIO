class Book:
    def __init__(self, title, author, isbn, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies

    def __str__(self):
        return f"{self.title} by {self.author}"

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

    def display_books(self):
        for book in self.books:
            print(f"{book} - Available Copies: {book.available_copies}")