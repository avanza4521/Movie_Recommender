# Generated by Django 3.0.2 on 2020-03-09 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_auto_20200309_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_year',
            field=models.CharField(default=2020, max_length=10),
        ),
    ]
