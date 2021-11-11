from rest_framework import response, status
from thelibrary.context.library.domain.category import CategoryRepository
from api.library.v1.categories.views.forms import CategoryForm


class CreateCategoryHandler:
    def __init__(
        self, 
        category_repository: CategoryRepository
    ):
        self.category_repository = category_repository


    def __call__(self, request):        
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return response.Response(status=status.HTTP_201_CREATED)

        return response.Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
