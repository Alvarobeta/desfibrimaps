from typing import Optional, List
from thelibrary.context.library.domain.category import CategoryRepository
from thelibrary.infrastructure.django.models.category import Category


class CategoryRepositoryDjango(CategoryRepository):

    def find_categories(self) -> Optional[List[Category]]:        
        categories = Category.objects.all()
        
        return categories if categories else None

    def find_categories_by_ids(self, category_ids: List[str]) -> Optional[List[Category]]:        
        categories = Category.objects.filter(id__in=category_ids)
        
        return categories if categories else None

    def find_one_by_id(self, category_id: int) -> Optional[Category]:
        category = Category.objects.filter(pk=category_id).first()

        return category if category else None
    
    def count(self) -> int:
        return Category.objects.all().count()

    def create(self, category_body: dict) -> Category:
        category = Category.objects.create(
            name=category_body['name'],
            description=category_body['description']
        )

        return category

    def update(self, category_body: dict, category: Category) -> None:
        category.update(            
            name=category_body['name'],
            description=category_body['description']
        )
        category.save()

    def delete(self, category: Category) -> None:
        category.delete()
