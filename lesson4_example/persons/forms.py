
from django import forms
from . import models

class Person(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = '__all__'
