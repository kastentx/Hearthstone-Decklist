# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('cost', models.PositiveIntegerField()),
                ('text', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(null=True)),
                ('wins', models.PositiveIntegerField()),
                ('losses', models.PositiveIntegerField()),
                ('cards', models.ManyToManyField(to='decklist.Card')),
            ],
        ),
    ]
