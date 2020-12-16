# Generated by Django 3.1.3 on 2020-11-16 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=50)),
                ('news_image', models.ImageField(blank=True, upload_to='images/')),
                ('date_uploaded', models.DateField()),
            ],
        ),
    ]