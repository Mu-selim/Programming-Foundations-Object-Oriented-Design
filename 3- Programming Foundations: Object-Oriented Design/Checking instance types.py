# Create classes

class Book:
    def __init__(self, title):
        self.title = title

class Newspaper:
    def __init__(self, name):
        self.name = name


# Create some instances of the classes
book1 = Book("Programming Intro")
book2 = Book("Object_Oriented using Python")
newspaper1 = Newspaper("The Washington Post")
newspaper2 = Newspaper("The New York Times")

# Use type to inspect the object type
print(type(book1))
print(type(newspaper1))

# Compare two types together
print(type(book1) == type(book2))
print(type(book1) == type(newspaper1))
print()

# Use instance to Compare a specific instance to a known type
print(isinstance(book1, Book))
print(isinstance(newspaper1, Newspaper))
print(isinstance(newspaper2, Book))
print(isinstance(book2, object))