# forms.py

from django import forms

class LoginForm(forms.ModelFormForm):
    student_id = forms.CharField(max_length=45)
    password = forms.CharField(widget=forms.PasswordInput)
