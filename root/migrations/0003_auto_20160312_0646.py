# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_auto_20160312_0638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taluk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('unique_id', models.CharField(null=True, max_length=256)),
                ('name', models.CharField(null=True, max_length=256)),
                ('district', models.ForeignKey(to='root.District')),
                ('state', models.ForeignKey(to='root.State')),
            ],
        ),
        migrations.AddField(
            model_name='farm_land_details',
            name='taluk',
            field=models.ForeignKey(to='root.Taluk', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farmer_details',
            name='taluk',
            field=models.ForeignKey(to='root.Taluk', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='officer_details',
            name='taluk',
            field=models.ForeignKey(to='root.Taluk', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='village',
            name='taluk',
            field=models.ForeignKey(to='root.Taluk', default=1),
            preserve_default=False,
        ),
    ]
