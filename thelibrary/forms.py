from django import forms
from .infrastructure.django.models import DjangoDea


class DeaForm(forms.ModelForm):
    class Meta: 
        model = DjangoDea
        fields = "__all__"

class NearestDeaForm(forms.ModelForm):
    class Meta:
        model = DjangoDea
        fields = ['lat', 'long'] 