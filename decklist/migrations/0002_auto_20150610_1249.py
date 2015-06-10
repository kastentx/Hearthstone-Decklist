# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('decklist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='losses',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='deck',
            name='wins',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
