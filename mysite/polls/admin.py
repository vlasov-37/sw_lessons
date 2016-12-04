#coding: utf-8
from django.contrib import admin
from polls import models #импортируем модели

# Register your models here.
admin.site.register(models.BlogEntry) # фукция регистрации в админке принимает объект модели
