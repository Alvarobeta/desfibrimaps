from abc import ABC, abstractmethod
from typing import Optional, List

from thelibrary.context.library.domain.book import BookId
from thelibrary.infrastructure.django.models.author import Author
from thelibrary.infrastructure.django.models.book import Book
from thelibrary.infrastructure.django.models.category import Category


class BookRepository(ABC):

    @abstractmethod
    def find_one_by_id(self, book_id: BookId) -> Optional[Book]:
        pass

    @abstractmethod
    def update(self, book: Book, author: Author, categories: Category) -> None:
        pass