from django.db import models
from django.contrib.auth.models import User
from datetime import date


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mail = models.EmailField(blank=False)
    birth_date = models.DateField(null=False, blank=False, default=date.today)
    MALE = 'M'
    FEMALE = 'F'
    OTHERS = 'O'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHERS, 'Others'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)