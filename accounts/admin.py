from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Brand,  Achievement, Profile


from .forms import CustomUser
from django.contrib import admin


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']




class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'username', 'age', 'profile']
    model = CustomUser
    profile = Profile

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Brand)
admin.site.register(Achievement)

