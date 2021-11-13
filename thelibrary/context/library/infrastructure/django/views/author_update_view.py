from rest_framework.views import APIView
from django.shortcuts import render
from thelibrary.context.library.application.get_authors.get_author_handler import GetAuthorHandler
from thelibrary.context.library.application.update_author import UpdateAuthorHandler
from thelibrary.context.library.infrastructure.django.repositories.author_repository_django import AuthorRepositoryDjango
from api.library.v1.authors.views.forms import AuthorForm


class AuthorUpdateView(APIView):
    def get(self, request, author_id: int):
        get_author_handler = GetAuthorHandler(author_repository=AuthorRepositoryDjango())
        result = get_author_handler(author_id=author_id)    

        return render(request, 'author_update.html', {'form': AuthorForm(instance=result)})
        
    def put(self, request, author_id: int):   
        author = {
            "full_name": request.data['full_name'],
            "pseudonym": request.data['pseudonym'],
            "born": request.data['born'] if request.data['born'] else None,
            "died": request.data['died'] if request.data['died'] else None
        }   

        update_author_handler = UpdateAuthorHandler(author_repository=AuthorRepositoryDjango())
        response = update_author_handler(author_id=author_id, author_body=author)  
        
        if response.status_code != 200:
            error_message = "Something went wrong with the author update, please check all required fields."
            return render(request, 'author_update.html', {'form': AuthorForm(), 'error_message': error_message})

        return render(request, 'author_detail.html', {'page_obj': response.data['author']})
