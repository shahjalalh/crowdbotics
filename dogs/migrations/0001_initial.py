# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-04 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Date of birth')),
            ],
        ),
    ]
