from django.db import models


class Book(models.Model):

    class Meta:
        db_table = "books"
        ordering = ['title']

    id = models.UUIDField(primary_key=True)
    isbn = models.CharField(max_length=13)
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', db_column='author_id', on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=500)
    categories = models.ManyToManyField('Category')
    
    def get_categories_names(self):
        categories = ', '.join([category.name for category in self.categories.all()])
        print('categories'*20)
        print('CATEGORIES: ', categories)
        print('categories'*20)
        return categories