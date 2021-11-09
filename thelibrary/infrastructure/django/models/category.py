from django.db import models


class Category(models.Model):

    class Meta:
        db_table = "categories"
        ordering = ['name']

    name = models.CharField(max_length=100)
    description = models.CharField(blank=True, max_length=300, null=True)