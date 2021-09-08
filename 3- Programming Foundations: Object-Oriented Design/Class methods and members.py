# Using class-level and static methods

class Book:
    # Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # double-underscore properties are hidden from other classes
    __bookList = None

    # create a class method
    @classmethod
    def getBookTypes(cls):
        return cls.BOOK_TYPES
    # create a static method
    @staticmethod
    def getBookList():
        if Book.__bookList == None:
            Book.__bookList = []
        return Book.__bookList

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktppe = booktype


# access the class attribute
print(f"Book types is: {Book.getBookTypes()}")

# Create some book instances
book1 = Book("Title 1", "HARDCOVER")
book2 = Book("Title 2", "EBOOK")

# Use the static method to access a singleton object
thebooks = Book.getBookList()
thebooks.append(book1)
thebooks.append(book2)