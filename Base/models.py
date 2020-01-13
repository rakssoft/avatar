from django.db import models
from django.conf import settings

# Create your models here.

class PointA(models.Model):
    income = models.IntegerField(blank=True, null=True)  #доходы
    costs = models.IntegerField(blank=True, null=True)   #расходы
    debts = models.IntegerField(blank=True, null=True)    #долги
    assets = models.IntegerField(blank=True, null=True)       #активы
    capital = models.IntegerField(unique=True, blank=True, null=True)   # капитал

    safety_pillow = models.IntegerField(blank=True, null=True)  # подушка безопасности


class IncomeDaily(models.Model):
    income_daily = models.IntegerField(blank=True, null=True)  #доходы за день
    date_of_day = models.DateField(blank=True, null=True)  # текущая дата
    pillow_all = models.IntegerField(blank=True, null=True) # подушка безопасности
    debts_all = models.IntegerField(blank=True, null=True)  # общий долг

