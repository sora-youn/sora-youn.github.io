# Generated by Django 2.2.12 on 2022-02-27 03:57

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('ExitSurvey', '0003_auto_20220226_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='enjoy',
        ),
        migrations.RemoveField(
            model_name='player',
            name='like',
        ),
        migrations.AddField(
            model_name='player',
            name='advice',
            field=otree.db.models.LongStringField(null=True, verbose_name='Please share any of your trick/strategy/advice in getting higher earnings for the future participants in this game:'),
        ),
    ]
