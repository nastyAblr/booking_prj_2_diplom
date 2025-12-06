from django.urls import path
from authapp import views as authapp  # подключаем views

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login_view, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('register/', authapp.register, name='register'),
    path('edit/', authapp.edit, name='edit'),
]
