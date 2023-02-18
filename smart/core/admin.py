from django.contrib import admin
from .models import Users, Companies

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    exclude=('id',)

@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    exclude=('company_id',)
