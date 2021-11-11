from typing import Optional, List
from thelibrary.context.library.domain.book import BookRepository
from thelibrary.infrastructure.django.models.author import Author
from thelibrary.infrastructure.django.models.book import Book
from thelibrary.infrastructure.django.models.category import Category


class BookRepositoryDjango(BookRepository):

    def find_one_by_id(self, book_id: int) -> Optional[Book]:
        book = Book.objects.filter(pk=book_id).first()

        return book if book else None
    
    def update(self, request, book: Book, author: Author, categories: List[Category]) -> None:
        book.isbn = request.data['isbn']
        book.title = request.data['title']
        book.description = request.data['description']
        book.author = author
        book.categories.set(categories)
        book.save()
