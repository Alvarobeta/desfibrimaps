from rest_framework.views import APIView
from django.shortcuts import redirect
from thelibrary.context.library.infrastructure.django.views.author_view import AuthorView as AuthorViewCore


class AuthorView(APIView):
    def get(self, request, author_id):
        return AuthorViewCore().get(
            request=request,
            author_id=author_id,
        )

    def post(self, request, author_id):
        AuthorViewCore().delete(
            request=request,
            author_id=author_id
        )

        return redirect('authors_view')
