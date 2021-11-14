from rest_framework import response, status
from thelibrary.context.library.domain.book import BookRepository


class GetBookHandler:
    def __init__(
        self, 
        book_repository: BookRepository
    ):
        self.book_repository = book_repository


    def __call__(self, book_id: int):        
        book = self.book_repository.find_one_by_id(book_id=book_id)
        
        return response.Response(status=status.HTTP_302_FOUND, data={'book': book})
