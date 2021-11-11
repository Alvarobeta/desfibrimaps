# from injector import inject
from rest_framework import response, status
from thelibrary.context.library.domain.author import AuthorRepository
from api.library.v1.authors.views.forms import AuthorForm


class CreateAuthorHandler:
    def __init__(
        self, 
        author_repository: AuthorRepository
    ):
        self.author_repository = author_repository


    def __call__(self, request):        
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return response.Response(status=status.HTTP_201_CREATED)

        return response.Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
