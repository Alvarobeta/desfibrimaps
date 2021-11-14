from rest_framework import response, status
from thelibrary.context.library.domain.author import AuthorRepository


class GetAuthorHandler:
    def __init__(
        self, 
        author_repository: AuthorRepository
    ):
        self.author_repository = author_repository


    def __call__(self, author_id: int):        
        author = self.author_repository.find_one_by_id(author_id=author_id)
        
        return response.Response(status=status.HTTP_302_FOUND, data={'author': author})
