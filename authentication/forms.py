from django.forms import ModelForm
# importing default user registration form
from django.contrib.auth.forms import UserCreationForm
# importing built-in user model
from django.contrib.auth.forms import User
from django import forms
from ads.models import Author

from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class UserRegistrationForm(UserCreationForm):
    # Styling the username form fields
    username = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'name': 'username',
        'placeholder': 'Nazwa użytkownika'
    }))

    # Styling the password1 form fields
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control',
        'name': 'password1',
        'placeholder': 'Hasło'
    }))

    # Styling the password2 form fields
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control',
        'name': 'password2',
        'placeholder': 'Powtórz hasło'
    }))

    # Making the email field required 
    email = forms.EmailField(required=True)

    # Styling the email form fields
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type': 'email',
        'class': 'form-control',
        'placeholder': 'Adres e-mail'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        duplicate_email = User.objects.filter(email=email).exists()
        print("Email Taken")
        if duplicate_email:
            raise forms.ValidationError("This Email address is already in use.")
        return email


class EmailValidationOnForgotPassword(PasswordResetForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={
        'type': 'email',
        'class': 'form-control',
        'placeholder': 'Adres e-mail'
    }))

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise forms.ValidationError("There is no user registered with the specified email address!")

        return email


class EmailSetPassword(SetPasswordForm):
    # Styling the password1 form fields
    new_password1 = forms.CharField(label="", widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control',
        'name': 'new_password1',
        'placeholder': 'Password'
    }))

    # Styling the password2 form fields
    new_password2 = forms.CharField(label="", widget=forms.TextInput(attrs={
        'type': 'password',
        'class': 'form-control',
        'name': 'new_password2',
        'placeholder': 'Retype Password'
    }))


# Updating the User registration form
class UserUpdateForm(ModelForm):
    first_name = forms.CharField(label="Imię", widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'name': 'first_name',
        'placeholder': 'Imię'
    }))

    last_name = forms.CharField(label="Nazwisko", widget=forms.TextInput(attrs={
        'type': 'text',
        'class': 'form-control',
        'name': 'last_name',
        'placeholder': 'Nazwisko'
    }))

    email = forms.EmailField(label="Adres e-mail", widget=forms.TextInput(attrs={
        'type': 'email',
        'class': 'form-control',
        'placeholder': 'Adres e-mail'
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        # exclude = ['user']


# Updating the profile form
class ProfileUpdateForm(ModelForm):
    profile_pic = forms.ImageField(label="Zdjęcie profilowe")

    class Meta:
        model = Author
        fields = ['profile_pic']
