# Generated by Django 2.2.12 on 2021-10-01 00:42

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Part3_T1', '0003_remove_player_game_round_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='num_LTs_Awareded',
            field=otree.db.models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='num_LTs_Awareded_Urn1',
            field=otree.db.models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='num_LTs_Awareded_Urn2',
            field=otree.db.models.FloatField(null=True),
        ),
    ]
