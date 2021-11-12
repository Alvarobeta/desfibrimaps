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
    
    def count(self) -> int:
        return Category.objects.all().count()

    def create(self, request) -> Category:
        category = Category.objects.create(
            name=request.data['name'],
            description=request.data['description'] if request.data['description'] else None
        )

        return category

    def update(self, request, category: Category) -> None:
        category.update(            
            name=request.data['name'],
            description=request.data['description']
        )
        category.save()

    def delete(self, category: Category) -> None:
        category.delete()
