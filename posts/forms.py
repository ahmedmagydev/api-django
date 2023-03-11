from django.db import models
from .models import NewProducts
from django import forms


class AddPro(forms.ModelForm):
    class Meta:
        model = NewProducts
        fields = '__all__'

