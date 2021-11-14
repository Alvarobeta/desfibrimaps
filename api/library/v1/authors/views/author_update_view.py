from rest_framework.views import APIView
from thelibrary.context.library.infrastructure.django.views.author_update_view import AuthorUpdateView as AuthorUpdateViewCore


class AuthorUpdateView(APIView):
    def get(self, request, author_id):
        return AuthorUpdateViewCore().get(
            request=request,
            author_id=author_id,
        )

    def post(self, request, author_id):
        return AuthorUpdateViewCore().put(
            request=request,
            author_id=author_id
        )
