# Generated by Django 3.1 on 2021-01-31 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0069_auto_20210121_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='colors',
            name='cart',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Cart color (hexadecimal): '),
        ),
        migrations.AddField(
            model_name='colors',
            name='subcart',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Cart option color (hexadecimal): '),
        ),
    ]
