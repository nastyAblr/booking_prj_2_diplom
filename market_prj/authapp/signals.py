from django.db.models.signals import post_save
from django.dispatch import receiver
from authapp.models import TravelUser, TravelUserProfile

# Сигнал на создание профиля при создании пользователя
@receiver(post_save, sender=TravelUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        TravelUserProfile.objects.create(user=instance)


# (опционально) сохранять профиль при сохранении пользователя
@receiver(post_save, sender=TravelUser)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'traveluserprofile'):
        instance.traveluserprofile.save()

