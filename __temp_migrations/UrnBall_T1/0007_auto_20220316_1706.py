# Generated by Django 2.2.12 on 2022-03-16 22:06

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('UrnBall_T1', '0006_auto_20220316_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='check_GuessInput',
            field=otree.db.models.BooleanField(choices=[[True, 'Confirm']], null=True),
        ),
    ]
