# coding=utf-8
from django.db import models

# Create your models here.
class Person(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)

    birth = models.DateField(u'Дата рождения', blank=True, null=True)
    email = models.EmailField(u'Почта', blank=True)


    def __unicode__(self):
        return '%s %s' % (self.last_name, self.first_name )
    # date_modify = models.DateField(auto_now=True)
    # date_create = models.DateField(auto_now_add=True)
