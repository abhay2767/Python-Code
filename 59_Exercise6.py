""" Write a Library with no_of_books and books as two instance variable. Write a program to
    create a Library class and show how you can print all the books, add a book and get the
    number of books using different methods. Show that your program does not persist the books
    after the program is stoped
 """
class Library:
    def __init__(self):
        self.noOfBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noOfBooks = len(self.books)

    def showinfo(self):
        print(f"The Library has {self.noOfBooks} books")
        for book in self.books:
            print(book)

li = Library()
li.addBook("Learn Pyhton")
li.addBook("Learn Java")
li.showinfo()
