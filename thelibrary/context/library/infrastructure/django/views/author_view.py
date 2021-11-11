from rest_framework.views import APIView
from django.shortcuts import render, redirect
from thelibrary.context.library.application.get_authors.get_author_handler import GetAuthorHandler
from thelibrary.context.library.application.delete_author import DeleteAuthorHandler
from thelibrary.context.library.infrastructure.django.repositories.author_repository_django import AuthorRepositoryDjango


class AuthorView(APIView):
    def get(self, request, author_id: int):
        get_author_handler = GetAuthorHandler(author_repository=AuthorRepositoryDjango())
        result = get_author_handler(author_id=author_id)    

        return render(request, 'author_detail.html', {'page_obj': result})
    
    def delete(self, request, author_id: int):
        delete_book_handler = DeleteAuthorHandler(author_repository=AuthorRepositoryDjango())
        delete_book_handler(author_id=author_id)

        return redirect('authors_view')
        