# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='pincode',
            name='name',
            field=models.CharField(unique=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]
