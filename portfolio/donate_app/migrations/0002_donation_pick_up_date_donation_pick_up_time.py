# Generated by Django 4.0.6 on 2022-07-24 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='pick_up_date',
            field=models.DateField(default=datetime.date(2022, 7, 24)),
        ),
        migrations.AddField(
            model_name='donation',
            name='pick_up_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]
