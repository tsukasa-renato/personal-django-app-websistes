# Generated by Django 3.0.7 on 2020-06-19 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0003_auto_20200618_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='websites',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 19, 8, 33, 34, 600869)),
        ),
        migrations.AlterField(
            model_name='websites',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
