# Generated by Django 3.0.2 on 2020-01-09 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointa',
            name='capital',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
    ]