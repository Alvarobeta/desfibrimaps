from abc import ABC, abstractmethod
from typing import Optional, List
from thelibrary.infrastructure.django.models.category import Category


class CategoryRepository(ABC):

    @abstractmethod
    def find_categories(self) -> Optional[List[Category]]:
        pass

    @abstractmethod
    def find_one_by_id(self, category_id: int) -> Optional[Category]:
        pass

    @abstractmethod
    def update(self, category: Category) -> None:
        pass
    