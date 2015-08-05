# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pincode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=6)),
                ('city', models.ForeignKey(related_name='pincode', to='app.City')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('city', models.ForeignKey(related_name='profile_city', to='app.City')),
                ('pincode', models.ForeignKey(related_name='profile_pincode', to='app.Pincode')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.ForeignKey(related_name='profile_state', to='app.State'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(related_name='city', to='app.State'),
        ),
    ]
