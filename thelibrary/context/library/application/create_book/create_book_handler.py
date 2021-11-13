from rest_framework import response, status
from thelibrary.context.library.domain.author import AuthorRepository
from thelibrary.context.library.domain.book import BookRepository
from thelibrary.context.library.domain.category import CategoryRepository
from api.library.v1.books.views.forms import BookForm
from thelibrary.infrastructure.django.models.book import Book

class CreateBookHandler:
    def __init__(
        self, 
        author_repository: AuthorRepository,
        book_repository: BookRepository,
        category_repository: CategoryRepository
    ):
        self.author_repository = author_repository
        self.book_repository = book_repository
        self.category_repository = category_repository


    def __call__(self, book: dict):  
        author = self.author_repository.find_one_by_id(author_id=book['author'])

        category_ids = book['categories']
        categories = self.category_repository.find_categories_by_ids(category_ids=category_ids)

        book = self.book_repository.create(book=book, author=author, categories=categories)
        
        if book:
            return response.Response(status=status.HTTP_201_CREATED, data={'book': book})

        return response.Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
