# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruit_transaction',
            name='external_id',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='fruit_transaction',
            name='order_state',
            field=models.CharField(max_length=50, choices=[('created', 'created'), ('pending', 'pending'), ('fineshed', 'fineshed')], default='created'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fruit_transaction',
            name='delivery',
            field=models.ForeignKey(null=True, blank=True, to='root.Delivery'),
        ),
        migrations.AlterField(
            model_name='fruit_transaction',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fruit_transaction',
            name='price',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='fruit_transaction',
            name='yields',
            field=models.ForeignKey(null=True, blank=True, to='root.Yield'),
        ),
    ]
