from .models import Articles
from django import forms


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'intro', 'whole_text', 'created_date']

        widgets = {
            "title": forms.TextInput(attrs={
                "class": 'form-conrol',
                'placeholder': 'Article title'
            }),
            "intro": forms.TextInput(attrs={
                "class": 'form-conrol',
                'placeholder': 'Article intro'
            }),
            "date": forms.DateTimeInput(attrs={
                "class": 'form-conrol',

            }),
            "date": forms.DateTimeInput(attrs={
                "class": 'form-conrol',
                'placeholder': 'Created text'

            }),
            "whole_text": forms.Textarea(attrs={
                "class": 'form-conrol',
                'placeholder': 'Article text'

            }),
        }