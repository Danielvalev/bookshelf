from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from accounts.models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(
        label='',  # default Username*
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(
        label='',  # default Password*
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password'}),  # Hide the password field
    )


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        labels = {
            'email': 'Email address*',
            'password1': '',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'password': forms.PasswordInput(),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email', False)
        if not email:
            raise forms.ValidationError('Email is required')
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
