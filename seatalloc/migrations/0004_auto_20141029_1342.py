# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seatalloc', '0003_candidate_preference'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='pd',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='candidate',
            name='ds',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
