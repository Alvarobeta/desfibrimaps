from rest_framework.views import APIView

from django.views import generic

from thelibrary.context.library.infrastructure.django.views.book_view import BookView as BookViewCore

class BookView(APIView):
    def get(self, request, book_id):
        return BookViewCore().get(
            request=request,
            book_id=book_id,
        )
