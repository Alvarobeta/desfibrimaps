from django import forms
from django.forms import widgets
from thelibrary.infrastructure.django.models.author import Author


class AuthorForm(forms.ModelForm):
    
    class Meta: 
        model = Author
        fields = ['full_name','pseudonym','born','died']
        widgets = {
            'born': widgets.DateInput(attrs={'type': 'date'}),
            'died': widgets.DateInput(attrs={'type': 'date'})
        }
