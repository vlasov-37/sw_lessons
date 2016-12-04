# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('text', models.TextField()),
                ('author', models.CharField(verbose_name='Автор', max_length=30)),
                ('date_create', models.DateTimeField()),
                ('date_modify', models.DateTimeField()),
            ],
        ),
    ]
