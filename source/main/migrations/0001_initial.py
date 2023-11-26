# Generated by Django 4.2.4 on 2023-11-26 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country_of_origin', models.CharField(blank=True, max_length=25)),
                ('date_born', models.DateTimeField()),
                ('date_died', models.DateTimeField(blank=True)),
                ('interests', models.CharField(max_length=255)),
            ],
        ),
    ]