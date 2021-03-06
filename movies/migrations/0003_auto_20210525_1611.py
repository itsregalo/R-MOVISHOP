# Generated by Django 3.1.7 on 2021-05-25 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_auto_20210513_1814'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rating',
            new_name='MovieRating',
        ),
        migrations.AlterField(
            model_name='tvseries',
            name='cover_image',
            field=models.ImageField(upload_to='images/series/covers'),
        ),
        migrations.CreateModel(
            name='TvReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TvRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.tvseries')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
