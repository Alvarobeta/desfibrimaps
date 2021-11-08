from typing import Optional, List, Set

from thelibrary.context.library.domain.book import BookId, BookRepository
from thelibrary.infrastructure.django.models.book import Book


class BookRepositoryDjango(BookRepository):

    def find_one_by_id(self, book_id: BookId) -> Optional[Book]:
        book = Book.objects.filter(pk=book_id).first()
        
        print('D'*50)
        print('BookRepositoryDjango')
        print('book: ', book)
        print('D '*50)

        return book if book else None
