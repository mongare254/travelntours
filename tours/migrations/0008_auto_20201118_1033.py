# Generated by Django 3.1.3 on 2020-11-18 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0007_auto_20201118_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publichat',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]
