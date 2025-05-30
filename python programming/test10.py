class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books += 1

    def print_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print("-", book)

    def get_no_of_books(self):
        return self.no_of_books

# Usage example
lib = Library()
lib.add_book("The Great Gatsby")
lib.add_book("1984")
lib.add_book("To Kill a Mockingbird")

lib.print_books()
lib.print_books()

print("Total number of books:", lib.get_no_of_books())

# Demonstrate non-persistence
print("\nRestart the program and run again to see that the books list is empty.")