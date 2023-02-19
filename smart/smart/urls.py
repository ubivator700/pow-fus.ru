from django.urls import path, include
from django.contrib import admin
from rest_framework import routers

from core import views

router = routers.DefaultRouter()
router.register(r'users', views.UsersViewSet)
router.register(r'analytic', views.AnalyticViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest/', include(router.urls)),
    path('api/', include('core.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
