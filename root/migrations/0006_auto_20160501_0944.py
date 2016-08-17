# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0005_auto_20160403_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer_details',
            name='mobile',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='officer_details',
            name='mobile',
            field=models.BigIntegerField(default=0),
        ),
    ]
