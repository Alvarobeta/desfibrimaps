from rest_framework.views import APIView
from django.shortcuts import render, redirect
from thelibrary.context.library.application.get_categories.get_category_handler import GetCategoryHandler
from thelibrary.context.library.application.delete_category import DeleteCategoryHandler
from thelibrary.context.library.infrastructure.django.repositories.category_repository_django import CategoryRepositoryDjango


class CategoryView(APIView):
    def get(self, request, category_id: int):
        get_category_handler = GetCategoryHandler(category_repository=CategoryRepositoryDjango())
        result = get_category_handler(category_id=category_id)    

        return render(request, 'category_detail.html', {'page_obj': result})
    
    def delete(self, request, category_id: int):
        delete_book_handler = DeleteCategoryHandler(category_repository=CategoryRepositoryDjango())
        delete_book_handler(category_id=category_id)

        return redirect('categories_view')
        