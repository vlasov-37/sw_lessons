import datetime
from django.db import models
from django.utils import timezone


class BlogEntry(models.Model):
    name = models.CharField('Название',max_length=25)
    text = models.TextField('Текст')
    author = models.CharField('Автор', max_length=25)
    date_create = models.DateTimeField('Дата создания')
    date_modify = models.DateTimeField('Дата модификации')
    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.date_modify >= timezone.now() - datetime.timedelta(days=1)
