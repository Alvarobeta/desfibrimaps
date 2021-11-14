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
    
    def count(self) -> int:
        return Author.objects.all().count()

    def create(self, author_body: dict) -> Author:
        author = Author.objects.create(
            full_name=author_body['full_name'],
            pseudonym=author_body['pseudonym'],
            born=author_body['born'],
            died=author_body['died']
        )

        return author

    def update(self, author_body: dict, author: Author) -> None:
        author.update(
            full_name=author_body['full_name'],
            pseudonym=author_body['pseudonym'],
            born=author_body['born'],
            died=author_body['died']
        )
        author.save()

    def delete(self, author: Author) -> None:
        author.delete()
