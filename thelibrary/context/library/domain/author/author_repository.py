from abc import ABC, abstractmethod
from typing import Optional, List
from thelibrary.infrastructure.django.models.author import Author


class AuthorRepository(ABC):

    @abstractmethod
    def find_authors(self) -> Optional[List[Author]]:
        pass

    @abstractmethod
    def find_one_by_id(self, author_id: int) -> Optional[Author]:
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def create(self, author_body: dict) -> Author:
        pass
    
    @abstractmethod
    def update(self, author_body: dict, author: Author) -> None:
        pass

    @abstractmethod
    def delete(self, author: Author) -> None:
        pass
