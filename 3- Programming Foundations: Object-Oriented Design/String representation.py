# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    """
    -> use the __str__ method to return a string
    -> The str function is used to provide a user-friendly string description of the object, 
       and is usually intended to be displayed to the user.
    """
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    """
    -> use the __repr__ method to return an obj representation
    -> The repr function is used to generate a more developer-facing string that ideally, can 
       be used to recreate the object in its current state. 
    -> It's commonly used for debugging purposes, so it gets used to display a lot of detailed information.
    """
    def __repr__(self):
        return f"Title = {self.title}, Author = {self.author}, Price = {self.price}"

book1 = Book("War and Peace", "Leo Tolstoy", 39.95)
book2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

print(book1)
print(book2)
print()
print(str(book1))
print(repr(book2))