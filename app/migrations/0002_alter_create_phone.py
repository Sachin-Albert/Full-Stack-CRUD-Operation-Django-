# Generated by Django 5.0.7 on 2024-11-21 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create',
            name='phone',
            field=models.IntegerField(),
        ),
    ]