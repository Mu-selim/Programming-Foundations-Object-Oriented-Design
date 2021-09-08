from dataclasses import dataclass

@dataclass
class Book:
    title : str
    author : str
    pages : int
    price : float

    def displayInfo(self):
        return f"{self.title} by {self.author}"


""" create some instances """
book1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
book2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
book3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)

""" access fields """
print(book1.title)
print(book2.author)
print()

""" print the book itself - dataclasses implement __repr__ """
print(book1)
print(book2)
print()

""" comparing two dataclasses - they implement __eq__ """
print(book1 == book3)
print()

""" change some fields """
book1.title = "Anna Karenina"
book1.author = "Leo Tolstoy"
print(book1.displayInfo())