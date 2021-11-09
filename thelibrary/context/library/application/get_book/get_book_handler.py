# from injector import inject
import thelibrary
from thelibrary.context.library.domain.book import BookRepository, BookId
from thelibrary.infrastructure.django.models.book import Book
from thelibrary.context.library.infrastructure.django.repositories.book_repository_django import BookRepositoryDjango

class GetBookHandler:
    def __init__(
        self, 
        book_repository: BookRepository
    ):
        self.book_repository = book_repository


    def __call__(self, book_id: BookId):        
        book = BookRepositoryDjango.find_one_by_id(self, book_id=book_id)
        return book
