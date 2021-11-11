from typing import Optional, List
from thelibrary.context.library.domain.author import AuthorRepository
from thelibrary.infrastructure.django.models.author import Author


class AuthorRepositoryDjango(AuthorRepository):

    def find_authors(self) -> Optional[List[Author]]:        
        authors = Author.objects.all()
        
        return authors if authors else None

    def find_one_by_id(self, author_id: int) -> Optional[Author]:
        author = Author.objects.filter(pk=author_id).first()

        return author if author else None
    
    def update(self, author: Author) -> None:
        Author.objects.filter(id=author.id).update(
            full_name=author.full_name,
            pseudonym=author.pseudonym,
            born=author.born,
            died=author.died
        )
