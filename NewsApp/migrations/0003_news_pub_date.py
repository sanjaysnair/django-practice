# Generated by Django 3.0.8 on 2020-07-04 08:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0002_sportsnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 7, 4, 8, 19, 45, 905909, tzinfo=utc)),
        ),
    ]
