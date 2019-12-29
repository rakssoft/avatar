from django.db import models

# Create your models here.

class PointA(models.Model):
    income = models.IntegerField()  #доходы
    costs = models.IntegerField()   #расходы
    debts = models.IntegerField()    #долги
    assets = models.IntegerField()       #активы
    capital = models.IntegerField()   # капитал
    date_of_day = models.DateField(blank=True, null=True)   #текущая дата

