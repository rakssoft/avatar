# Generated by Django 3.0.2 on 2020-01-09 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0002_auto_20200109_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointa',
            name='assets',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
        migrations.AlterField(
            model_name='pointa',
            name='costs',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
        migrations.AlterField(
            model_name='pointa',
            name='date_of_day',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
        migrations.AlterField(
            model_name='pointa',
            name='debts',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
        migrations.AlterField(
            model_name='pointa',
            name='income',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
    ]