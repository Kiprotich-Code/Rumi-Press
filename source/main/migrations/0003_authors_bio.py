# Generated by Django 4.2.4 on 2023-11-27 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_authors_date_died_alter_authors_date_born_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
