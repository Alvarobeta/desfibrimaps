from rest_framework.views import APIView
from rest_framework import serializers
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from thelibrary.context.library.application.get_authors.get_authors_handler import GetAuthorsHandler
from thelibrary.context.library.application.create_author.create_author_handler import CreateAuthorHandler
from thelibrary.context.library.infrastructure.django.repositories.author_repository_django import AuthorRepositoryDjango
from api.library.v1.authors.views.forms import AuthorForm


class AuthorPostISerializer(serializers.Serializer):
    full_name = serializers.CharField()
    pseudonym = serializers.CharField(required=False, allow_null=True)
    born = serializers.DateField()
    died = serializers.DateField(required=False, allow_null=True)

class AuthorsListView(APIView):
    def get(self, request):
        get_authors_list_handler = GetAuthorsHandler(author_repository=AuthorRepositoryDjango())
        result = get_authors_list_handler()    
        
        paginator = Paginator(result.data['authors'], 10) # Show 10 Authors per page.
        page_number = request.GET.get('page')
        author_list = paginator.get_page(page_number)

        return render(request, 'author_list.html', {'author_list': author_list})


class AuthorsView(APIView):
    def post(self, request):
        serializer_i = AuthorPostISerializer(data=request.data)

        if not serializer_i.is_valid():
            error_message = serializer_i.errors
            return render(request, 'author_create.html', {'form': AuthorForm(), 'error_message': error_message})

        author_body = {
            "full_name": serializer_i.validated_data['full_name'],
            "pseudonym": serializer_i.validated_data['pseudonym'],
            "born": serializer_i.validated_data['born'],
            "died": serializer_i.validated_data['died']
        }

        create_author_handler = CreateAuthorHandler(
            author_repository=AuthorRepositoryDjango()
        )
    
        response = create_author_handler(author_body=author_body)

        if response.status_code != 201:
            error_message = "Something went wrong with the author creation, please check all required fields."
            return render(request, 'author_create.html', {'form': AuthorForm(), 'error_message': error_message})

        return redirect('authors_view')
