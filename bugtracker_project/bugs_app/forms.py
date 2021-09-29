from django import forms
from .models import Bug

class AddBugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('name','desc','priority','state','assigned_user','comments')
        widgets = {
            'name': forms.TextInput(attrs = {
                'class': 'form-control'
            }),
            'desc': forms.Textarea(attrs = {
                'class': 'form-control'
            }),
            'comments': forms.Textarea(attrs = {
                'class': 'form-control'
            }),
            'priority': forms.Select(attrs = {
                'class': 'form-control'
            }),
            'state': forms.Select(attrs = {
                'class': 'form-control'
            }),
            'assigned_user': forms.TextInput(attrs = {
                'class': 'form-control'
            })
        }

