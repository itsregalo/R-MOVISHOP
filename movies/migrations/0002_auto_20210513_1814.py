# Generated by Django 3.1.7 on 2021-05-13 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='is_hd',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tvseries',
            name='is_hd',
            field=models.BooleanField(default=True),
        ),
    ]
