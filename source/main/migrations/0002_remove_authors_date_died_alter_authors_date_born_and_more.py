# Generated by Django 4.2.4 on 2023-11-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authors',
            name='date_died',
        ),
        migrations.AlterField(
            model_name='authors',
            name='date_born',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='authors',
            name='interests',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]