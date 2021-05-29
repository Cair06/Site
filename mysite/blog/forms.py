from django import forms
from .models import *
from django.core.exceptions import ValidationError


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['title', 'body', 'city', 'subcategory']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'city': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'subcategory': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
