# Generated by Django 2.2.12 on 2022-03-29 18:07

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('RiskAmb', '0002_player_ambig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='risk',
            field=otree.db.models.PositiveIntegerField(choices=[[0, ''], [1, ''], [2, ''], [3, ''], [4, ''], [5, ''], [6, ''], [7, ''], [8, ''], [9, ''], [10, '']], null=True),
        ),
    ]
