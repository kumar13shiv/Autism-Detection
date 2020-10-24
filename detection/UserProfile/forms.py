from django import forms
# from django.contrib.auth.models import User
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'mail', 'birth_date', 'gender')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'mail', 'birth_date', 'gender')
        widgets = {
            'birth_date': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }