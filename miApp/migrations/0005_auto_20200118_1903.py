# Generated by Django 3.0.2 on 2020-01-18 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0004_auto_20200118_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='availability',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(null=True, upload_to='miApp/static/images/events'),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='event_constraint',
            name='max_group_size',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='event_constraint',
            name='max_participant_age',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='event_constraint',
            name='min_group_size',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='event_constraint',
            name='min_participant_age',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='event_stage',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='status',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='status',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='status',
            field=models.BooleanField(default=True, null=True),
        ),
    ]