from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .router import router


urlpatterns = [
    path('', include('home.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)