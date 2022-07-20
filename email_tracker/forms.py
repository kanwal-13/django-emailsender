from typing_extensions import Required
from django import forms

class enteruser(forms.Form):
         # each field would be mapped as an input field in HTML
        name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': "form-control"}))
        email_address = forms.EmailField(widget=forms.TextInput(attrs={'class': "form-control"}))
        message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5,'class': "form-control"}))
        subject = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'class': "form-control"}))
