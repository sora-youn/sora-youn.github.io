# Generated by Django 2.2.12 on 2022-03-16 21:54

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('UrnBall_T1', '0003_player_pointsperg_urn2'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='check_GuessInput',
            field=otree.db.models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
    ]
