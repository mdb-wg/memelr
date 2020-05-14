# Generated by Django 3.0.6 on 2020-05-13 20:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_post_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 13, 20, 36, 37, 948822, tzinfo=utc), verbose_name='date posted'),
        ),
        migrations.AlterField(
            model_name='response',
            name='submission_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 13, 20, 36, 37, 971177, tzinfo=utc), verbose_name='date responded'),
        ),
    ]
