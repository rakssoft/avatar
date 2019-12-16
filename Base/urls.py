from django.contrib import admin
from django.urls import path
from . import views
from Base.views import *


urlpatterns = [

    path('goals/', goals, name='goals')
]
