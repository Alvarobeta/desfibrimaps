from abc import ABC, abstractmethod
from typing import Optional, List

from thelibrary.context.library.domain.book import BookId
from thelibrary.infrastructure.django.models.book import Book


class BookRepository(ABC):

    @abstractmethod
    def find_one_by_id(self, book_id: BookId) -> Optional[Book]:
        pass
