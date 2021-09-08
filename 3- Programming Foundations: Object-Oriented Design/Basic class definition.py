# create a basic class
class Book:
    # initializer function not constructor
    def __init__(self, title):
        self.title = title


# create book instance of class
book1 = Book("Object-Oriented Programming")


# print class and proerty
print(book1)
print(book1.title)