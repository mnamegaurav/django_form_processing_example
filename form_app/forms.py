from django import forms
from .models import FormData
from django.forms.widgets import PasswordInput

class PracticeForm(forms.Form):

    name = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=10,widget=forms.PasswordInput())
    file = forms.FileField()


class PracticeModelForm(forms.ModelForm):

    class Meta:
        model = FormData
        fields = '__all__'
        widgets = {
        'password':PasswordInput(attrs={'type':'password'}),
        }