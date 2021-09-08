# Understanding class inheritance

class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Periodical(Publication):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages


class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price, period, publisher)


book = Book("Brave New World", "Aldous Huxley", 311, 29.0)
newspaper = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
magazine = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(book.author)
print(newspaper.publisher)
print(book.price, magazine.price, newspaper.price)