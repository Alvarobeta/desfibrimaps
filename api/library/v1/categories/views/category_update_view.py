from rest_framework.views import APIView
from thelibrary.context.library.infrastructure.django.views.category_update_view import CategoryUpdateView as CategoryUpdateViewCore


class CategoryUpdateView(APIView):
    def get(self, request, category_id):
        return CategoryUpdateViewCore().get(
            request=request,
            category_id=category_id,
        )

    def post(self, request, category_id):
        return CategoryUpdateViewCore().put(
            request=request,
            category_id=category_id
        )
