class Book:

    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages

book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)

gosho = Book("gosho", "pesho", 254)
print(gosho.name)
print(gosho.author)
print(gosho.pages)