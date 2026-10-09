class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

class Library:
    def __init__(self):
        self.books = []

    def add_books(self, book):
        if book not in self.books:
            self.books.append(book)
        else:
            return f'Книжка {book.title} уже есть в библиотеке'

    def take_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_issued:
                    book.is_issued = True
                    return f'Книжка {book.title} была успешна выдана'
                else:
                    return f'Книжка {book.title} уже выдана'
        return 'Такой книги нету'
    
        
books = [Book('Война и мир', 'Л.Н. Толстой'), Book('Анна Каренина', 'Л.Н. Толстой')]
library = Library()
for book in books:
    library.add_books(book,)
print(library.take_book(title='Война и мир'))
