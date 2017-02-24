# coding utf-8
from django.db import models


class Student(models.Model):
    surname = models.CharField('Фамилия', max_length=25)
    name = models.CharField('Имя', max_length=20)
    middlename = models.CharField('Отчество', max_length=20, blank=True, null=True)
    study_group = models.CharField('Учебная группа', max_length=15)

    def __str__(self):
        return self.surname

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class RecordBook(models.Model):
    number = models.CharField('Номер зачетной книжки', max_length=15)
    student = models.OneToOneField('Student', on_delete=models.CASCADE, related_name='student')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Зачетная книжка'
        verbose_name_plural = 'Зачетные книжки'
