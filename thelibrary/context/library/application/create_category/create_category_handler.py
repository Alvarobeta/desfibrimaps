from rest_framework import response, status
from thelibrary.context.library.domain.category import CategoryRepository


class CreateCategoryHandler:
    def __init__(
        self, 
        category_repository: CategoryRepository
    ):
        self.category_repository = category_repository


    def __call__(self, category_body: dict):        
        category = self.category_repository.create(category_body=category_body)
        if category:
            return response.Response(status=status.HTTP_201_CREATED, data={'category': category})

        return response.Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
