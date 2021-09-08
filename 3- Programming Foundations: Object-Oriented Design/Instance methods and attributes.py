# create a basic class
class Book:
    # initializer function not constructor
    def __init__(self, title, price, pages):
        self.title = title
        self.price = price
        self.pages = pages

    # create some instance methods
    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setDiscount(self, amount):
        self._discount = amount


# create book instance of class
book1 = Book("Object-Oriented Programming", 100.00, 680)


# print proerty
print(book1.title)


# try to set discount
print(f"Book price before 25% discount = {book1.getPrice()}")
book1.setDiscount(0.25)
print(f"Book price after 25% discount = {book1.getPrice()}")