from django.db import models
from typing import Optional, List

from thelibrary.infrastructure.django.models.author import Author
from thelibrary.infrastructure.django.models.category import Category

class Book(models.Model):

    class Meta:
        db_table = "books"
        ordering = ['title']

    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', db_column='author_id', on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=500)
    categories = models.ManyToManyField('Category')
    
    def get_categories_names(self):
        categories = ', '.join([category.name for category in self.categories.all()])
        return categories
