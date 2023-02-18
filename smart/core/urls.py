from django.urls import path
from . import views

urlpatterns = [
    path('owners/', views.owners_list),
    path('owners/<int:pk>', views.owner_detail)
]
