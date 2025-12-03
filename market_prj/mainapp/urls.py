from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'


urlpatterns = [
    path('', mainapp.main, name='index'),  # ← главная страница!
    path('accommodations/', mainapp.accommodations, name='accommodations'),
    path('accommodation/<int:pk>/', mainapp.accommodation, name='accommodation'),
]
