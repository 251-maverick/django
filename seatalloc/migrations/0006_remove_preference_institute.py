# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seatalloc', '0005_auto_20141029_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preference',
            name='institute',
        ),
    ]
