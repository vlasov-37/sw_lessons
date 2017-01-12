from django.db import models


class Person(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    birth = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    email = models.EmailField(verbose_name='Почта', null=True)

    def years_old(self):
        raise NotImplementedError

    def __unicode__(self):
        return '%s %s' % (self.last_name, self.first_name)

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'


class Passport(models.Model):
    serial = models.PositiveIntegerField('Серия')
    number = models.PositiveIntegerField('Номер')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True, related_name='passport')
    propiska = models.TextField('Прописка')

    def __unicode__(self):
        return '%s %s' % (self.serial, self.number)

    class Meta:
        unique_together = ('serial', 'number')
        verbose_name = 'Паспорт'
        verbose_name_plural = 'Паспорта'
