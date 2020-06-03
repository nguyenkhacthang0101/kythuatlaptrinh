class Book:
    def__init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def__str__(self):
        return "Title:%s, author:%s, pages:%s " %\
               (self.title, self.author, self.pages)

    def__len__(self):
        return self.pages

    def__del__(self):
        print("A book is destroyed")


book = Book("Inside Steve's Brain", "Leonder Vahney", 304)

print(book)
print(len(book))
del(book)
