# from injector import inject
from rest_framework import response, status
from thelibrary.context.library.domain.book import BookRepository
from thelibrary.infrastructure.django.models.author import Author
from thelibrary.infrastructure.django.models.category import Category
from thelibrary.context.library.infrastructure.django.repositories.book_repository_django import BookRepositoryDjango


class UpdateBookHandler:
    def __init__(
        self, 
        book_repository: BookRepository
    ):
        self.book_repository = book_repository


    def __call__(self, request, book_id: int):   

        book = self.book_repository.find_one_by_id(book_id=book_id)

        author = Author.objects.get(id=request.data['author'])

        category_ids = request.data.getlist('categories')
        categories = Category.objects.filter(id__in=category_ids)

        self.book_repository.update(request, book, author, categories)

        return response.Response(status=status.HTTP_201_CREATED, data={'book': book})
