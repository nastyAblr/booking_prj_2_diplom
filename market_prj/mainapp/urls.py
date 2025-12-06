from django.urls import path, include
import mainapp.views as mainapp


app_name = 'mainapp'


urlpatterns = [

    path('', mainapp.main, name='main'),  # ← главная страница!
    path('accommodations/', mainapp.accommodations, name='accommodations'),
    path('accommodation/<int:pk>/', mainapp.accommodation, name='accommodation'),

]
