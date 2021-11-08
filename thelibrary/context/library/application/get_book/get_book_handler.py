from injector import inject
import thelibrary
from thelibrary.context.library.domain.book import BookRepository, BookId
from thelibrary.infrastructure.django.models.book import Book
from thelibrary.context.library.infrastructure.django.repositories.book_repository_django import BookRepositoryDjango

class GetBookHandler:
    @inject
    def __init__(
        self, 
        book_repository: BookRepository
    ):
        self.book_repository = book_repository

    def GetBook(self, book_id: BookId):

        print('GetBookHandler --------------------------------------------------------------------')

        book = BookRepositoryDjango.find_one_by_id(self, book_id=book_id)

        print('C'*50)
        print('GetBookHandler')
        print('book', book.categories.all())
        print('C '*50)
        # categories = book.books.all()
        # print('categories: ', categories)
        print('C '*50)
        # book.categories=book.
        # book_response = Book(
        #     id=book.id,
        #     isbn=book.isbn,
        #     title=book.title,
        #     author = book.author,
        #     description = book.description
        # )


        # book_response.categories.set(book.categories)

        return book
