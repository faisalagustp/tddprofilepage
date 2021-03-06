# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def find_dupes(apps, schema_editor):
    List = apps.get_model("profileapp", "List")
    for list_ in List.objects.all():
        items = list_.item_set.all()
        texts = set()
        for ix, item in enumerate(items):
            if item.text in texts:
                item.text = '{} ({})'.format(item.text, ix)
                item.save()
            texts.add(item.text)

class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(find_dupes)
    ]
