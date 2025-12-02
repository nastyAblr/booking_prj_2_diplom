
from django.db import models


class ListOfCountries(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name



class Regions(models.Model):
    country = models.ForeignKey(ListOfCountries, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, verbose_name='имя')
    description = models.TextField(blank=True, verbose_name='описание')
    is_active = models.BooleanField(default=True, verbose_name='активна')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('country', 'name')


class Accommodation(models.Model):
    country = models.ForeignKey(ListOfCountries, on_delete=models.CASCADE)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, verbose_name='название проживания')
    image = models.ImageField(upload_to='accommodation_img', blank=True, null=True)
    short_desc = models.TextField(max_length=128, blank=True, verbose_name='краткое описание продукта')
    description = models.TextField(blank=True, verbose_name='описание продукта')
    availability = models.PositiveIntegerField(verbose_name='количество свободных номеров')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name='цена')
    room_desc = models.CharField(max_length=80, blank=True, verbose_name='краткое описание комнаты')
    is_active = models.BooleanField(default=True, verbose_name='активна')

    @staticmethod
    def get_items():
        return Accommodation.objects.filter(is_active=True).order_by('country', 'region', 'name')

    def __str__(self):
        return f'{self.name} ({self.country.name})'

    class Meta:
        verbose_name = 'проживание'
        verbose_name_plural = 'проживания'
        unique_together = ('region', 'name')
