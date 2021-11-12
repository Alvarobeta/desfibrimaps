from thelibrary.context.library.domain.book import BookRepository


class DeleteBookHandler:
    def __init__(
        self, 
        book_repository: BookRepository
    ):
        self.book_repository = book_repository


    def __call__(self, book_id: int):   
        
        book = self.book_repository.find_one_by_id(book_id=book_id)
        self.book_repository.delete(book)
