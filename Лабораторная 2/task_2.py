BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# класс Book
class Book:
    def __init__(self, id_=None, name='', pages=None):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга "{self.name}"'


# класс Library
class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self.books = books

    def get_book_ids(self):
        return [book.id for book in self.books] or None

    def get_next_book_id(self):
        book_ids = self.get_book_ids()
        if book_ids is None:
            next_book_id = 1
        else:
            next_book_id = sorted(book_ids)[-1] + 1
        return next_book_id

    def get_index_by_book_id(self, book_id):
        return self.get_book_ids().index(book_id)


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
