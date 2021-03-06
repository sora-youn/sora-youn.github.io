# Generated by Django 2.2.12 on 2022-04-02 18:42

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eexitsurvey_group', to='otree.Session')),
            ],
            options={
                'db_table': 'eExitSurvey_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eexitsurvey_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'eExitSurvey_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('sex', otree.db.models.StringField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Decline to state', 'Decline to state')], max_length=10000, null=True)),
                ('age', otree.db.models.IntegerField(choices=[(18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59)], null=True)),
                ('major', otree.db.models.StringField(choices=[('Yes.', 'Yes.'), ('No.', 'No.')], max_length=10000, null=True)),
                ('advice', otree.db.models.LongStringField(null=True, verbose_name='Your comment here:')),
                ('part1', otree.db.models.StringField(choices=[('Very easy', 'Very easy'), ('Easy', 'Easy'), ('Hard', 'Hard'), ('Very hard', 'Very hard')], max_length=10000, null=True)),
                ('comment', otree.db.models.LongStringField(null=True, verbose_name='Your comment here:')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eExitSurvey.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eexitsurvey_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eexitsurvey_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eExitSurvey.Subsession')),
            ],
            options={
                'db_table': 'eExitSurvey_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eExitSurvey.Subsession'),
        ),
    ]
