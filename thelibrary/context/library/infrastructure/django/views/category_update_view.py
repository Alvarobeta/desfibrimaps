from rest_framework.views import APIView
from django.shortcuts import render
from thelibrary.context.library.application.get_categories.get_category_handler import GetCategoryHandler
from thelibrary.context.library.application.update_category import UpdateCategoryHandler
from thelibrary.context.library.infrastructure.django.repositories.category_repository_django import CategoryRepositoryDjango
from api.library.v1.categories.views.forms import CategoryForm


class CategoryUpdateView(APIView):
    def get(self, request, category_id: int):
        get_category_handler = GetCategoryHandler(category_repository=CategoryRepositoryDjango())
        result = get_category_handler(category_id=category_id)    

        return render(request, 'category_update.html', {'form': CategoryForm(instance=result.data['category'])})
        
    def put(self, request, category_id: int):     
        category = {
            "name": request.data['name'],
            "description": request.data['description']
        }   

        update_category_handler = UpdateCategoryHandler(category_repository=CategoryRepositoryDjango())
        response = update_category_handler(category_id=category_id, category_body=category)  
        
        if response.status_code != 200:
            error_message = "Something went wrong with the category update, please check all required fields."
            return render(request, 'category_update.html', {'form': CategoryForm(), 'error_message': error_message})

        return render(request, 'category_detail.html', {'page_obj': response.data['category']})
