# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seatalloc', '0004_auto_20141029_1342'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='preference',
            unique_together=set([('candidate', 'program')]),
        ),
    ]
