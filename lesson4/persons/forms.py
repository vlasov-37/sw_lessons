# coding=utf-8
from django import forms
from . import models

class Person(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = '__all__'


class Message(forms.Form):
    title = forms.CharField(label=u'Заголовок', max_length=255)
    comment = forms.CharField(label=u'Заголовок', max_length=255)
    email = forms.EmailField(label=u'Email')
    post_scriptum = forms.CharField(label=u'П.С.', required=False)

