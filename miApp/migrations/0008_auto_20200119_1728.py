# Generated by Django 3.0.2 on 2020-01-19 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miApp', '0007_auto_20200118_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='join_code',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
