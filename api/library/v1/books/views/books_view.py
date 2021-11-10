from rest_framework.views import APIView

from django.shortcuts import render

from thelibrary.context.library.infrastructure.django.views.books_view import BooksView as BooksViewCore

from api.library.v1.books.views.forms import BookForm


class BooksView(APIView):
    def get(self, request):
        return render(request, 'book_create.html', {'form': BookForm()})

    def post(self, request):
        return BooksViewCore().post(request=request)
