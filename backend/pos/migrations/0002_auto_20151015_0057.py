# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='follow_up_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
