from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import *


class PostAdsForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'name': 'title',
        'placeholder': 'Title'
    }))

    description = forms.CharField(widget=CKEditorWidget(attrs={
        'type': 'text',
        'class': 'form-control',
        'name': 'description',
        'placeholder': 'Description'
    }))

    price = forms.CharField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'name': 'price',
        'placeholder': 'Price'
    }))

    city = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'name': 'city',
        'placeholder': 'City'
    }))

    brand = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'name': 'brand',
        'placeholder': 'Brand'
    }))

    phone = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'name': 'phone',
        'placeholder': 'Phone'
    }))

    class Meta:
        model = Ads
        fields = '__all__'
        exclude = ['author', 'date_created', 'is_featured']


class EditAdsForm(forms.ModelForm):
    title = forms.CharField(label="Tytuł", widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'name': 'title',
        'placeholder': 'Title'
    }))

    description = forms.CharField(widget=CKEditorWidget(attrs={
        'type': 'text',
        'class': 'form-control',
        'name': 'description',
        'placeholder': 'Description'
    }))

    price = forms.CharField(label="Cena", widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'name': 'price',
        'placeholder': 'Price'
    }))

    brand = forms.CharField(label="Marka", widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'name': 'brand',
        'placeholder': 'Brand'
    }))

    phone = forms.CharField(label="Telefon kontaktowy", widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'name': 'phone',
        'placeholder': 'Phone'
    }))

    class Meta:
        model = Ads
        fields = 'title', 'description', 'price', 'brand', 'phone'
