from dataclasses import dataclass, field
import random

def random_value():
    return float(random.randrange(20, 40))

@dataclass
class Book:
    """ you can define default values when attributes are declared """
    title: str = "No Tilte"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory = random_value)

book1 = Book("War and Peace", "Leo Tolstoy", 1225)
book2 = Book("The Catcher in the Rye", "JD Salinger", 234)
print(book1)
print(book2)