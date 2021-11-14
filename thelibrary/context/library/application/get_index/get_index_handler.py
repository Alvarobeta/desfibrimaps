from rest_framework import response, status
from thelibrary.context.library.domain.author import AuthorRepository
from thelibrary.context.library.domain.book import BookRepository
from thelibrary.context.library.domain.category import CategoryRepository


class GetIndexHandler:
    def __init__(
        self, 
        author_repository: AuthorRepository,
        book_repository: BookRepository,
        category_repository: CategoryRepository
    ):
        self.author_repository = author_repository
        self.book_repository = book_repository
        self.category_repository = category_repository


    def __call__(self):        
        authors_count = self.author_repository.count()
        books_count = self.book_repository.count()
        categories_count = self.category_repository.count()

        return response.Response(
            status=status.HTTP_302_FOUND, 
            data={'authors_count':authors_count, 'books_count':books_count, 'categories_count':categories_count}
        )