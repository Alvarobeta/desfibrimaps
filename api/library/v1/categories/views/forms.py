from django import forms
from thelibrary.infrastructure.django.models.category import Category


class CategoryForm(forms.ModelForm):
    
    class Meta: 
        model = Category
        fields = ['name','description']
