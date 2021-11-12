from rest_framework import response, status
from thelibrary.context.library.domain.book import BookRepository
from api.library.v1.books.views.forms import BookForm
from thelibrary.infrastructure.django.models.author import Author
from thelibrary.infrastructure.django.models.category import Category


class CreateBookHandler:
    def __init__(
        self, 
        book_repository: BookRepository
    ):
        self.book_repository = book_repository


    def __call__(self, request):        
        form = BookForm(request.POST)

        if form.is_valid():
            author = Author.objects.get(id=request.data['author'])

            category_ids = request.data.getlist('categories')
            categories = Category.objects.filter(id__in=category_ids)

            book = self.book_repository.create(request, author, categories)

            if book:
                return response.Response(status=status.HTTP_201_CREATED)

        return response.Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
