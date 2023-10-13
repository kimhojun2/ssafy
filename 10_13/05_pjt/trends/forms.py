from django import forms
from .models import Trend, Keyword

class KeywordForm(forms.ModelForm):
    class Meta:
        model = Keyword
        fields = '__all__'
    