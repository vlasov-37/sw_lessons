# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=25)),
                ('date_create', models.DateTimeField(verbose_name='Create Date')),
                ('date_modify', models.DateTimeField(verbose_name='Modification Date')),
            ],
        ),
    ]