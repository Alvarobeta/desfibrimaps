from rest_framework import response, status
from thelibrary.context.library.domain.author import AuthorRepository
from thelibrary.context.library.domain.book import BookRepository
from thelibrary.context.library.domain.category import CategoryRepository


class UpdateBookHandler:
    def __init__(
        self, 
        author_repository: AuthorRepository,
        book_repository: BookRepository,
        category_repository: CategoryRepository
    ):
        self.author_repository = author_repository
        self.book_repository = book_repository
        self.category_repository = category_repository

    def __call__(self, book_id: int, book_body: dict):   
        book = self.book_repository.find_one_by_id(book_id=book_id)

        author = self.author_repository.find_one_by_id(author_id=book_body['author'])

        category_ids = book_body['categories']
        categories = self.category_repository.find_categories_by_ids(category_ids=category_ids)

        self.book_repository.update(book_body=book_body, book=book, author=author, categories=categories)

        return response.Response(status=status.HTTP_200_OK, data={'book': book})
