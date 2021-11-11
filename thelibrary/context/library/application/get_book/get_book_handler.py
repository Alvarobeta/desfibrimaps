from thelibrary.context.library.domain.book import BookRepository


class GetBookHandler:
    def __init__(
        self, 
        book_repository: BookRepository
    ):
        self.book_repository = book_repository


    def __call__(self, book_id: int):        
        book = self.book_repository.find_one_by_id(self, book_id=book_id)
        return book
