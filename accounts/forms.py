from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class SignupForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','email','age','gender',)
        
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)