from typing import Optional, List
from thelibrary.context.library.domain.category import CategoryRepository
from thelibrary.infrastructure.django.models.category import Category


class CategoryRepositoryDjango(CategoryRepository):

    def find_categories(self) -> Optional[List[Category]]:        
        categories = Category.objects.all()
        
        return categories if categories else None

    def find_one_by_id(self, category_id: int) -> Optional[Category]:
        category = Category.objects.filter(pk=category_id).first()

        return category if category else None
    
    def update(self, category: Category) -> None:
        Category.objects.filter(id=category.id).update(
            name=category.name,
            description=category.description
        )
