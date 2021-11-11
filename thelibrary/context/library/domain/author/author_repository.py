from abc import ABC, abstractmethod
from typing import Optional, List
from thelibrary.infrastructure.django.models.author import Author
from thelibrary.infrastructure.django.models.author import Author
from thelibrary.infrastructure.django.models.category import Category


class AuthorRepository(ABC):

    @abstractmethod
    def find_authors(self) -> Optional[List[Author]]:
        pass

    @abstractmethod
    def find_one_by_id(self, author_id: int) -> Optional[Author]:
        pass

    @abstractmethod
    def update(self, author: Author) -> None:
        pass
    