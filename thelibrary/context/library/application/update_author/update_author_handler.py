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
        author.update(
            full_name=request.data['full_name'],
            pseudonym=request.data['pseudonym'],
            born=request.data['born'] if request.data['born'] else None,
            died=request.data['died'] if request.data['died'] else None
        )
        self.author_repository.update(author)

        return response.Response(status=status.HTTP_201_CREATED, data={'author': author})

