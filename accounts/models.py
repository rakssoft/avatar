from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings



class Tests(models.Model):
    testeruserss = models.CharField(max_length=125)
# Create your models here.

class Brand(models.Model):

    name = models.CharField(max_length=100)
    # slug = models.SlugField(null=True)
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    email = models.EmailField(null=False)


class Achievement(models.Model):
    name = models.CharField(max_length=120)
    # status = models.BooleanField()
    # goal = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return 'Profile for user {}'.format(self.user)
