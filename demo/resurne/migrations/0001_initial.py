# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 18:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=40)),
                ('educationTitle', models.TextField(max_length=1600)),
            ],
        ),
        migrations.CreateModel(
            name='PeopleResurne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ima_url', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=20)),
                ('birthday', models.CharField(max_length=30)),
                ('identityCard', models.CharField(max_length=20)),
                ('identityNum', models.CharField(max_length=18)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=40)),
                ('other', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workTimeStart', models.CharField(max_length=20)),
                ('workTimeEnd', models.CharField(max_length=20)),
                ('workUnit', models.CharField(max_length=40)),
                ('workTitle', models.TextField(max_length=1600)),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resurne.PeopleResurne')),
            ],
        ),
        migrations.AddField(
            model_name='education',
            name='people',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resurne.PeopleResurne'),
        ),
    ]