# Generated by Django 3.0.8 on 2020-12-15 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0052_auto_20201215_1251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='colors',
            old_name='categories',
            new_name='category',
        ),
    ]