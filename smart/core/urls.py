from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users_list),
    path('user/<int:pk>', views.user_detail),

    path('companies/', views.companies_list),
    path('company/<int:pk>', views.company_detail),

    path('analytic/', views.analytics_list),
    path('analytic/<str:name>', views.analytics_detail),

    path('actions/', views.action_list)
]
