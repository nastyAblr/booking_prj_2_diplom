from django.contrib.auth.models import AbstractUser
from django.db import models


class TravelUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(default=18, verbose_name='возраст')


class TravelUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж')
    )

    user = models.OneToOneField(TravelUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE) # один юзер один профиль
    tagline = models.CharField(max_length=128, blank=True, verbose_name='теги')
    aboutMe = models.TextField(max_length=512, blank=True, verbose_name='о себе')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, verbose_name='пол')
