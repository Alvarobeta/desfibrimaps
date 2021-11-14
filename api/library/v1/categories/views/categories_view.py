from rest_framework.views import APIView
from django.shortcuts import render
from thelibrary.context.library.infrastructure.django.views.categories_view import CategoriesListView as CategoriesListViewCore
from thelibrary.context.library.infrastructure.django.views.categories_view import CategoriesView as CategoriesViewCore
from api.library.v1.categories.views.forms import CategoryForm


class CategoriesListView(APIView):
    def get(self, request):
        return CategoriesListViewCore().get(
            request=request
        )

class CategoriesView(APIView):
    def get(self, request):
        return render(request, 'category_create.html', {'form': CategoryForm()})

    def post(self, request):
        return CategoriesViewCore().post(
            request=request
        )
