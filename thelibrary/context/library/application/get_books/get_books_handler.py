from rest_framework import response, status
from thelibrary.context.library.domain.book import BookRepository


class GetBooksHandler:
    def __init__(
        self, 
        book_repository: BookRepository
    ):
        self.book_repository = book_repository


    def __call__(self):        
        books = self.book_repository.find_books()
 
        return response.Response(status=status.HTTP_302_FOUND, data={'books': books})
        