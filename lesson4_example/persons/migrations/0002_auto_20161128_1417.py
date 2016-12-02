# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birth',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f', blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='\u041f\u043e\u0447\u0442\u0430', blank=True),
        ),
    ]
