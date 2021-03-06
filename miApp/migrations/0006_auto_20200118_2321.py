# Generated by Django 3.0.2 on 2020-01-18 23:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('miApp', '0005_auto_20200118_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizer',
            name='password',
        ),
        migrations.RemoveField(
            model_name='organizer',
            name='username',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='password',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='username',
        ),
        migrations.AddField(
            model_name='organizer',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(null=True, upload_to='miApp/media'),
        ),
        migrations.AddConstraint(
            model_name='membership',
            constraint=models.UniqueConstraint(fields=('participant', 'group', 'event'), name='unique_membership'),
        ),
        migrations.AddConstraint(
            model_name='notification',
            constraint=models.UniqueConstraint(fields=('participant', 'event_stage'), name='unique_notification'),
        ),
    ]
