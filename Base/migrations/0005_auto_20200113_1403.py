# Generated by Django 3.0.2 on 2020-01-13 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0004_auto_20200113_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeDaily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_daily', models.IntegerField(blank=True, null=True)),
                ('date_of_day', models.DateField(blank=True, null=True)),
                ('pillow_all', models.IntegerField(blank=True, null=True)),
                ('debts_all', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='pointa',
            name='date_of_day',
        ),
    ]
