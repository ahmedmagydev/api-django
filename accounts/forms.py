from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname=forms.CharField(max_length=100,required=False,initial='optional.......')
    lastname=forms.CharField(max_length=100,required=False,initial='optional.......')

    class Meta:
        model=User
        fields=['firstname','lastname','username', 'email','password1','password2' ]