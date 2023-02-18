from django.contrib import admin
from .models import Users, Companies

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    exclude=('user_id',)

@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    exclude=('company_id',)
