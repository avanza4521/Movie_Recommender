# Generated by Django 3.0.2 on 2020-04-26 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_auto_20200420_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Twitter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_tweet', models.CharField(max_length=50)),
            ],
        ),
    ]
