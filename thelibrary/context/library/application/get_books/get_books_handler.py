from thelibrary.context.library.domain.book import BookRepository


class GetBooksHandler:
    def __init__(
        self, 
        book_repository: BookRepository
    ):
        self.book_repository = book_repository


    def __call__(self):        
        books = self.book_repository.find_books()
        return books
