# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resurne', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='peopleresurne',
            name='ctime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
