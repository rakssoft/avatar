# Generated by Django 2.2.7 on 2019-12-25 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_achievement_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='achievement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Achievement'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Brand'),
        ),
    ]
