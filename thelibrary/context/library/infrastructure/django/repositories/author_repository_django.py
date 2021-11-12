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

    def create(self, request) -> Author:
        author = Author.objects.create(
            full_name=request.data['full_name'],
            pseudonym=request.data['pseudonym'],
            born=request.data['born'],
            died=request.data['died'] if request.data['died'] else None
        )

        return author

    def update(self, request, author: Author) -> None:
        author.update(
            full_name=request.data['full_name'],
            pseudonym=request.data['pseudonym'],
            born=request.data['born'] if request.data['born'] else None,
            died=request.data['died'] if request.data['died'] else None
        )
        author.save()

    def delete(self, author: Author) -> None:
        author.delete()
