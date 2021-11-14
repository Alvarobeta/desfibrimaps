from rest_framework.views import APIView
from django.shortcuts import redirect
from thelibrary.context.library.infrastructure.django.views.book_view import BookView as BookViewCore


class BookView(APIView):
    def get(self, request, book_id):
        return BookViewCore().get(
            request=request,
            book_id=book_id,
        )

    def post(self, request, book_id):
        BookViewCore().delete(
            request=request,
            book_id=book_id
        )

        return redirect('books_view')
