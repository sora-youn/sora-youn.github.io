# Generated by Django 2.2.12 on 2022-03-27 02:37

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('SliderTask', '0005_auto_20220326_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='Ngreenball',
        ),
        migrations.RemoveField(
            model_name='player',
            name='productivity',
        ),
        migrations.AddField(
            model_name='player',
            name='indi_prod',
            field=otree.db.models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='num_slider',
            field=otree.db.models.FloatField(null=True),
        ),
    ]
