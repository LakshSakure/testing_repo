from django import forms

class LoginFrom(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required','id': 'user_name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': 'required', 'id': 'password'}))
