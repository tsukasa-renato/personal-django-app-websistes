# Generated by Django 3.0.7 on 2020-07-11 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0033_auto_20200709_1344'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='products',
            name='unique_product',
        ),
        migrations.AlterField(
            model_name='groups',
            name='user_input',
            field=models.CharField(choices=[('1', 'default'), ('2', 'text'), ('3', 'number'), ('4', 'date'), ('5', 'color'), ('6', 'image')], default='1', max_length=1),
        ),
        migrations.AddConstraint(
            model_name='products',
            constraint=models.UniqueConstraint(fields=('websites', 'slug'), name='unique_product'),
        ),
    ]
