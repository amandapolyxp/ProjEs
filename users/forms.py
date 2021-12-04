from django import forms
from django.contrib.auth.models import User
from .models import ExtraData
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, PasswordChangeForm
from django.forms import ModelForm


class UserRegistForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'Placeholder':'username'}), label="")
    email = forms.EmailField(widget=forms.TextInput(attrs={'Placeholder':'email'}), label="")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'Placeholder':'password'}), label="")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'Placeholder': 'Confirm password'}), label="")
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
   
        
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'Placeholder': 'Nome'}), label="")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'Placeholder': 'Password'}), label="")

    class Meta:
        model = User
        fields = ['username', 'password']


class UserTokenForm(ModelForm):
    token = forms.CharField(widget=forms.TextInput(attrs={'Placeholder':'GitLab token'}), label="")
    
    class Meta:
        model = ExtraData
        fields = ['token']
        
        
class UserProjectForm(ModelForm):
    proj = forms.DecimalField(widget=forms.TextInput(attrs={'Placeholder':'Project id'}), label="")
    
    class Meta:
        model = ExtraData
        fields = ['proj']

