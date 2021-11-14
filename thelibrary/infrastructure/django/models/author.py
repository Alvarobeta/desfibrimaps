from django.db import models
from django.urls import reverse
from typing import Optional
from datetime import date


class Author(models.Model):
    
    class Meta:
        db_table = "authors"
        ordering = ['full_name']

    full_name = models.CharField(max_length=100)
    pseudonym = models.CharField(blank=True, max_length=100, null=True)
    born = models.DateField()
    died = models.DateField(blank=True, null=True, default='')


    def get_detail_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author_view', args=[self.id])

    def update(
        self,
        full_name: Optional[str],
        pseudonym: Optional[str],
        born: Optional[date],
        died: Optional[date]
    ) -> None:
        self.full_name = self.full_name if full_name is None else full_name
        self.pseudonym = self.pseudonym if pseudonym is None else pseudonym
        self.born = self.born if born is None else born
        self.died = self.died if died is None else died
