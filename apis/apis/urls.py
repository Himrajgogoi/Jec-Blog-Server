from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .settings import MEDIA_URL,MEDIA_ROOT


urlpatterns = [
    path('', include('articles.urls')),
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls)
] + static(MEDIA_URL, document_root = MEDIA_ROOT)
