from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('dev/', admin.site.urls),
    path('', include('census_users.urls', namespace='users')),
    path('', include('census_auth.urls', namespace='auth')),
    path('', include('census_admin.urls', namespace='staff')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
