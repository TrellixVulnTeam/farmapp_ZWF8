# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0006_auto_20160501_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmer_details',
            name='assignee',
        ),
        migrations.RemoveField(
            model_name='farmer_details',
            name='qualification_details',
        ),
        migrations.AlterField(
            model_name='crop_life_cycle',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='crop_life_cycle',
            name='image',
            field=models.CharField(max_length=256, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='crop_life_cycle',
            name='video',
            field=models.CharField(max_length=256, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='key',
            field=models.CharField(max_length=256, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='status',
            field=models.CharField(max_length=256, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='farm_land_details',
            name='image',
            field=models.CharField(max_length=256, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='farmer_details',
            name='account_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='farmer_details',
            name='account_number',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='farmer_details',
            name='image',
            field=models.CharField(max_length=256, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='farmer_details',
            name='proof_number',
            field=models.CharField(max_length=256, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='farming',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='officer_details',
            name='image',
            field=models.CharField(max_length=256, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='officer_details',
            name='proof_number',
            field=models.CharField(max_length=256, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yield',
            name='cost_end_of_farm',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yield',
            name='final_yield',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yield',
            name='image',
            field=models.CharField(max_length=256, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yield',
            name='no_of_units_sold_fruit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yield',
            name='no_of_units_to_seed',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yield',
            name='spend_per_unit',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='yield',
            name='video',
            field=models.CharField(max_length=256, blank=True, null=True),
        ),
    ]
