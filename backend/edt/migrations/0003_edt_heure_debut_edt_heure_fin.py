# Generated by Django 4.1.5 on 2023-01-18 19:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edt', '0002_edt_date_edt_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='edt',
            name='heure_debut',
            field=models.TimeField(blank=True, default=datetime.datetime(2023, 1, 18, 19, 58, 19, 820777, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='edt',
            name='heure_fin',
            field=models.TimeField(blank=True, default=datetime.datetime(2023, 1, 18, 19, 58, 30, 527481, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
