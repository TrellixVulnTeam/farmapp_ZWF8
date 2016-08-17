# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=256, null=True)),
                ('full_name', models.CharField(max_length=256, null=True)),
                ('email', models.EmailField(max_length=256)),
                ('phone', models.BigIntegerField(default=0)),
                ('idproof_type', models.CharField(blank=True, max_length=25, choices=[('Adhaar', 'Adhaar'), ('VoterId', 'VoterId'), ('RationId', 'RationId'), ('PanId', 'PanId'), ('Other', 'Other')], null=True)),
                ('gender', models.CharField(max_length=25, choices=[('Male', 'Male'), ('Female', 'Female')])),
                ('proof_number', models.CharField(blank=True, max_length=256, null=True)),
                ('image', models.CharField(blank=True, max_length=256, null=True)),
                ('address', models.TextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
