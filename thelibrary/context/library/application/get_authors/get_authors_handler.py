from thelibrary.context.library.domain.author import AuthorRepository


class GetAuthorsHandler:
    def __init__(
        self, 
        author_repository: AuthorRepository
    ):
        self.author_repository = author_repository


    def __call__(self):        
        authors = self.author_repository.find_authors()
        return authors
