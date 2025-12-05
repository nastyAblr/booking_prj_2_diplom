from django.urls import path

from authapp import views

app_name = 'authapp'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),

    # восстановление пароля
    path('password-reset/', views.TravelPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', views.TravelPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', views.TravelPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/complete/', views.TravelPasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
