from rest_framework.views import APIView
from django.shortcuts import render
from thelibrary.context.library.application.get_books import GetBookHandler
from thelibrary.context.library.application.update_book import UpdateBookHandler
from thelibrary.context.library.infrastructure.django.repositories.author_repository_django import AuthorRepositoryDjango
from thelibrary.context.library.infrastructure.django.repositories.book_repository_django import BookRepositoryDjango
from thelibrary.context.library.infrastructure.django.repositories.category_repository_django import CategoryRepositoryDjango
from api.library.v1.books.views.forms import BookForm


class BookUpdateView(APIView):
    def get(self, request, book_id: int):
        get_book_handler = GetBookHandler(book_repository=BookRepositoryDjango())
        result = get_book_handler(book_id=book_id)    

        return render(request, 'book_update.html', {'form': BookForm(instance=result.data['book'])})
        
    def put(self, request, book_id: int):        
        book = {
            "isbn": request.data['isbn'],
            "title": request.data['title'],
            "author": request.data['author'],
            "description": request.data['description'],
            "categories": request.data.getlist('categories')
        }

        update_book_handler = UpdateBookHandler(
            author_repository=AuthorRepositoryDjango(), 
            book_repository=BookRepositoryDjango(), 
            category_repository=CategoryRepositoryDjango()
        )
        response = update_book_handler(book_id=book_id, book_body=book)  
        
        if response.status_code != 200:
            error_message = "Something went wrong with the book update, please check all required fields."
            return render(request, 'book_update.html', {'form': BookForm(), 'error_message': error_message})

        return render(request, 'book_detail.html', {'page_obj': response.data['book']})
