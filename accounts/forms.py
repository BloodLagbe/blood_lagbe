# from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta:
        """Meta class"""
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone')
