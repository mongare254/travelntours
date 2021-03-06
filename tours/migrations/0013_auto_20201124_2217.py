# Generated by Django 3.1.3 on 2020-11-24 19:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0012_auto_20201123_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='sender',
        ),
        migrations.AddField(
            model_name='chat',
            name='sender',
            field=models.CharField(blank=True, default='Sender', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='update',
            name='date_uploaded',
            field=models.DateField(default=datetime.date(2020, 11, 24)),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
