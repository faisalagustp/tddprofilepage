# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='text',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(to='profileapp.List', default=None),
        ),
    ]
