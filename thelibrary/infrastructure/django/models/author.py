from django.db import models


class Author(models.Model):

    class Meta:
        db_table = "authors"
        ordering = ['full_name']

    full_name = models.CharField(max_length=100)
    pseudonym = models.CharField(blank=True, max_length=100, null=True)
    born = models.DateField(blank=True, null=True)
    died = models.DateField(blank=True, null=True)