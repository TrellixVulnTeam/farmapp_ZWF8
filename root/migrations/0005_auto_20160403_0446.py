# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0004_village_pincode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farm_land_details',
            old_name='farmer_id',
            new_name='farmer',
        ),
        migrations.RenameField(
            model_name='farming',
            old_name='farmer_id',
            new_name='farmer',
        ),
        migrations.RenameField(
            model_name='farming',
            old_name='farming_type_id',
            new_name='farming_type',
        ),
        migrations.AddField(
            model_name='farmer_details',
            name='image',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='officer_details',
            name='image',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
