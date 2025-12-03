from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp

urlpatterns = [
    path('admin/', admin.site.urls),

# Главная страница + список размещений + детали — всё отсюда!
    path('', include('mainapp.urls')),

]
