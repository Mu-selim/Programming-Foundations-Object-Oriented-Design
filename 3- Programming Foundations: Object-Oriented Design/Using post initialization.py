from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    """
    the __post_init__ function lets us customize additional properties
    after the object has been initialized via built-in __init__
    """
    def __post_init__(self):
        self.description = f"{self.title} by {self.author}, {self.pages} pages"

""" create some Book objects """
book1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
book2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

""" use the description attribute """
print(book1.description)
print(book2.description)