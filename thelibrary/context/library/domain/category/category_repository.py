from abc import ABC, abstractmethod
from typing import Optional, List
from thelibrary.infrastructure.django.models.category import Category


class CategoryRepository(ABC):

    @abstractmethod
    def find_categories(self) -> Optional[List[Category]]:
        pass

    @abstractmethod
    def find_categories_by_ids(self, category_ids: List[str]) -> Optional[List[Category]]:
        pass

    @abstractmethod
    def find_one_by_id(self, category_id: int) -> Optional[Category]:
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def create(self, category: dict) -> Category:
        pass
    
    @abstractmethod
    def update(self, category_body: dict, category: Category) -> None:
        pass
    
    @abstractmethod
    def delete(self, category: Category) -> None:
        pass