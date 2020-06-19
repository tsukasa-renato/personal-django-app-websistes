# Generated by Django 3.0.7 on 2020-06-18 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Websites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=50, unique=True)),
                ('images', models.ImageField(blank=True, null=True, upload_to='media')),
                ('title', models.CharField(max_length=20)),
                ('telephone', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('facebook', models.CharField(blank=True, max_length=50, null=True)),
                ('instagram', models.CharField(blank=True, max_length=50, null=True)),
                ('twitter', models.CharField(blank=True, max_length=50, null=True)),
                ('youtube', models.CharField(blank=True, max_length=50, null=True)),
                ('whatsapp', models.CharField(blank=True, max_length=20, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('reason', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
