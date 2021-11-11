from rest_framework.views import APIView
from django.shortcuts import render, redirect
from thelibrary.context.library.application.get_authors.get_authors_handler import GetAuthorsHandler
from thelibrary.context.library.application.create_author.create_author_handler import CreateAuthorHandler
from thelibrary.context.library.infrastructure.django.repositories.author_repository_django import AuthorRepositoryDjango
from api.library.v1.authors.views.forms import AuthorForm


class AuthorsListView(APIView):
    def get(self, request):
        get_authors_list_handler = GetAuthorsHandler(author_repository=AuthorRepositoryDjango())
        result = get_authors_list_handler()    
        
        return render(request, 'author_list.html', {'author_list': result})


class AuthorsView(APIView):
    def post(self, request):
        create_author_handler = CreateAuthorHandler(author_repository=AuthorRepositoryDjango())
        response = create_author_handler(request=request)

        if response.status_code != 201:
            error_message = "Something went wrong with the user creation, remember to fill the required fields"
            return render(request, 'author_create.html', {'form': AuthorForm(), 'error_message': error_message})

        return redirect('index')
