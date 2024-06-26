from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import AdviceForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Advice(forms.ModelForm):
    class Meta:
        model = AdviceForm
        fields = ['firstname', 'lastname', 'advice']


