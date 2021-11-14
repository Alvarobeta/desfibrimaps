from rest_framework.views import APIView
from django.shortcuts import redirect
from thelibrary.context.library.infrastructure.django.views.category_view import CategoryView as CategoryViewCore


class CategoryView(APIView):
    def get(self, request, category_id):
        return CategoryViewCore().get(
            request=request,
            category_id=category_id,
        )

    def post(self, request, category_id):
        CategoryViewCore().delete(
            request=request,
            category_id=category_id
        )

        return redirect('categories_view')
