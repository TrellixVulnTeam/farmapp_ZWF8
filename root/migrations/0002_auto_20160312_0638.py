# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taluk',
            name='district',
        ),
        migrations.RemoveField(
            model_name='taluk',
            name='state',
        ),
        migrations.RemoveField(
            model_name='farm_land_details',
            name='taluk',
        ),
        migrations.RemoveField(
            model_name='farmer_details',
            name='taluk',
        ),
        migrations.RemoveField(
            model_name='officer_details',
            name='taluk',
        ),
        migrations.RemoveField(
            model_name='village',
            name='taluk',
        ),
        migrations.DeleteModel(
            name='Taluk',
        ),
    ]
