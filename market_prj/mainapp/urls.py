from django.urls import path, include
import mainapp.views as mainapp

from mainapp import views

app_name = 'mainapp'


urlpatterns = [
    #path('', views.main, name='index'),
    path('', mainapp.main, name='index'),  # ← главная страница!
    path('accommodations/', mainapp.accommodations, name='accommodations'),
    path('accommodation/<int:pk>/', mainapp.accommodation, name='accommodation'),

]
