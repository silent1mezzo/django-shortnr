from django import forms
from models import ShortenedUrl

class ShortenerForm(forms.ModelForm):
    class Meta:
        model = ShortenedUrl
        fields = ['url',]