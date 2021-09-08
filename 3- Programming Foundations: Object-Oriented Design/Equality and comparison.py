# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    """ the __eq__ method checks for equality between two objects """
    def __eq__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book")

        return (self.title == value.title and
                self.author == value.author and
                self.price == value.price)

    """ the __ge__ establishes >= relationship with another obj """
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book")

        return (self.price < value.price)

    """ the __lt__ establishes < relationship with another obj """
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError("Can't compare book to a non-book")

        return (self.price < value.price)


book1 = Book("War and Peace", "Leo Tolstoy", 39.95)
book2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
book3 = Book("War and Peace", "Leo Tolstoy", 39.95)
book4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

""" Check for equality """
print(book1 == book3)
print(book1 == book2)
# print(book1 == 78) -> Value error
print()

""" Check for greater and lesser value """
print(book2 <= book1)
print(book2 < book1)
print()

""" Now we can sort them too """
books = [book4, book3, book2, book1]
books.sort()
print([book.title for book in books])