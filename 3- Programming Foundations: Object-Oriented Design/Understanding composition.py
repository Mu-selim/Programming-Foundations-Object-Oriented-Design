# Using composition to build complex objects


class Book:
    def __init__(self, title, price, author = None):
        self.title = title
        self.price = price

        # Use references to other objects, like author and chapters
        self.author = author
        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def get_book_page_count(self):
        result = 0
        for ch in self.chapters:
            result += ch.page_count
        return result

class Author:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Chapter:
    def __init__(self, name, page_count):
        self.name = name
        self.page_count = page_count

auth = Author("Leo", "Tolstoy")
book = Book("War and Peace", 39.0, auth)

book.addchapter(Chapter("Chapter 1", 125))
book.addchapter(Chapter("Chapter 2", 97))
book.addchapter(Chapter("Chapter 3", 143))


print(book.author)
print(book.title)
print(book.get_book_page_count())