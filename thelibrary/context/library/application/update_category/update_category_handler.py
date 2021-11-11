# from injector import inject
from rest_framework import response, status
from thelibrary.context.library.domain.category import CategoryRepository


class UpdateCategoryHandler:
    def __init__(
        self, 
        category_repository: CategoryRepository
    ):
        self.category_repository = category_repository


    def __call__(self, request, category_id: int):   
        category = self.category_repository.find_one_by_id(category_id=category_id)
        category.update(
            name=request.data['name'],
            description=request.data['description']
        )
        self.category_repository.update(category)

        return response.Response(status=status.HTTP_201_CREATED, data={'category': category})

