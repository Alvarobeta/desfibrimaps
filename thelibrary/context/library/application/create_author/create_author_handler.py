from rest_framework import response, status
from thelibrary.context.library.domain.author import AuthorRepository


class CreateAuthorHandler:
    def __init__(
        self, 
        author_repository: AuthorRepository
    ):
        self.author_repository = author_repository


    def __call__(self, author_body: dict):
        author = self.author_repository.create(author_body=author_body)

        if author:
            return response.Response(status=status.HTTP_201_CREATED, data={'author': author})

        return response.Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
