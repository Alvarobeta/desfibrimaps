# from injector import inject
from rest_framework import response, status
from thelibrary.context.library.domain.author import AuthorRepository
from thelibrary.context.library.infrastructure.django.repositories.author_repository_django import AuthorRepositoryDjango


class UpdateAuthorHandler:
    def __init__(
        self, 
        author_repository: AuthorRepository
    ):
        self.author_repository = author_repository


    def __call__(self, request, author_id: int):   
        author = self.author_repository.find_one_by_id(author_id=author_id)
        self.author_repository.update(request, author)

        return response.Response(status=status.HTTP_201_CREATED, data={'author': author})

