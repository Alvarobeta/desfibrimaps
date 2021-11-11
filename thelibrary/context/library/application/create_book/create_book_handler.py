from rest_framework import response, status
from thelibrary.context.library.domain.book import BookRepository
from api.library.v1.books.views.forms import BookForm


class CreateBookHandler:
    def __init__(
        self, 
        book_repository: BookRepository
    ):
        self.book_repository = book_repository


    def __call__(self, request):        
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return response.Response(status=status.HTTP_201_CREATED)

        return response.Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
