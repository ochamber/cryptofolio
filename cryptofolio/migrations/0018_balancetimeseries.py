# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-21 21:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cryptofolio', '0017_timeseries'),
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceTimeSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('amount', models.FloatField(blank=True, default=None, null=True)),
                ('currency', models.CharField(default='BTC', max_length=10)),
                ('fiat', models.CharField(default='USD', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
