from rest_framework.views import APIView
from thelibrary.context.library.infrastructure.django.views.book_update_view import BookUpdateView as BookUpdateViewCore


class BookUpdateView(APIView):
    def get(self, request, book_id):
        return BookUpdateViewCore().get(
            request=request,
            book_id=book_id,
        )

    def post(self, request, book_id):
        return BookUpdateViewCore().put(
            request=request,
            book_id=book_id
        )
