from injector import Module, singleton, provider

from thelibrary.context.library.domain.book import BookRepository
from thelibrary.context.library.infrastructure.django.repositories import BookRepositoryDjango


class ServicesModule(Module):

    def configure(self, binder):
        binder.bind(BookRepository, to=BookRepositoryDjango(), scope=singleton)
