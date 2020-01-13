from django.contrib import admin
from django.urls import path
from . import views
from Base.views import *


urlpatterns = [

    path('goals/', goals, name='goals'),
    path('goals/money', money, name='money'),

    path('money/finsecurity', finsecurity, name='finsecurity'),
    path('money/findaily', fin_daily, name='fin_daily'),

    path('money/finsec', finsec, name='finsec'),
    path('money/finsec/finsecA', finsecA, name='finsecA'),
    path('money/finstab', finstab, name='finstab'),
    path('money/finind', finind, name='finond'),
    path('money/finsfree', finfree, name='finfree'),

]
