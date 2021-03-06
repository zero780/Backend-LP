# Generated by Django 2.2.3 on 2020-01-10 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='availability',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='event_constraint',
            name='max_group_size',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='event_constraint',
            name='max_participant_age',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='event_constraint',
            name='min_group_size',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='event_constraint',
            name='min_participant_age',
            field=models.IntegerField(default=None),
        ),
    ]
