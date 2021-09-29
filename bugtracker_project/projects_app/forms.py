from django import forms
from .models import Project
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'organization_name': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'desc': forms.Textarea(attrs = {
                'class': 'form-control'
            }),
            'sector': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'technology': forms.TextInput(attrs = {
                'class': 'form-control'
            })
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']