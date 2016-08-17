# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0003_auto_20160312_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='village',
            name='pincode',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
