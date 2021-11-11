from rest_framework.views import APIView
from django.shortcuts import render
from thelibrary.context.library.infrastructure.django.views.authors_view import AuthorsListView as AuthorsListViewCore
from thelibrary.context.library.infrastructure.django.views.authors_view import AuthorsView as AuthorsViewCore
from api.library.v1.authors.views.forms import AuthorForm


class AuthorsListView(APIView):
    def get(self, request):
        return AuthorsListViewCore().get(
            request=request
        )

class AuthorsView(APIView):
    def get(self, request):
        return render(request, 'author_create.html', {'form': AuthorForm()})

    def post(self, request):
        return AuthorsViewCore().post(request=request)
        