from rest_framework.views import APIView

from thelibrary.context.library.infrastructure.django.views.books_view import BooksView as BooksViewCore

class BooksView(APIView):
    def get(self, request):
        return BooksViewCore().get(request=request)

    def post(self, request):
        return BooksViewCore().post(request=request)
