from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import Profile
from Base.models import PointA, IncomeDaily

User = get_user_model()





class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Passwords don\'t match.')
            return cd['password2']

class PointAForm(forms.ModelForm):
    class Meta:
        model = PointA
        fields = ('income', 'costs', 'debts', 'assets')


class IncomeDailyForm(forms.ModelForm):
    class Meta:
        model = IncomeDaily
        fields = ('income_daily', 'pillow_all', 'debts_all')
