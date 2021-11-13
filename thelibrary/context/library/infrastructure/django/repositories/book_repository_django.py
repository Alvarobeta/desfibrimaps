from typing import Optional, List
from thelibrary.context.library.domain.book import BookRepository
from thelibrary.infrastructure.django.models.author import Author
from thelibrary.infrastructure.django.models.book import Book
from thelibrary.infrastructure.django.models.category import Category


class BookRepositoryDjango(BookRepository):

    def find_books(self) -> Optional[List[Book]]:        
        books = Book.objects.all()
        
        return books if books else None

    def find_one_by_id(self, book_id: int) -> Optional[Book]:
        book = Book.objects.filter(pk=book_id).first()

        return book if book else None
    
    def count(self) -> int:
        return Book.objects.all().count()

    def create(self, book: dict, author: Author, categories: Category) -> Book:
        book = Book.objects.create(
            isbn=book['isbn'],
            title=book['title'],
            description=book['description'],
            author=author
        )

        book.categories.set(categories)

        return book

    def update(self, book_body: dict, book: Book, author: Author, categories: List[Category]) -> None:
        book.isbn = book_body['isbn']
        book.title = book_body['title']
        book.description = book_body['description']
        book.author = author
        book.categories.set(categories)
        book.save()

    def delete(self, book: Book) -> None:
        book.delete()
