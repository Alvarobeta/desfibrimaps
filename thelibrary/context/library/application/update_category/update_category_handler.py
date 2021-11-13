# from injector import inject
from rest_framework import response, status
from thelibrary.context.library.domain.category import CategoryRepository


class UpdateCategoryHandler:
    def __init__(
        self, 
        category_repository: CategoryRepository
    ):
        self.category_repository = category_repository


    def __call__(self, category_id: int, category_body: dict):   
        category = self.category_repository.find_one_by_id(category_id=category_id)
        self.category_repository.update(category_body=category_body, category=category)

        return response.Response(status=status.HTTP_200_OK, data={'category': category})

