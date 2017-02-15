from django.db import models

# Create your models here.


class Author(models.Model):
    login = models.CharField('Логин', max_length=100)
    name = models.CharField('Имя', max_length=20, blank=True, null=True)
    surname = models.CharField('Фамилия', max_length=40, blank=True, null=True)
    birthday = models.DateField('Дата рождения')

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Tag(models.Model):
    tag_name = models.CharField('Название тега', max_length=30)
    tag_detail = models.CharField('Краткое описание тега', max_length=255)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Record(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст')
    author = models.OneToOneField('Author', related_name = 'Автор')
    tags = models.ManyToManyField('Tag', related_name='Теги')
    pub_date = models.DateTimeField('Дата создания')
    modify_date = models.DateTimeField('Дата модификации', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'