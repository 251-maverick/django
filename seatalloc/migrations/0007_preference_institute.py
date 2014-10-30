# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seatalloc', '0006_remove_preference_institute'),
    ]

    operations = [
        migrations.AddField(
            model_name='preference',
            name='institute',
            field=models.CharField(max_length=1, default=1),
            preserve_default=False,
        ),
    ]
