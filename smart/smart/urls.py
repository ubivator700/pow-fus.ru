from django.urls import path, include
from django.contrib import admin
from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
