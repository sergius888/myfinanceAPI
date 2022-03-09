from json import JSONEncoder


# we defined the class named Book
class Book:
    def __init__(self, name, author, pages):
        self.name = name  # we create an object variable in self.name
        self.author = author
        self.pages = pages
        self.pages_read = 0

    def add_pages_read(self, pages_read):
        self.pages_read += pages_read

    def get_percent_read(self):
        return int(self.pages_read / self.pages * 100)


# book1 = Book("Game of Thrones", "George Martin", 600)  # we created an object from class Book
# book2 = Book("2052", "Jørgen Randers", 473)
#
# print(book1.name)

if __name__ == "__main__":
    pass
