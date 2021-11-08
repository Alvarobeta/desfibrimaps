from rest_framework.views import APIView

from django.views import generic

from thelibrary.context.library.infrastructure.django.views.books_view import BooksView as BooksViewCore
from thelibrary.infrastructure.django.models.book import Book

class BooksView(APIView):
    def get(self, request, book_id):
        return BooksViewCore().get(
            request=request,
            book_id=book_id,
        )

# class BooksView(generic.DetailView):
#     model = Book
#     template_name = 'dea.html'