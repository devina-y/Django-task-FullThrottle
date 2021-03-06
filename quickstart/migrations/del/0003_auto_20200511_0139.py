# Generated by Django 3.0.6 on 2020-05-10 20:09

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_auto_20200511_0109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity_period',
            options={'ordering': ['start_time']},
        ),
        migrations.AddField(
            model_name='activity_period',
            name='memberss',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='quickstart.member'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity_period',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 11, 1, 38, 52, 317521)),
        ),
        migrations.AlterField(
            model_name='activity_period',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 11, 1, 38, 52, 317521)),
        ),
    ]
