from rest_framework import response, status
from thelibrary.context.library.domain.author import AuthorRepository


class DeleteAuthorHandler:
    def __init__(
        self, 
        author_repository: AuthorRepository
    ):
        self.author_repository = author_repository


    def __call__(self, author_id: int):   
        
        author = self.author_repository.find_one_by_id(author_id=author_id)
        self.author_repository.delete(author=author)
        
        return response.Response(status=status.HTTP_204_NO_CONTENT)