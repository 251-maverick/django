# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seatalloc', '0002_category_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('roll', models.CharField(unique=True, max_length=9)),
                ('cat', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('candidate', models.ForeignKey(to='seatalloc.Candidate', to_field='id')),
                ('institute', models.CharField(max_length=1)),
                ('program', models.CharField(max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
