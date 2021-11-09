from django import forms
from django.forms import ModelChoiceField, ModelMultipleChoiceField

from thelibrary.infrastructure.django.models.book import Book
from thelibrary.infrastructure.django.models.author import Author
from thelibrary.infrastructure.django.models.category import Category

class AuthorModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.full_name

class CategoryModelMultipleChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class BookForm(forms.ModelForm):

    author = AuthorModelChoiceField(queryset=Author.objects.all())
    categories = CategoryModelMultipleChoiceField(queryset=Category.objects.all(), widget = forms.CheckboxSelectMultiple)
    
    class Meta: 
        model = Book
        fields = ['isbn','title','author','categories','description']

# class NearestDeaForm(forms.ModelForm):
#     class Meta:
#         model = DjangoDea
#         fields = ['lat', 'long'] 