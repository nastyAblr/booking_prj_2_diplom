from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

# Главная страница + список размещений + детали — всё отсюда!
    path('', include('mainapp.urls')),
    path('auth/', include('authapp.urls', namespace='authapp'))

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)