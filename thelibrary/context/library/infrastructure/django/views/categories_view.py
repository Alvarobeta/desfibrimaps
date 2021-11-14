from rest_framework.views import APIView
from rest_framework import serializers
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from thelibrary.context.library.application.get_categories.get_categories_handler import GetCategoriesHandler
from thelibrary.context.library.application.create_category.create_category_handler import CreateCategoryHandler
from thelibrary.context.library.infrastructure.django.repositories.category_repository_django import CategoryRepositoryDjango
from api.library.v1.categories.views.forms import CategoryForm


class CategoryPostISerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField(required=False, allow_null=True)

class CategoriesListView(APIView):
    def get(self, request):
        get_categories_list_handler = GetCategoriesHandler(category_repository=CategoryRepositoryDjango())
        result = get_categories_list_handler()    

        paginator = Paginator(result.data['categories'], 10) # Show 10 Categories per page.
        page_number = request.GET.get('page')
        category_list = paginator.get_page(page_number)

        return render(request, 'category_list.html', {'category_list': category_list})


class CategoriesView(APIView):
    def post(self, request):
        serializer_i = CategoryPostISerializer(data=request.data)

        if not serializer_i.is_valid():
            error_message = serializer_i.errors
            return render(request, 'category_create.html', {'form': CategoryForm(), 'error_message': error_message})

        category_body = {
            "name": serializer_i.validated_data['name'],
            "description": serializer_i.validated_data['description']
        }

        create_category_handler = CreateCategoryHandler(category_repository=CategoryRepositoryDjango())
        response = create_category_handler(category_body=category_body)

        if response.status_code != 201:
            error_message = "Something went wrong with the category creation, please check all required fields."
            return render(request, 'category_create.html', {'form': CategoryForm(), 'error_message': error_message})

        return redirect('categories_view')
