from abc import ABC, abstractmethod
from typing import Optional, List
from thelibrary.infrastructure.django.models.author import Author
from thelibrary.infrastructure.django.models.book import Book
from thelibrary.infrastructure.django.models.category import Category


class BookRepository(ABC):

    @abstractmethod
    def find_books(self) -> Optional[List[Book]]:
        pass

    @abstractmethod
    def find_one_by_id(self, book_id: int) -> Optional[Book]:
        pass
    
    @abstractmethod
    def count(self) -> int:
        pass
    
    @abstractmethod
    def create(self, book: dict, author: Author, categories: Category) -> Book:
        pass
    
    @abstractmethod
    def update(self, book_body: dict, book: Book, author: Author, categories: Category) -> None:
        pass
    
    @abstractmethod
    def delete(self, book: Book) -> None:
        pass