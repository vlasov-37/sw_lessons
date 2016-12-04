#coding: utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here. BlogEntry(name, text, author, date_create, date_modify),
class BlogEntry(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField()
    author = models.CharField(max_length=30, verbose_name='Автор')
    date_create = models.DateTimeField()
    date_modify = models.DateTimeField()
