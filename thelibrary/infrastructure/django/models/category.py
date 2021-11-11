from django.db import models
from django.urls import reverse
from typing import Optional


class Category(models.Model):

    class Meta:
        db_table = "categories"
        ordering = ['name']

    name = models.CharField(max_length=100)
    description = models.CharField(blank=True, max_length=300, null=True)


    def get_absolute_url(self):
        """Returns the url to access a particular category instance."""
        return reverse('category_view', args=[self.id])

    def update(
        self,
        name: Optional[str],
        description: Optional[str]
    ) -> None:
        self.name = self.name if name is None else name
        self.description = self.description if description is None else description