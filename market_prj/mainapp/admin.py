from django.contrib import admin
from .models import ListOfCountries, Regions, Accommodation

@admin.register(ListOfCountries)
class ListOfCountriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_editable = ('is_active',)

@admin.register(Regions)
class RegionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('country',)

@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'region', 'price', 'availability', 'is_active')
    list_editable = ('price', 'availability', 'is_active')
    list_filter = ('country', 'region')

